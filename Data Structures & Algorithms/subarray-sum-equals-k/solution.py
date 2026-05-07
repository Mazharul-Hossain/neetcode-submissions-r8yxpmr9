import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = collections.Counter()
        prefixSums[0] = 1

        # index_map = collections.defaultdict(list)
        # # prefix sum 0 exists before array starts
        # index_map[0].append(-1)

        # answer = []        
        result = prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            diff = prefix - k

            result += prefixSums[diff]
            # # all previous positions with prefix = diff
            # for j in index_map[diff]:
            #     print(result, ":", prefix, diff, j, i)
            #     answer.append(nums[j + 1 : i + 1])
        
            # index_map[prefix].append(i)
            prefixSums[prefix] += 1
        
        # print(answer)
        return result