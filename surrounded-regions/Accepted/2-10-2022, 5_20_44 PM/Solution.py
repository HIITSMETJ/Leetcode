// https://leetcode.com/problems/surrounded-regions

import queue
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        o_crds=[]  
        m=len(board)
        n=len(board[0])
        for i in range(m):
            if board[i][0]=='O':
                o_crds.append([i,0])
                
            if board[i][n-1]=='O':
                o_crds.append([i,n-1])
        for j in range(n):
            if board[0][j]=='O':
                o_crds.append([0,j])
            if board[m-1][j]=='O':
                o_crds.append([m-1,j])
        root=o_crds        
        for o_crd in root:      
            q = queue.Queue()
            q.put(o_crd)
            while q.qsize()>0:
                [i,j] = q.get()
                if i>0 and board[i-1][j]=='O' and ([i-1,j] not in o_crds):
                    q.put([i-1,j]) 
                    o_crds.append([i-1,j])
                if i<m-1 and board[i+1][j]=='O' and ([i+1,j] not in o_crds):
                    q.put([i+1,j]) 
                    o_crds.append([i+1,j])
                if j>0 and board[i][j-1]=='O' and ([i,j-1] not in o_crds):
                    q.put([i,j-1]) 
                    o_crds.append([i,j-1])
                if j<n-1 and board[i][j+1]=='O' and ([i,j+1] not in o_crds):
                    q.put([i,j+1]) 
                    o_crds.append([i,j+1])
        for i in range(m):
            for j in range(n):
                if [i,j] in o_crds:
                    board[i][j]='O'
                else:
                    board[i][j]='X'

                