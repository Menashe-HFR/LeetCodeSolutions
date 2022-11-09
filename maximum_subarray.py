# def max_sub_array(nums):
# 	temp, big = 0, max(nums)

# 	for idx, v in enumerate(nums):
# 		if v > 0:
# 			for c in range(len(nums) -idx):
# 				temp += nums[idx +c]
# 				if temp < 0:
# 					break
# 				if temp > big:
# 					big = temp
# 			temp = 0
# 	return big

# def max_sub_array(nums):
# 	l, r, big = 0, 1 , max(max(nums),sum(nums))
# 	while r < len(nums):
# 		if nums[l] > 0:
# 			if sum(nums[l:r+1]) > big:
# 				big = sum(nums[l:r+1])
# 			elif sum(nums[l:r+1]) < 0 or sum(nums) :
# 				l = r
# 		else:
# 			l += 1
# 		r += 1	
# 	return big		

def max_sub_array(nums):
	big, temp = max(nums), 0

	for n in nums:
		temp += n
		if temp >= 0:
			big = max(big,temp)
		else:
			temp = 0
	return big
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [5,4,-1,7,8]
print (max_sub_array(nums2))
