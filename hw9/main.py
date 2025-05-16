from Rectangle import *
from Point import *

def main():
    p1=Point(5,5)
    p2=Point(20,10)
    r1 = Rectangle(p1, p2)
    a = r1.getArea()
    p = r1.getPerimeter()
    r1.show()
    print(f'넓이는 {a}, 둘레는 {p}')

if __name__=="__main__":
    main()