from typing import List
from collections import deque
# import math




class Solution:
            def letterCombinations(self, digits: str) -> List[str]:
                if not digits: return []
                phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
                queue = ['']  # 初始化队列
                for digit in digits:
                    for _ in range(len(queue)):
                        tmp = queue.pop(0)
                        for letter in phone[ord(digit) - 50]:  # 这里我们不使用 int() 转换字符串，使用ASCII码
                            queue.append(tmp + letter)
                return queue



print(Solution().letterCombinations("234"))