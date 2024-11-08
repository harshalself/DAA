# Main greedy function to solve the Fractional Knapsack problem
def fractionalKnapsack(W, arr):

    # Sorting items based on the profit-to-weight ratio in descending order
    arr.sort(key=lambda x: x[0] / x[1], reverse=True)

    # Result (value in the knapsack)
    finalvalue = 0.0

    # Looping through all items
    for profit, weight in arr:
        # If adding the entire item does not exceed capacity, add it
        if weight <= W:
            W -= weight
            finalvalue += profit
        # If we can't add the entire item, add fractional part
        else:
            finalvalue += profit * W / weight
            break

    # Returning the final value
    return finalvalue


# Driver Code
if __name__ == "__main__":
    
    W = int(input("Enter the total capacity of the knapsack: "))  # Total capacity of the knapsack
    n = int(input("Enter the number of items: "))  # Number of items

    arr = []
    # Taking input for each item (profit and weight)
    for i in range(n):
        print(f"Enter profit and weight for item {i+1}:")
        profit = int(input("Profit: "))
        weight = int(input("Weight: "))
        arr.append((profit, weight))

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(max_val)
