#problem 2


def main():
    n = int(input("Input nilai N : "))
    n1 = 1
    n2 = 2

    data = []
    data.append(n2)
    result = 2
    nf = 0

    while (nf<n):
        nf = n1 + n2
        n1 = n2
        n2 = nf
        if(nf<n and nf%2==0):
            data.append(nf)
            result += nf
        nf+=1
    
    print("sum :" , result)

if __name__ == "__main__":
    main()
