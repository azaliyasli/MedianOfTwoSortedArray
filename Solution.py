class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedList = nums1 + nums2
        mergedList.sort()
        i = len(mergedList) // 2
        if len(mergedList) % 2 == 0:
            med = (mergedList[i-1] + mergedList[i]) / 2
        else:
            med = mergedList[i]
        return med
