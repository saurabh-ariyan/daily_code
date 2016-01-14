# Rotate an array of n elements by k steps
#Trying different ways to solve the problem

class Solution:
	# @param nums, a list of int
	# @param k, num of steps
	# returns nothing, modifies the list
	def rotate(self, nums, k):
		k %= len(nums)
		self.reverse(nums, 0, len(nums))
		self.reverse(num, 0, k)
		self.reverse(num, k, len(nums))

	def reverse(self, nums, start, end):
		while start < end:
			num[start], num[end-1] = num[end-1], num[start]
			start +=1
			end  -= 1

from fractions import gcd

class Solution2:
	# @param nums, a list of int
	# @param k, num of steps
	# @return nothing, please modify the num list in-place
	# 

	def rotate(self, nums, k):
		k %= len(nums)
		num_cycles = gcd(len(num), k)
		cycle_len = len(nums) / num_cycles
		for i in xrange(num_cycles):
			self.apply_cycle_permutation(k, i, cycle_len, nums)

	def apply_cycle_permutation(self, k, offset, cycle_len, nums):
		tmp = nums[offset]
		for i in xrange(1, cycle_len):
			nums[(offset + i * k) % len(nums)], tmp = tmp, num[(offset + i*k) % len(nums)]
		nums[offset] = tmp



if __name__ == '__main__':
	nums = [1,2,3,4,5,6]
	Solution().rotate(nums, 3)
	print nums 

