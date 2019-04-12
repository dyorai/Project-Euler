#problem 3
import math

def division(N):
    div = []
    M = int(math.sqrt(N))
    for i in range(1,M+1):
        if(N%i==0):
            div.append(i)
    #if(N!=1):
    div.append(N)
    return div

def checkPrima(N):
    is_prima=True
    j=2
    while(is_prima and j<N):
        if(N%j==0):
            is_prima = False
            return is_prima
        j+=1
    return is_prima

def main():
    n = int(input("Input nilai n :"))
    faktor_prima =[]
    faktor_N = division(n)
    
    length_faktor = len(faktor_N)
    for i in range(2,length_faktor):
        if(checkPrima(faktor_N[i])):
            faktor_prima.append(faktor_N[i]) 
    length_prima = len(faktor_prima)
    if(length_prima>0):
        print("largest prime factor : ", faktor_prima[length_prima-1])
    else :
        print(n, " didn't had prime factor")

if __name__ == "__main__":
    main()    