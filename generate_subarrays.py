def generate_subarrays(array):
	res = []
	big = small = len(array)-1
	cur = []
	for i in range(len(array)):
		j = i
		cur = []
		while j < array[len(array)-1]:
			cur.append(array[j])
			res.append(cur.copy())
			j+=1

			print(res)

generate_subarrays([1,2,3,4])

