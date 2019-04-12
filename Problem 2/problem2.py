#problem 2


def main():
    n1 = 1
    n2 = 2

    data = []
    data.append(n2)
    result = 2
    nf = 0

    while (nf<4000000):
        nf = n1 + n2
        n1 = n2
        n2 = nf
        if(nf<4000000 and nf%2==0):
            data.append(nf)
            result += nf
        nf+=1
    print(nf)
    
    dataLength = len(data)
    print("angka fibo :")
    for i in range(dataLength):
        print(data[i],end = " ")
    
    print("\nsum :" , result)

    


if __name__ == "__main__":
    main()
