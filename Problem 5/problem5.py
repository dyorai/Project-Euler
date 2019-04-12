#problem 5
import math

def checkPrima(N):
    is_prima=True
    j=2
    while(is_prima and j<N):
        if(N%j==0):
            is_prima = False
            return is_prima
        j+=1
    return is_prima

def searchPrima(N):
    f_prima = []
    for i in range (2,N+1):
        if(checkPrima(i)):
            f_prima.append(i)
    return f_prima

def main():
    n = int(input("Masukkan nilai n :"))
    f_prima = searchPrima(n)

    # menentukan faktorisasi prima 
    length = len(f_prima)
    for i in range(length):
        j = 2
        found = True
        while(found):
            if(f_prima[i]**j<=n):
                f_prima.append(f_prima[i])
            else:
                found = False 
            j+=1
    
    result = 1
    length = len(f_prima)

    #mencari nilai fpb
    for i in range(length):
        result *= f_prima[i]
    
    print(result)

if __name__ == "__main__":
    main()    