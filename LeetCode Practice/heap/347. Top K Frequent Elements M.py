from typing import List
from collections import Counter
import heapq
import random # only used by approach 4 (quick select) in the comments below

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # approach1: min heap + Counter
        # we only need to maintain a k size min_heap, if size > k,
        # pop the top (freq, num).

        counter = Counter(nums) # {num:freq}
        min_heap = []

        for num, freq in counter.items():

            heapq.heappush(min_heap, (freq,num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = [num for freq, num in min_heap]

        return res



        '''
        # approach2: max heap + Counter
        # TC: O(n log n)
        # SC: O(how many different numbers in the array) -> worst O(n)

        counter = Counter(nums) 
        max_heap = []

        for num, freq in counter.items():
            heapq.heappush(max_heap, (-freq,num))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])

        return res
        '''


        '''
        # approach3: bucket sort

        freq = Counter(nums)

        # use frequency as bucket
        max_freq = max(cnt for cnt in freq.values())
        buckets = [[] for _ in range(max_freq + 1)]

        for num, cnt in freq.items():

            buckets[cnt].append(num)

        res = []
        for i in range(max_freq, -1, -1):
            
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
                    k -= 1
                    if k == 0:
                        return res

        # time: O(n)
        # space: O(n)
        # only when the scale of freq is not very huge
        # 选heap 因为k已知 额外空间很稳定；追求极致性价比才可以buckets 
        # buckets 空间不稳定 （但也不会超过n）因为依赖于nums中最大freq which is unknown
        # bucket sort 理论上可以做到 O(n)，但需要 O(n) 额外空间，并且依赖“频率范围有限”这个条件；工程上 heap 往往更稳、更通用。
        # 如果是数据流 要用updatable ordered data structure + hash map；或者像redis那样用skip list + hashmap
        # 因为当数据增加的时候 要从heap里面取出这个元素加入再放进去是很耗费的 应该直接要一个可更新的 比如ordered map

        '''


        '''
        # approach 4: quick select
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 第一步：统计每个数字出现的频率
        # count 是一个字典，形如 {数字: 频率}
        count = Counter(nums)
        
        # unique 存的是所有"不重复"的数字（去重后的数组）
        # 我们接下来要对这个数组按"频率"做部分排序
        unique = list(count.keys())
        n = len(unique)

        # ============================================
        # 三路划分（Dutch National Flag 荷兰国旗问题）
        # 目的：把 unique[left:right+1] 这个区间，
        #      按照"频率和pivot频率的大小关系"分成三段：
        #
        #      [ < pivot频率 ] [ == pivot频率 ] [ > pivot频率 ]
        #        left到lt-1        lt到gt          gt+1到right
        #
        # 返回值 (lt, gt) 就是"等于pivot频率"这一段的左右边界
        # ============================================
        def three_way_partition(left, right, pivot_index):
            
            # 记录pivot的频率值，作为比较基准
            pivot_freq = count[unique[pivot_index]]
            
            # 先把pivot换到最右边，方便后续处理
            # （这是一个常见技巧，先把pivot"藏"到边界上）
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 三个指针的含义：
            # lt (less than)：lt指针左边（不含lt）的元素，都严格 < pivot频率
            # gt (greater than)：gt指针右边（不含gt）的元素，都严格 > pivot频率
            # i：当前正在扫描、还没确定归属的元素
            #
            # 初始时，[left, right] 整个区间都还没分类
            # 注意：pivot现在在right位置，先假装它也在"未分类"区域里
            lt = left
            i = left
            gt = right

            # 循环不变量：
            # unique[left : lt]      → 全部 < pivot频率
            # unique[lt : i]         → 全部 == pivot频率
            # unique[i : gt+1]       → 还没检查，未知
            # unique[gt+1 : right+1] → 全部 > pivot频率
            #
            # 当 i > gt 时，说明"未知区域"已经清空，循环结束
            while i <= gt:
                
                current_freq = count[unique[i]]

                if current_freq < pivot_freq:
                    # 当前元素比pivot小 → 应该归到最左边那一段
                    # 把它和lt位置的元素交换，扩大"小于pivot"的区域
                    unique[lt], unique[i] = unique[i], unique[lt]
                    lt += 1
                    i += 1  # i和lt都往前走一步，因为这个位置已经确定归属了

                elif current_freq > pivot_freq:
                    # 当前元素比pivot大 → 应该归到最右边那一段
                    # 把它和gt位置的元素交换，缩小"未知区域"的右边界
                    unique[gt], unique[i] = unique[i], unique[gt]
                    gt -= 1
                    # 注意：这里i不能加1！
                    # 因为从gt位置换过来的元素，我们还没检查过它的值，
                    # 需要在下一轮循环里重新判断这个新换过来的元素

                else:
                    # current_freq == pivot_freq
                    # 当前元素和pivot频率相等 → 已经在正确的中间位置
                    # 不需要交换，只需要把i往前移动，去看下一个元素
                    i += 1

            # 循环结束后：
            # [left, lt-1]  → < pivot频率
            # [lt, gt]      → == pivot频率（这里面也包含了原来的pivot自己）
            # [gt+1, right] → > pivot频率
            return lt, gt

        # ============================================
        # Quickselect主逻辑
        # 目标：找到"频率第k大"的元素应该在的位置
        # 
        # 等价于：把 unique 数组按频率从小到大排序后，
        #        第 (n-k) 个位置（0-indexed）就是我们要的分界点
        # 因为"频率第k大"＝"升序排列中倒数第k个"＝"正数第(n-k)个"
        # ============================================
        def quickselect(left, right, k_smallest):
            
            # 递归终止条件：区间只剩0或1个元素，不需要再划分
            if left >= right:
                return

            # 随机选一个pivot的下标（而不是固定选第一个或最后一个）
            # 这样做是为了避免"输入本身有序"时退化成O(n^2)的最坏情况
            # 随机化能保证期望时间复杂度是 O(n)
            pivot_index = random.randint(left, right)
            
            # 做一次三路划分，得到"等于pivot频率"这一段的边界 [lt, gt]
            lt, gt = three_way_partition(left, right, pivot_index)

            if lt <= k_smallest <= gt:
                # 我们要找的第k_smallest小的位置，正好落在"等于pivot"这一段里
                # 说明已经找到了，不需要再递归，直接结束
                return
            elif k_smallest < lt:
                # 目标位置在"小于pivot"那一段的左边，只需要递归处理左边区间
                # 右边（>= pivot的部分）已经不需要再管了，直接丢弃
                quickselect(left, lt - 1, k_smallest)
            else:
                # 目标位置在"大于pivot"那一段的右边，只需要递归处理右边区间
                # 左边（<= pivot的部分）已经不需要再管了，直接丢弃
                quickselect(gt + 1, right, k_smallest)

        # 调用quickselect，目标是让unique数组在"第(n-k)个位置"处
        # 完成"局部排序"：使得这个位置左边的都是频率更小的，右边都是频率更大/相等的
        quickselect(0, n - 1, n - k)

        # 划分完成后，unique数组的后k个元素（下标n-k到n-1）
        # 就是频率最高的k个数字（顺序不一定完全有序，但这k个一定是频率最高的）
        return unique[n - k:]


        # TC: 平均 O(n)，最坏 O(n^2)（但用随机pivot后最坏情况概率极低）
        # SC: O(n) 主要是count字典和unique数组的开销
        
        
        
        '''