arr=list(map(int,input().split()))
def trappedWater(arr):
	left=0       #made pointer to start from the left end
	right=len(arr)-1       #made pointer to start from the right end
	left_max=0              #for tracking the max height to the left
	right_max=0	#for tracking the max height to the right
	water=0	#to store the trapped water
	while left<right:
		if arr[left]<arr[right]:
			if arr[left]>=left_max:
				left_max=arr[left]   #updating left max if current is higher
			else:
				water+=left_max-arr[left]
			left+=1
		else:
			if arr[right]>=right_max:       #updating right max if current is higher
				right_max=arr[right]
			else:
				water+=right_max-arr[right]
			right-=1
	return water
print("trapped water",trappedWater(arr))    #calling the function and to print the result





#For using the analog data

import numpy as np
def generate_heights():
	x=np.linspace(-6,5,500)
	f=lambda x: 3+np.sin(x)+0.5*np.cos(2*x)
	y=f(x)
	y_normalized=y-np.min(y)
	return y_normalized.tolist()

def trappedWater(arr):
	left=0       #made pointer to start from the left end
	right=len(arr)-1       #made pointer to start from the right end
	left_max=0              #for tracking the max height to the left
	right_max=0	#for tracking the max height to the right
	water=0	#to store the trapped water
	while left<right:
		if arr[left]<arr[right]:
			if arr[left]>=left_max:
				left_max=arr[left]   #updating left max if current is higher
			else:
				water+=left_max-arr[left]
			left+=1
		else:
			if arr[right]>=right_max:       #updating right max if current is higher
				right_max=arr[right]
			else:
				water+=right_max-arr[right]
			right-=1
	return water
arr=generate_heights()
print("trapped water",trappedWater(arr)) #calling the function and to print the result
