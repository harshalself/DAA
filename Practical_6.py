# A naive recursive implementation of 
# optimal binary search tree problem 

# A recursive function to calculate 
# cost of optimal binary search tree 
def optCost(freq, i, j):
	
	# Base cases 
	if j < i:	 # no elements in this subarray 
		return 0
	if j == i:	 # one element in this subarray 
		return freq[i] 
	
	# Get sum of freq[i], freq[i+1], ... freq[j] 
	fsum = Sum(freq, i, j) 
	
	# Initialize minimum value 
	Min = 999999999999
	
	# One by one consider all elements as 
	# root and recursively find cost of 
	# the BST, compare the cost with min
	# and update min if needed 
	for r in range(i, j + 1):
		cost = (optCost(freq, i, r - 1) + optCost(freq, r + 1, j)) 
		if cost < Min: 
			Min = cost
	
	# Return minimum value 
	return Min + fsum

# The main function that calculates minimum 
# cost of a Binary Search Tree. It mainly 
# uses optCost() to find the optimal cost. 
def optimalSearchTree(keys, freq, n):
	
    # Sorting keys and rearranging freq accordingly
    combined = sorted(zip(keys, freq))  # Sort by keys
    keys[:], freq[:] = zip(*combined)  # Unzip the sorted pairs back to keys and freq
    
    return optCost(freq, 0, n - 1)

# A utility function to get sum of
# array elements freq[i] to freq[j] 
def Sum(freq, i, j):
    return sum(freq[i:j + 1])

# Driver Code
if __name__ == '__main__':
	keys = [10, 12, 20] 
	freq = [34, 8, 50] 
	n = len(keys) 
	print("Cost of Optimal BST is", optimalSearchTree(keys, freq, n))