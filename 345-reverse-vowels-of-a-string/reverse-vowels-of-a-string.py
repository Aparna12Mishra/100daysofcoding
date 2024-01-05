class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        s=list(s)
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                l.append(s[i])
                s[i]="*"
        l=l[::-1]
        start=0
        for i in range(len(s)):
            if s[i]=="*" and start<len(l):
                s[i]=l[start]
                start+=1
        str1=""
        for i in s:
            str1+=i
        return str1

