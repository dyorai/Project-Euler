#problem 3
import math

     
def main():
    n = int(input("Masukkan nilai n :"))
    f_prima = []
    
    for i in range (2,n+1):
        is_prima=True
        j=2
        while(is_prima and j<i):
            if(i%j==0):
                is_prima = False
            j+=1
        if(is_prima):
            f_prima.append(i)
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

    for i in range(length):
        result *= f_prima[i]
    print(f_prima)
    print(result)

if __name__ == "__main__":
    main()    