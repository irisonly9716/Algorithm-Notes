public class TokenBucket {
    private final long capacity;        // 桶的最大容量(允许的最大突发量)
    private final double refillRate;    // 每秒补充多少个令牌(长期平均速率)
    private double tokens;              // 当前令牌数
    private long lastRefillTimestamp;   // 上次"结算"的时间点(纳秒)

    public TokenBucket(long capacity, double refillRate) {
        this.capacity = capacity;
        this.refillRate = refillRate;
        this.tokens = capacity;                     // 一开始桶是满的
        this.lastRefillTimestamp = System.nanoTime();
    }

    // 尝试拿 1 个令牌,成功返回 true(放行),失败返回 false(限流)
    public synchronized boolean tryAcquire() {
        refill();
        if (tokens >= 1) {
            tokens -= 1;
            return true;
        }
        return false;
    }

    // 核心:按经过的时间,把该补的令牌补上
    private void refill() {
        long now = System.nanoTime();
        double elapsedSeconds = (now - lastRefillTimestamp) / 1_000_000_000.0;
        double tokensToAdd = elapsedSeconds * refillRate;
        if (tokensToAdd > 0) {
            tokens = Math.min(capacity, tokens + tokensToAdd);  // 补满就不再多加
            lastRefillTimestamp = now;
        }
    }
}

// 如果需要多个实例共享一个令牌桶 那就需要redis来存令牌状态 redis天然单线程/天然命令是原子的 没有中间态 而且操作很快
// TC:O(1)
// SC:O(1)


/* 
public class TokenBucketTest {
    public static void main(String[] args) throws InterruptedException {
        TokenBucket bucket = new TokenBucket(5, 2);

        // 连续请求 7 次
        for (int i = 1; i <= 7; i++) {
            boolean allowed = bucket.tryAcquire();
            System.out.println("Request " + i + ": " + allowed);
        }

        // 等 1 秒，让桶补 2 个 token
        Thread.sleep(1000);

        System.out.println("After 1 second:");

        for (int i = 1; i <= 3; i++) {
            boolean allowed = bucket.tryAcquire();
            System.out.println("Request " + i + ": " + allowed);
        }
    }
}
*/




