class Rectangle:
    def __init__(self, lt, rb):
        self.__lt=lt; self.__rb=rb
    def show(self):
        print("좌측 상단 꼭지점이 ",self.__lt.get(),"이고 우측 하단 꼭지점이 ",self.__rb.get(),"인 사각형입니다.",sep="")
    def getWidth(self):
        return abs(self.__lt.get()[0]-self.__rb.get()[0])
    def getHeight(self):
        return abs(self.__lt.get()[1]-self.__rb.get()[1])

    def getArea(self):
        return self.getWidth()*self.getHeight()
    def getPerimeter(self):
        return 2*(self.getWidth()+self.getHeight())