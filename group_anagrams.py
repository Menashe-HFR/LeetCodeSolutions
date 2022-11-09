def groupAnagrams(strs):
	temp, res, place = {}, [], 0

	for s in strs:
		if str(sorted(list(s))) not in temp:
			temp[str(sorted(list(s)))] = place
			res.append([s])
			place += 1
		else:
			res[temp[str(sorted(list(s)))]].append(s)
	return res

h = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(h))
