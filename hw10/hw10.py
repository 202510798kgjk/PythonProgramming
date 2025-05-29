from os.path import exists as xfile
from os.path import isdir as xdir
from os.path import getsize
from os import mkdir
import numpy as np

def print_info(score_list,slen):
    
    print("[점수 출력]")
    print("개인 점수: ",end="")
    for j in range(slen):
        print(score_list[j],end=" ")
    print()
    print("평균: ",end="")
    average=0
    for j in range(slen):
        average+=score_list[j]/slen
    print(average)

def main():
    if not xdir("bin"):
        os.mkdir("bin")

    if not xfile("bin/score.bin"):
        print("[점수 입력]")
        quit=False; i=0
        score_list=[]
        while not quit:
            
            with open("bin/score.bin","ab") as file:
                num=int(input(f"#{i+1}? "))
                if num==-1:
                    quit=True
                else:
                    score_list.append(num)
                    b=num.to_bytes(4, byteorder="little",signed=True)
                    print(b)
                    print(score_list)
                    file.write(b)
                    i+=1

        print()
        print_info(score_list,len(score_list))
    else:
        with open("bin/score.bin","rb") as file:
            print("[파일 읽기]")
            score_bytes=bytes(file.read())
            score_list=[]
            ssize=getsize("bin/score.bin")//4
            for i in range(ssize):
                score_list.append(int.from_bytes(score_bytes[i*4:4*(i+1)],"little"))
                
            print_info(score_list,ssize)

if __name__=="__main__":
    main()
