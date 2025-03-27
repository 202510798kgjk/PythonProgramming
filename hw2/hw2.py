def get_integer():
    return int(input("금액의 수는?: "))

def exchange(money):
    q500=money//500
    money%=500
    print("500원 동전의 개수:", q500)

    q100=money//100
    money%=100
    print("500원 동전의 개수:", q100)

    q50=money//50
    money%=50
    print("500원 동전의 개수:", q50)

    q10=money//10
    money%=10
    print("500원 동전의 개수:", q10)

exchange(get_integer())