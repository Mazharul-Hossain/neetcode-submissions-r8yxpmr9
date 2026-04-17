class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_deque = collections.deque()
        # Deque is always:
        # decreasing (front → back)

        left = -1
        answer = []
        for right, num in enumerate(nums):

            if mono_deque and nums[mono_deque[0]] <= num:
                while mono_deque and nums[mono_deque[0]] <= num:
                    _ = mono_deque.popleft()
                mono_deque.appendleft(right)
            
            else:
                while mono_deque and nums[mono_deque[-1]] <= num:
                    _ = mono_deque.pop()
                mono_deque.append(right)
            
            while mono_deque[0] <= left:
                _ = mono_deque.popleft()

            if right - left == k:
                answer.append(nums[mono_deque[0]])
                left += 1
            
            # print(right, num, mono_deque)

        return answer