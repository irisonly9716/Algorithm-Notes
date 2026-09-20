'''
实现查询一个string出现过几次
以及这个string是否可以作为新密码

作为新密码的条件：
旧密码不可以是新密码的prefix
新密码不可以是旧密码的prefix

'''


class Node:

    def __init__(self):

        self.children = {}
        self.word_count = 0

class Trie:

    def __init__(self):

        self.root = Node()

    def count_word(self, word:str) -> int:
 
        curr = self.root

        for char in word:

            if char not in curr.children:
                return 0
            
            curr = curr.children[char]

        return curr.word_count

    # for checking if a password is valid
    # a valid password is not a prefix of existing word
    # existing word cannot be prefix of new password
    def check_password(self, password:str) -> bool:

        curr = self.root

        for char in password:

            # if old password is the prefix of new one
            if curr.word_count > 0:
                return False
            
            if char not in curr.children:
                return True
            
            curr = curr.children[char]

        # same password exists
        if curr.word_count > 0:
            return False
    
        # new password is prefix of old ones
        if curr.children:
            return False
        
        return True


    def insert_word(self, word:str) -> None:

        curr = self.root

        for char in word:

            if char not in curr.children:
                curr.children[char] = Node()

            curr = curr.children[char]

        curr.word_count += 1


    def insert_password(self, password:str) -> bool:

        if not self.check_password(password):
            return False
        
        self.insert_word(password)

        return True











'''
class Node:

    def __init__(self):

        self.children = {} # {char:node}
        self.word_count = 0

class Trie:


    def __init__(self):

        self.root = Node()

    def insert(self, word:str) -> None:

        curr = self.root

        for char in word:

            if char not in curr.children:

                curr.children[char] = Node()

            curr = curr.children[char]
        
        curr.word_count += 1

    def check_password(self, password:str) -> bool:
        
        curr = self.root

        for char in password:

            # 如果旧密码是新密码的前缀 不能作为密码 (⭐这个和下面不能换顺序 因为先要检查是否旧密码是prefix 才能往下判断)
            # 旧密码不能是新密码的前缀 如果旧密码是abc 新密码是abcd 那在abc的时候就返回false了
            if curr.word_count > 0:
                return False
            
            # 如果已经到了没有当前节点 返回True因为新密码不会是旧密码的prefix了
            if char not in curr.children:
                return True
            
            curr = curr.children[char]


        # 如果相同密码？ 这里要再查一次 因为下到最后一个char的node还没有检查查过word_count (最后已经跳出循环了因为)
        if curr.word_count > 0:
            return False
        
        # 新密码是旧密码的 prefix
        if curr.children:
            return False
        
        return True
    
    def insert_password(self, password:str) -> bool:

        if not self.check_password(password):
            return False
        
        self.insert(password)

        return True



'''



































'''
from collections import defaultdict


# hashset 也可以做 但是查询的时间复杂度会比较高
# 适合密码不多的情况 如果密码量很大 还是要用Trie树
class PasswordManager:

    def __init__(self):
        self.passwords = set()
        self.count = defaultdict(int)

    def insert_word(self, word: str) -> None:
        self.passwords.add(word)
        self.count[word] += 1

    def exact_word(self, word: str) -> int:
        return self.count.get(word, 0)

    def password_check(self, password: str) -> bool:

        # 1. 旧密码是新密码 prefix
        for i in range(1, len(password)):
            if password[:i] in self.passwords:
                return False

        # 2. 新密码是旧密码 prefix
        for old in self.passwords:
            if old.startswith(password):
                return False

        # 3. 相同密码
        if password in self.passwords:
            return False

        return True
'''
    




'''
class Node:

    def __init__(self):
        
        self.children = {} # {char: node}
        self.word_count = 0

class Trie:

    def __init__(self):
        
        self.root = Node()

    def insert_word(self, word) -> None:

        curr = self.root

        for char in word:

            if char not in curr.children:

                curr.children[char] = Node()
            
            curr = curr.children[char]

        curr.word_count += 1 # go down to char node and add the word count


    def exact_word(self, word:str) -> int:

        curr = self.root

        for char in word:

            if char not in curr.children:

                return 0
            
            curr = curr.children[char]

        return curr.word_count


    def Password_check(self, password:str) -> bool:

        curr = self.root

        for char in password:

            # # 旧密码是新密码的 prefix
            if curr.word_count > 0:
                return False
            
            # 走不下去了，说明后面不可能存在“旧密码是新密码前缀”或“新密码是旧密码前缀”
            if char not in curr.children:
                return True

            curr = curr.children[char]

        # 如果当前char下面非空 说明当前密码是旧密码的prefix； 或者如果当前char的word_count > 0 说明完全一致的密码已存在
        if curr.children or curr.word_count > 0:
            return False
        
        return True
    
    # 插入密码的封装 先检查后插入
    def add_password(self, password: str) -> bool:

        if not self.password_check(password):
            return False
        
        self.insert_word(password)

        return True
    

'''




'''

class Node:
    def __init__(self):

        self.children = {}
        self.word_count = 0

class PasswordTrie:

    def __init__(self):

        self.root = Node()

    # exact 查询
    def countWordsEqualTo(self, word: str) -> int:

        curr = self.root

        for char in word:
            if char not in curr.children:
                return 0
            curr = curr.children[char]

        return curr.word_count


    # password check + 插入
    def insert(self, word: str) -> bool:

        curr = self.root

        for char in word:

            # 情况1：已有更短密码是 prefix
            if curr.word_count > 0:
                return False

            if char not in curr.children:
                curr.children[char] = Node()

            curr = curr.children[char]

        # 情况2：新密码是已有更长密码的 prefix
        if curr.children:
            return False

        curr.word_count += 1
        return True
'''

