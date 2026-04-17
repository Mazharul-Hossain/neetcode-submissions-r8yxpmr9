class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_deque = collections.deque()
        # Deque is always:
        # decreasing (front → back)

        left = -1
        answer = []
        for right, num in enumerate(nums): # O(N)

            # if mono_deque and nums[mono_deque[0]] <= num:
            #     while mono_deque and nums[mono_deque[0]] <= num:
            #         _ = mono_deque.popleft() # O(1)
            #     mono_deque.appendleft(right) # O(1)
            
            # else:
            # pop smaller useless elements from back
            while mono_deque and nums[mono_deque[-1]] <= num:
                # Back: maintain decreasing order (remove useless elements)
                _ = mono_deque.pop() # O(1)
            # append new candidate index
            mono_deque.append(right) # O(1)
            
            # Remove expired elements from front if out of window
            while mono_deque and mono_deque[0] <= left:
                _ = mono_deque.popleft() # O(1)

            if right >= k - 1:
                answer.append(nums[mono_deque[0]]) # O(1)
                left += 1
            
            # The deque stores a compressed representation of the windows `future maxima`
            # Not all elements - only relevant ones
            # print(right, num, mono_deque)
            # Time complexity: O(N) as deque add and remove opperations are O(1)
            #                  and we do these only once 1 add and 1 remove
            # Space complexity: O(N)

        return answer