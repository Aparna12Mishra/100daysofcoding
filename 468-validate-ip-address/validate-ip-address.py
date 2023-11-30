class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.find(".") != -1:
            queryChunks = queryIP.split(".")
            if len(queryChunks) != 4:
                return "Neither"
            for chunk in queryChunks:
                if not re.match(r"^(\d{1,4})$", chunk):
                    return "Neither"
                if len(chunk) > 3 or len(chunk) == 0:
                    return "Neither"
                if chunk[0] == "0" and len(chunk) > 1:
                    return "Neither"
                if chunk.find("e") != -1:
                    return "Neither"
                if chunk.find("f") != -1:
                    return "Neither"
                if int(chunk) > 255:
                    return "Neither"
            return "IPv4"

        if queryIP.find(":") != -1:
            queryChunks = queryIP.split(":")
            if len(queryChunks) != 8:
                return "Neither"
            for chunk in queryChunks:
                if not re.match(r"^([0-9a-fA-F]{1,4})$", chunk):
                    return "Neither"
            return "IPv6"

        return "Neither"