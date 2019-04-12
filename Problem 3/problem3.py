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

def main():
    n = int(input("Masukkan nilai n :"))
    bil_prima = []
    faktor_prima =[]
    akar_n = math.ceil(math.sqrt(n))
    faktor_N = division(n)
    print(faktor_N)
    length_faktor = len(faktor_N)
    for i in range(2,length_faktor):
        is_prima=True
        j=2
        while(is_prima and j<faktor_N[i]):
            if(faktor_N[i]%j==0):
                is_prima=False
            j+=1
        if(is_prima):
            faktor_prima.append(faktor_N[i]) 
    length_prima = len(faktor_prima)
    print(faktor_prima)
    print(faktor_prima[length_prima-1])

if __name__ == "__main__":
    main()    