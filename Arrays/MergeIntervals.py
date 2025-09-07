class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by the start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []

        for interval in intervals:
            # If merged list is empty or no overlap with last interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap exists, so merge with the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged       