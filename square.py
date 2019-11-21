class Square():
    def __init__(self,num=3):
            self.diameter=num
            self.Sq= [[0 for a in range(self.diameter)] for b in range(self.diameter)] #creates an emptyPosition square with the diameter as sides
            self.xPosition=0
            self.yPosition=0
            self.visited=[]
            self.nextInt=1 #this is the next int that will be placed in the square
            
    def solve(self):
        while self.nextInt<self.diameter*self.diameter+1:
            functions=[self.moveRight,self.moveDown,self.moveLeft,self.moveUp]
            for i in range(4):
                functions[i%4]()
                if self.nextInt>=(self.diameter*self.diameter+1):
                    return self.Sq

    def moveRight(self):
        while True:
            self.Sq[self.xPosition][self.yPosition]=self.nextInt
            self.nextInt+=1
            self.visited.append([self.xPosition,self.yPosition])
            if self.nextInt==self.diameter*self.diameter+1:
                return
            if self.yPosition==self.diameter-1:
                self.xPosition+=1
                break
            if [self.xPosition,self.yPosition+1] in self.visited:
                self.xPosition+=1
                break
            else:
                self.yPosition+=1
                    
    def moveDown(self):
        while True:
            self.Sq[self.xPosition][self.yPosition]=self.nextInt
            self.nextInt+=1
            self.visited.append([self.xPosition,self.yPosition])
            if self.nextInt==self.diameter*self.diameter+1:
                return self.Sq
            if self.xPosition==self.diameter-1:
                self.yPosition-=1
                break
            if [self.xPosition+1,self.yPosition] in self.visited:
                self.yPosition-=1
                break
            else:
                self.xPosition+=1
                
    def moveLeft(self):
        while True:
            self.Sq[self.xPosition][self.yPosition]=self.nextInt
            self.nextInt+=1
            self.visited.append([self.xPosition,self.yPosition])
            if self.nextInt==self.diameter*self.diameter+1:
                return
            if self.yPosition==0:
                self.xPosition-=1
                break
            if [self.xPosition,self.yPosition-1] in self.visited:
                self.xPosition-=1
                break
            else:
                self.yPosition-=1
                
    def moveUp(self):
        while True:
            self.Sq[self.xPosition][self.yPosition]=self.nextInt
            self.nextInt+=1
            self.visited.append([self.xPosition,self.yPosition])
            
            if self.nextInt==self.diameter*self.diameter+1:
                return 
            if self.xPosition==0:
                self.yPosition+=1
                break
            if [self.xPosition-1,self.yPosition] in self.visited:
                self.yPosition+=1
                break
            else:
                self.xPosition-=1

    def print(self):
        for z in self.Sq:
            for x in z:
                print("{:=2.0f}".format(float(x)), end=" ")
            print()
    
        

            
if __name__=="__main__":
    print("Type in the square dimension:", end="")
    dim=input()
    solution=Square(int(dim))
    solution.solve()
    solution.print()
