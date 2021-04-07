def addUp(nums, k):
	for i in range(len(nums)):
		for j in range(len(nums)):
			if nums[i] + nums[j] == k and i != j:
				return True
	return False
