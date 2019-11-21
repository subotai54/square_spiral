class Square():
    def __init__(self,num=3):
            self.d=num
            self.arr= [[0 for a in range(self.d)] for b in range(self.d)]
            self.x=0
            self.y=0
            self.visited=[]
            self.point=1
            
    def solve(self):
        
        while self.point<self.d*self.d+1:
            functions=[self.right,self.down,self.left,self.up]
            for i in range(4):
                functions[i%4]()
                if self.point>=(self.d*self.d+1):
                    return self.arr

    def right(self):
            while True:

                self.arr[self.x][self.y]=self.point
                self.point+=1
                self.visited.append([self.x,self.y])
                if self.point==self.d*self.d+1:
                    return
                if self.y==self.d-1:
                    self.x+=1
                    break
                if [self.x,self.y+1] in self.visited:
                    self.x+=1
                    break
                else:
                    self.y+=1
                    
    def down(self):
        while True:
            self.arr[self.x][self.y]=self.point
            self.point+=1
            self.visited.append([self.x,self.y])
            if self.point==self.d*self.d+1:
                return self.arr
            if self.x==self.d-1:
                self.y-=1
                break
            if [self.x+1,self.y] in self.visited:
                self.y-=1
                break
            else:
                self.x+=1
                
    def left(self):
        while True:
            self.arr[self.x][self.y]=self.point
            self.point+=1
            self.visited.append([self.x,self.y])
            if self.point==self.d*self.d+1:
                return
            if self.y==0:
                self.x-=1
                break
            if [self.x,self.y-1] in self.visited:
                self.x-=1
                break
            else:
                self.y-=1
                
    def up(self):
        while True:

            self.arr[self.x][self.y]=self.point
            self.point+=1
            self.visited.append([self.x,self.y])
            
            if self.point==self.d*self.d+1:
                return 
            if self.x==0:
                self.y+=1
                break
            if [self.x-1,self.y] in self.visited:
                self.y+=1
                break
            else:
                self.x-=1
    def print(self):
        for z in self.arr:
            for x in z:
                print("{:=2.0f}".format(float(x)), end=" ")
            print()
    
        

            
if __name__=="__main__":
    print("Type in the square dimension:", end="")
    dim=input()
    solution=Square(int(dim))
    solution.solve()
    solution.print()
