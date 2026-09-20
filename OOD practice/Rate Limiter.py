'''
设计并实现一个 rate limiter：限制某个 client 调用某个 service 的频率
限制规则：每个 client 每分钟最多 N/limit 次（图里写的是 N = 10）
 
最小实现：bool should_limit(Request new_request, int limit_request_count) 
 
request: "hh:mm:ss"
'''


from dataclasses import dataclass
from collections import deque

@dataclass
class Request:

    time: str    

    def to_sec(self) -> int:

        hour, minute, sec = list(map(int, self.time.split(':')))
        return hour * 3600 + minute * 60 + sec
    
class RateLimiter:

    def __init__(self, client: str):

        self.client = client
        self.queue = deque()
        self.window = 60

    def should_limit(self, request: Request, limit:int) -> bool:

        time = request.to_sec()

        while self.queue and self.queue[0] <= time - self.window:

            self.queue.popleft()

        if len(self.queue) >= limit:
            return True # limited
        
        self.queue.append(time)
        return False









'''
# 解：用一个deque来保持每个client 每分钟的窗口 ，窗口大小 <= limit
# 为什么不是单调queue？ 时间戳本来就是单调递增的
# 为什么不用ordereddict？ 只需要维护limit = n 以及是否队头弹出 不用从中间删除/挪动节点
# 这里是每个client一个rate limiter； 如果有很多clients
# 也可以在rate limiter里面设一个字典，每个client一个queue

from collections import deque
from dataclasses import dataclass 

@dataclass
class Request:

    time:str

    # 把request转换成int时间戳 这个会简单很多很多
    # request = "hh:mm:ss"
    def to_sec(self) -> int:

        h, m, s = map(int, self.time.split(":"))
        return h * 3600 + m * 60 + s

class RateLimiter:

    def __init__(self, client:str):

        self.client = client
        self.queue = deque()
        self.WINDOW = 60

    # the head of the queue is the earliest valid request
    # the window size always <= limit
    def should_limit(self, request: Request, limit:int) -> bool:

        now = request.to_sec()

        # 先清理过期！！
        # 如果queue前面的元素已经不在当前时间戳的60s内 需要弹出
        while self.queue and (self.queue[0] <= now - self.WINDOW):
            self.queue.popleft()

        # check the queue 如果窗口内已经有10个request 不允许再request
        if len(self.queue) >= limit:
            return True # return true表示要限流
        
        # 否则可以加入
 
        self.queue.append(now)
        return False # return false表示放行


'''
