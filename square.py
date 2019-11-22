import argparse


parser = argparse.ArgumentParser()
class Square():
    def __init__(self,num=3):
        self.diameter=int(num)
        self.Sq= [[0 for a in range(self.diameter)] for b in range(self.diameter)] #creates an emptyPosition square with the diameter as sides
        self.xPosition=0
        self.yPosition=0
        self.visited=[]
        self.nextInt=1 #this is the next int that will be placed in the square
        self.maxPoint=self.diameter*self.diameter+1
            
    def solve(self):
        while self.nextInt<self.maxPoint:
            functions=[self.moveRight,self.moveDown,self.moveLeft,self.moveUp]
            for i in functions:
                i()
                if self.nextInt>=(self.maxPoint):
                    return self.Sq

    def moveRight(self):
        while True:
            self.Sq[self.xPosition][self.yPosition]=self.nextInt
            self.nextInt+=1
            self.visited.append([self.xPosition,self.yPosition])
            if self.nextInt==self.maxPoint:
                return
            if self.yPosition==self.diameter-1:
                self.xPosition+=1
                return
            if [self.xPosition,self.yPosition+1] in self.visited:
                self.xPosition+=1
                return
            else:
                self.yPosition+=1
                    
    def moveDown(self):
        while True:
            self.Sq[self.xPosition][self.yPosition]=self.nextInt
            self.nextInt+=1
            self.visited.append([self.xPosition,self.yPosition])
            if self.nextInt==self.maxPoint:
                return
            if self.xPosition==self.diameter-1:
                self.yPosition-=1
                return
            if [self.xPosition+1,self.yPosition] in self.visited:
                self.yPosition-=1
                return
            else:
                self.xPosition+=1

    def moveLeft(self):
        while True:
            self.Sq[self.xPosition][self.yPosition]=self.nextInt
            self.nextInt+=1
            self.visited.append([self.xPosition,self.yPosition])
            if self.nextInt==self.maxPoint:
                return
            if self.yPosition==0:
                self.xPosition-=1
                return
            if [self.xPosition,self.yPosition-1] in self.visited:
                self.xPosition-=1
                return
            else:
                self.yPosition-=1
                
    def moveUp(self):
        while True:
            self.Sq[self.xPosition][self.yPosition]=self.nextInt
            self.nextInt+=1
            self.visited.append([self.xPosition,self.yPosition])
            
            if self.nextInt==self.maxPoint:
                return 
            if self.xPosition==0:
                self.yPosition+=1
                return
            if [self.xPosition-1,self.yPosition] in self.visited:
                self.yPosition+=1
                return
            else:
                self.xPosition-=1

    def print(self):
        for z in self.Sq:
            for x in z:
                print("{num:0{width}}".format(num=int(x),width=len(str(self.maxPoint))), end=" ") #pads numbers to give a square appearance
            print()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dimension", help="Input the dimension you want for your square")
    args = parser.parse_args()
    try:
        solution = Square(args.dimension)
        solution.solve()
        solution.print()
    except (TypeError, IndexError, ValueError):
        print("Error, input incorrect. Please enter a non-negative single integer")
