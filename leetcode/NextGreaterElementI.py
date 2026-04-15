class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        map = dict()
        for i in range(len(nums2)):
            for j in range(i, len(nums2)):
                if nums2[j] > nums2[i]:
                    map[nums2[i]] = nums2[j]
                    break
            if nums2[i] not in map:
                map[nums2[i]] = -1

        for num in nums1:
            ans.append(map[num])
        
        return ans