PI=3.14

def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(r):
    result=r**2*PI
    return result

r=get_radius("넓이를 구하고자 하는 원의 반지름은? ")
result=get_circle_area(r)
print("반지름 {0}인 원의 넓이 = {1} x {0} x {0} = {2}".format(r, PI, result))
