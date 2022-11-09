def combinationSum(candidates, target):
	res = []

	def dfs(i, cur, total):
		if total == target:
			res.append(cur.copy())
			print(cur, 'perfect')
			return
		if i >= len(candidates) or total > target:
			print(cur, 'null')
			return

		cur.append(candidates[i])
		dfs(i, cur, total + candidates[i])
		cur.pop()
		dfs(i+1, cur, total)
	dfs(0, [], 0)
	return res
print(combinationSum([2], 1))