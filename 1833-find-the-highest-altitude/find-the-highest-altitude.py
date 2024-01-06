class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_point = 0
        prev_altitude = 0
        for i in gain:
            prev_altitude += i
            highest_point = max(highest_point, prev_altitude)

        return highest_point