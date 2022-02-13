// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(s,op,cl,n):
            re=[]
            if op+1<=n:
                re.append([s+"(",op+1,cl])
            if cl+1<=op:
                re.append([s+")",op,cl+1])
            return re
        
        ans=[]   
        re = generate("",0,0,n)
        while len(re)>0:
            s,op,cl = re.pop()
            if op==n and cl==n:                
                ans.append(s)                
            else:                
                re+=(generate(s,op,cl,n))  
                
        return ans        