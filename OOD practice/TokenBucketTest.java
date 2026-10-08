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