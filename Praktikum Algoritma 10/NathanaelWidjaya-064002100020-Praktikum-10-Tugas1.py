list= [122,5,6,123,2,6]
def bubblesort(list):
    for Number in range(len(list)-1,0,-1):
        for i in range(Number):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
bubblesort(list)
print("data sudah disorting:",list)


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
arr = list
x = int(input("Masukan nomor yang ingin dicacari:"))
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("nomor yang dicari ada pada index", str(result))
else:
    print("nomor yang dicari tidak ada di list:",list)
