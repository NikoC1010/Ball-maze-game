import random
import pygame
from GLOBAL import *
class Maze:
    LEN=0#
    WID=0#
    def __init__(self,length,wid):
        self.len=length
        self.wid=wid

    def create_maze(self):
        maze=[[0]*self.wid for i in range(self.len)]
        for i in range(self.len):
            maze[i][0]=1
            maze[0][i]=1
            maze[self.len-1][i]=1
            maze[i][self.len-1]=1
        X=list()
        Y=list()
        X.append(2)
        Y.append(2)
        while len(X)>0:
            r=random.randint(0,len(X))%len(X)
            x=X[r]
            y=Y[r]
            count=0
            for i in range(x-1,x+2):
                for k in range(y-1,y+2):
                    if abs(x-i)+abs(y-k)==1 and maze[i][k]>0:
                        count+=1 
            if count<=1:
                maze[x][y]=1
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2):
                        if abs(x-i)+abs(y-j)==1 and maze[i][j]==0:
                            X.append(i)
                            Y.append(j)                 
            del X[r]
            del Y[r]       
        maze[2][1]=1
        for i in range(self.len-3,-1,-1):
            if maze[i][self.len-3]==1:
                maze[i][self.len-2]=1
                break
        for i in range(self.len):
            for j in range(self.wid):
                if maze[i][j]==1:
                    print('  ',end='')
                else:
                    print('国',end='')
            print()
        return maze
    
        #print(map_)
if __name__=='__main__':
    ma=Maze(30,30)
    #ma.create_map()
