#교수님 서버가 다운돼서 pdf 파일을 다운받지 못하였습니다. 지금 올렸습니다.
basketList={}
while True:
    name=input("상품명? ")
    if(name=="quit"):
        break
    num=input("수량은? ")

    basketList[name]=num
print("현재 장바구니: ", basketList)
