class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            # Partition nums1
            partition1 = (left + right) // 2

            # Partition nums2
            partition2 = (m + n + 1) // 2 - partition1

            # Values immediately around the partitions
            maxLeft1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float("inf") if partition1 == m else nums1[partition1]

            maxLeft2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float("inf") if partition2 == n else nums2[partition2]

            # Correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                # Total length is odd
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))

                # Total length is even
                return (max(maxLeft1, maxLeft2) +
                        min(minRight1, minRight2)) / 2.0

            # Partition1 is too far right
            elif maxLeft1 > minRight2:
                right = partition1 - 1

            # Partition1 is too far left
            else:
                left = partition1 + 1