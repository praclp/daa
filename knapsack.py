class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):
   
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True) 
    finalvalue = 0.0
    
    for item in arr:
        if item.weight <= W:  
            W -= item.weight
            finalvalue += item.profit
        else:  
            finalvalue += item.profit * W / item.weight
            break
            
    return finalvalue

if __name__ == "__main__":
   
    W = float(input("Enter the capacity of the knapsack: "))
    
    # Get user input for the number of items
    n = int(input("Enter the number of items: "))
    
    arr = []
    for i in range(n):
        # Get profit and weight for each item
        profit = float(input(f"Enter profit for item {i + 1}: "))
        weight = float(input(f"Enter weight for item {i + 1}: "))
        arr.append(Item(profit, weight))
    
   
    max_val = fractionalKnapsack(W, arr)
    print(f"The maximum value in the knapsack is: {max_val}")
