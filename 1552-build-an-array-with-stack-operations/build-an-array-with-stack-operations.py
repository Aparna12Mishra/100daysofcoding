class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stream = 1
        ops = []
        for num in target:
            while stream < num:
                ops.extend(["Push", "Pop"])
                stream += 1
            ops.append("Push")
            stream += 1
        return ops       