# Problem 1

def main():
    N = int(input("Input nilai N : "))
    data = []
    result = 0
    for i in range(1,N):
        if((i%3==0) or (i%5==0) or (i% 15==0)):
            data.append(i)
            result = result+i

    dataLength = len(data)
    print("result : ", result)

if __name__ == "__main__":
    main()
