def addDictionary(productName,productNum,pDictionary):
    pDictionary[productName]=productNum
    return pDictionary
def searchforProduct(productName,pDictionary):
    return pDictionary.index(productName)
    
def main():
    pDictionary={}
    quit=False
    while not quit:
        productName=input("Enter the product name: ")
        if productName=="":
            quit=True
        else:
            productNum=int(input("Enter the number of product: "))
            print("%s(%d) has been included."%(productName,productNum))
            pDictionary=addDictionary(productName,productNum,pDictionary)
    
    print(pDictionary)
    prompt=input("search for product: ")
    if prompt in pDictionary:
        print("%s(%d)"%(prompt,pDictionary[prompt]))
    else:
        print("No product.")
        
if __name__ == "__main__":
    main()
    
