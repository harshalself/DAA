
def binarysearch(arr,key):
	low=0
	high=len(arr)-1
	while low<=high:
		mid=(low+high)//2
		if arr[mid]==key:
			return mid
		elif key>arr[mid]:
			low=mid+1
		else:
			high=mid-1
	return -1

arr = []
n=int(input("Enter Number of Elements : "))
for i in range(n):
	ele=int(input(f"enter element {i} : "))
	arr.append(ele)

arr.sort()

key=int(input("Enter Key : "))

result = binarysearch(arr,key)

if result!=-1:
	print(f"Element is found as position {result}")
else:
	print("element not found")

	
	