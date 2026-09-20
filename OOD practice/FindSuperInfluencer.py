'''
题意：社交网络上有 n 个具有强大影响力的用户，我们需要找到其中的超级影响者，超级影响者需要满足：

没有关注任何其他有影响力的用户

其他有影响力的用户都关注了他

他的关注者数量比其他任何人都大至少 1M

我们可以假设下面两个函数已经被实现：

Followers(a, b)，如果 a 关注了 b，那么就返回 true，否则返回 false。

getFollowersCount(a)，返回关注 a 的用户个数。

'''
# clarify
# 用户的储存形式是什么？ -> integer, 范围是[1， n]
# task：need to find a candidate 
# 1. who has no followee
# 2. all n-1 other user follows him/her
# 3. he/she has 1M followers more than others

class solution:

    def followers(self, a:int, b:int) -> bool:
        pass

    def get_followers_count(self, a:int) -> int:
        pass

    def find_Super_influencer(self, n:int) -> int:

        candidate = 1

        # 先找到这个candidate 这是题目的考点 ⭐线性遍历找到一个i 它没有关注它后面的所有其他i --elimination strategy--
        for i in range(2, n + 1): # 在 [1...i] 这些人里，candidate 是唯一“还可能成为答案的人”

            # if candidate follows i, the original candidate is not valid, try i
            if self.followers(candidate, i):
                candidate = i

        # now we find a candidate who does not follow any one, check if everyone follows him/her.
        for i in range(1, n + 1):

            if i == candidate:
                continue

            # candidate不能关注任何人
            if self.followers(candidate, i):
                return -1
        
            # 任何人不能不关注candidate
            if not self.followers(i, candidate):
                return -1
            
        # check the candiate's follower number >= every other candidate + 1,000,000
        follower = self.get_followers_count(candidate)

        for i in range(1, n + 1):

            if i == candidate:
                continue

            if self.get_followers_count(i) + 1000000 > follower:
                return -1

        return candidate

            


