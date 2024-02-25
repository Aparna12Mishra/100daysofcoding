class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def find_set_leader(disjoint_set, x):
            if disjoint_set[x] == x:
                return x
            disjoint_set[x] = find_set_leader(disjoint_set, disjoint_set[x])
            return disjoint_set[x]

        def union_sets(disjoint_set, set_size, x, y):
            x_leader = find_set_leader(disjoint_set, x)
            y_leader = find_set_leader(disjoint_set, y)
            if x_leader == y_leader:
                return
            if set_size[x_leader] < set_size[y_leader]:
                disjoint_set[x_leader] = y_leader
                set_size[y_leader] += set_size[x_leader]
            else:
                disjoint_set[y_leader] = x_leader
                set_size[x_leader] += set_size[y_leader]

        num_elements = len(nums)
        if num_elements == 1:
            return True

        disjoint_set = [i for i in range(num_elements)]
        set_size = [1] * num_elements
        factor_first_occurrence = {}

        for i, num in enumerate(nums):
            divisor = 2
            while divisor * divisor <= num:
                if num % divisor == 0:
                    if divisor in factor_first_occurrence:
                        union_sets(disjoint_set, set_size, i, factor_first_occurrence[divisor])
                    else:
                        factor_first_occurrence[divisor] = i
                    while num % divisor == 0:
                        num //= divisor
                divisor += 1
            if num > 1:
                if num in factor_first_occurrence:
                    union_sets(disjoint_set, set_size, i, factor_first_occurrence[num])
                else:
                    factor_first_occurrence[num] = i

        return set_size[find_set_leader(disjoint_set, 0)] == num_elements