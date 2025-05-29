def readSingleDigit(num):
    unicodeVariable=""
    match (num):
        case 0: unicodeVariable="영"
        case 1: unicodeVariable="일"
        case 2: unicodeVariable="이"
        case 3: unicodeVariable="삼"
        case 4: unicodeVariable="사"
        case 5: unicodeVariable="오"
        case 6: unicodeVariable="육"
        case 7: unicodeVariable="칠"
        case 8: unicodeVariable="팔"
        case 9: unicodeVariable="구"
    print(unicodeVariable, end=" ")

def readNumber(resolvingNum):
    readSingleDigit(resolvingNum//100)
    resolvingNum%=100
    readSingleDigit(resolvingNum//10)
    resolvingNum%=10
    readSingleDigit(resolvingNum)

readNumber(int(input("세 자리 수 정수 입력: ")))
