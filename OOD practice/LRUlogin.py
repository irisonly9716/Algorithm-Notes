'''
用户登录系统 找出只登录过一次的最早用户

newUserLogin(username)
getOldestOneTimeVisitingUser()

'''

# LRU OOD 变种
# 一个新用户登录需要插入双向链表的头节点 
# O(1) 时间找出在尾节点的一次登录用户
# LRU里面存的是只登录一次的用户 如果用户二次登录 O(1)把其移除 所以需要字典O(1)找到这个用户的节点
# 还需要一个set 装进二次登录过的用户 不然如果用户 三次登录 LRU里不存在 会被当成首次登录

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:

    key: str = "" # default value
    prev: Optional["Node"] = None # Node还没有定义完 要加字符串引号
    next: Optional["Node"] = None

class LRUcache:

    def __init__(self):

        self.dummy = Node()
        self.tail = Node()
        self.dummy.next = self.tail
        self.tail.prev = self.dummy

        self.dict = {} # {key: node} # 可以改成once_user 不然有点泛泛
        self.twice_set = set() # {username}

    def new_user_login(self, username:str) -> None:

        # if the user in twice set, return
        # 已经出现过至少两次，后面直接忽略
        if username in self.twice_set:
            return
        
        # if it is the first time the user login, insert the node to the head
        # 用户第一次登录：进链表
        if username not in self.dict:
            
            node = Node(key=username)

            self.dict[username] = node

            node.next = self.dummy.next
            node.prev = self.dummy
            self.dummy.next.prev = node
            self.dummy.next = node

            
        # if the user is in the LRU, remove them and add them to the twice_set.
        # 第二次登录：从 once 中删除，并放入 twice_set
        else:

            del_node = self.dict[username]
            del self.dict[username]

            self.twice_set.add(username)

            del_node.prev.next = del_node.next
            del_node.next.prev = del_node.prev

            del_node.next = None
            del_node.prev = None


    def get_oldest_onetime_visiting_user(self) -> str:

        if self.tail.prev is self.dummy:
            return "" # 如果默认设为“”其实不用这里
        return self.tail.prev.key
    
