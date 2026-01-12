def merge(arr,mid,l,r):
	m=int(mid-l+1)
	n=int(r-mid)
	L=[]
	R=[]
	for i in range (m):
		L.append(arr[l+i])
	for j in range(n):
		R.append(arr[mid+1+j])
	a=0
	b=0
	k=l
	while a<m and b<n:
		if (L[a]<R[b]):
			arr[k]=L[a]
			a+=1
		else:
			arr[k]=R[b]
			b+=1
		k+=1
	while a<m:
		arr[k]=L[a]
		k+=1
		a+=1
	while b<n:
		arr[k]=R[b]
		k+=1
		b+=1



def mergesort(arr,l,r):
	if(l<r):
		mid=int((l+r)/2)
		mergesort(arr,l,mid)
		mergesort(arr,mid+1,r)
		merge(arr,mid,l,r)
arr=[]
n=int(input("Enter number of elements: "))
sum=0
for i in range (n):
	element = int(input(f"Enter element {i+1}: "))
	arr.append(element)
	sum+=element
mergesort(arr,0,n-1)
print(f"Maximum element: {arr[n-1]}")
print(f"Minimum element: {arr[0]}")
mean=sum/n
print(f"Mean: {mean}")
mid_idx=n//2
print(f"Median: {arr[mid_idx]}")

