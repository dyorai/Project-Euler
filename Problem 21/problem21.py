#problem 21
import math

def division(N):
    div = []
    M = int(math.ceil((N+1)/2))
    for i in range(1,M+1):
        if(N%i==0):
            div.append(i)
    return div

def sum(arr):
    n_arr = len(arr)
    sum = 0
    for i in range(n_arr):
        sum+=arr[i]
    return sum

def isAmicable(N):
    a_arr = division(N)
    sum_a = sum(a_arr)
    b_arr = division(sum_a)
    sum_b = sum(b_arr)
    if(sum_b==N and N != sum_a):
        return True
    else :
        return False

def checkList(N,list):
    n_list = len(list)
    i = 0
    found = False
    while(not found and i<n_list):
        if(N==list[i]):
            found = True
        i+=1
    return found

def main():
    n = int(input("Input nilai N : "))
    amicable = []
    for i in range(1,n):
        if(checkList(i,amicable)):
            continue
        else:
            if(isAmicable(i)):
                amicable.append(i)

    sum_amicable = sum(amicable)
    print("sum of amicable number under", n, " : " , sum_amicable)

if __name__ == "__main__":
    main()    