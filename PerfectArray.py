n=int(input("Enter a number of elements"))
arr=list(map(int,input("Enter Element:").split()))

if arr == arr[::-1]:
    print("Perfect Array")
else:
    print("Not Perfect Array")    