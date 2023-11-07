class Solution:
    def eliminateMaximum(self, dist, speed):
        count = 0
        n = len(dist)

        # Convert distances into time required to reach the city
        for i in range(n):
            if dist[i] % speed[i] != 0:
                dist[i] = (dist[i] // speed[i]) + 1
            else:
                dist[i] //= speed[i]

        # Sort time required to eliminate monsters that reach first
        dist.sort()

        for i in range(n):
            dist[i] -= i  # Minutes away from the city at the ith minute
            if dist[i] <= 0:  # Monster already at the city
                break
            count += 1  # Eliminate the monster

        return count