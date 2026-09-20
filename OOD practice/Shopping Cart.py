'''
购物车
这是一道经典的社交网络 + 数据聚合题目

基础版： 给定用户的朋友列表和每个人的购物记录，找出朋友中购买最多的商品（排序输出）
Follow-up： 扩展到朋友的朋友（2跳/ n跳），用 BFS/DFS 遍历社交图

# 用户的朋友关系图
friends = {
    "Alice": ["Bob", "Carol"],
    "Bob": ["Alice", "Dave"],
    ...
}

# 每个用户的购物记录
purchases = {
    "Bob":   ["iPhone", "AirPods", "iPhone"],
    "Carol": ["AirPods", "MacBook"],
    "Dave":  ["iPhone", "MacBook"],
}
'''
from collections import Counter, deque
from typing import Dict, List
# 如果面试官只给个数据结构形式 比如告诉你friends是dict 可以自己可视化出来

class SocialPurchases:

    def __init__(self, friends:Dict[str, List[str]], purchases:Dict[str, List[str]]):

        self.friends = friends
        self.purchases = purchases

    # calculate the frequencies of goods user's friends. output: reversely ordered goods by frequencies
    # user themselves not count
    def friend_purchases(self, user:str) -> List[str]:

        freq = Counter()

        friends_list = self.friends[user]
        if not friends_list:
            return []
        
        for friend in friends_list:
            for item in self.purchases[friend]:

                freq[item] += 1

        item_list = [item for item, count in sorted(freq.items(), reverse=True, key=lambda x:x[1])] # sort dictionary by count
        return item_list
    
    def friend_purchases_with_k(self, user:str, k:int) -> List[str]:

        # graph bfs; k friend layers; iterate friends layer by layer
        # k == 2, we can calculate frequencies of user's friends' friends.
        # every friend is node of graph

        freq = Counter()

        friends_list = self.friends[user]
        if not friends_list:
            return []
        
        queue = deque(friends_list) # queue中是第一层朋友列表
        visited = set(friends_list) | {user} # user is not included
        layer = 0

        while queue:

            layer += 1

            for _ in range(len(queue)):

                friend = queue.popleft()

                for item in self.purchases[friend]:

                    freq[item] += 1

                new_friends = self.friends[friend]
                for new_friend in new_friends:

                    if new_friend not in visited:

                        visited.add(new_friend)
                        queue.append(new_friend)

            # 本层遍历完看看是不是到k
            if layer == k:
                break

        purchase_list = [item for item, _ in sorted(freq.items(), reverse=True, key=lambda x:x[1])]
        return purchase_list








'''
from collections import Counter, deque
from typing import Dict, List

class ShoppingReference:

    def __init__(self, friends: Dict[str, List[str]], purchases: Dict[str, List[str]]):

        self.friends = friends
        self.purchases = purchases

    # 仅需找出user的朋友的最爱物品排序列表
    def friend_perferences(self, user:str) -> List[str]:

        friends_list = self.friends[user]

        # edge
        if not friends_list:
            return []

        freq = Counter()
        for friend in friends_list:

            purchase_list = self.purchases[friend]

            for item in purchase_list:
                freq[item] += 1

        # 仅返回根据物品freq次数的倒序列表 dict.items()的x[0]是key, x[1]是value； key=lambda x:x[1]就是根据value排序
        # 或者 用most_common() API: preference_list = [item for item, _ in freq.most_common()]
        perference_list = [item for item, _ in sorted(freq.items(), reverse=True, key=lambda x:x[1])]

        return perference_list

    # 根据朋友的朋友的朋友的 （多少个朋友取决于k） 购买列表，输出朋友最爱物品排序列表
    def friends_perferences_with_k(self, user:str, k:int) -> List[str]:

        freq = Counter()

        # graph BFS
        curr_friends = self.friends[user] # first layer of nodes
        queue = deque(curr_friends)
        visited = set(curr_friends) # protect itteration from graph cycle (repeated friend?)
        visited.add(user)  # 防止 user 自己被算进去 //// 要clarify好 自己算不算进去？
        depth = 0

        while queue:

            depth += 1

            for _ in range(len(queue)):
            
                friend = queue.popleft()

                # 把当前节点的数据取出来 计算
                for item in self.purchases[friend]:

                    freq[item] += 1

                for new_friend in self.friends[friend]:
                    if new_friend not in visited:
                        queue.append(new_friend)
                        visited.add(new_friend) # 不要忘记加visited！！！！BFS+环永恒的visited!!!!!!!!!!!!!!
            
            # 当前层如果已经是k层，所有k层内的朋友已经遍历完，break
            if depth == k:
                break

        preferences_list = [item for item, value in sorted(freq.items(), reverse=True, key=lambda x:x[1])]

        return preferences_list
'''



