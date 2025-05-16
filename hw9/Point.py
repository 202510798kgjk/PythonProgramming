class Point:
    def __init__(self,x=0,y=0):
        self.__x=x;self.__y=y
    def show(self):
        print(f"({self.__x},{self.__y})")
    def set(self,x,y):
        self.__x=x;self.__y=y
    def get(self):
        return (self.__x,self.__y)