import numpy as np

def cross_entropy(y_true, y_pred):
    """
    Compute the cross-entropy loss between true labels and predicted probabilities.

    Parameters:
    y_true (array-like): True labels (one-hot encoded or binary).
    y_pred (array-like): Predicted probabilities.

    Returns:
    float: Cross-entropy loss.
    """
    # Ensure predictions are clipped to avoid log(0)
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
    # Compute cross-entropy
    loss = -np.sum(y_true * np.log(y_pred)) / y_true.shape[0]
    return 
    return loss

def entropy(p):
    if p==0 or p==1:
        return 0
    return - (p * np.log(p) + (1 - p) * np.log(1 - p)) / np.log(2)

def call_entropy():
    while True:
        print("Press x to exit.")
        p = input("Please enter a probability between 0 and 1:")
        if p=='x': return
        try:
            p = float(p)
            if 0 <= p <= 1:
                # valid
                result = entropy(p)
                print(f"The entropy for p = {p} is: {result}")
                continue
            else:
                print("Invalid input. Please enter a probability between 0 and 1.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        # Calculate entropy

    return

def partition_entropy(ls):
    
    result = 0
    
    for item in ls:
        result += item[0] * entropy(item[1])
    
    return result

def call_partition_entropy():
    while True:
        print("Press x to exit.")
        ip = input("Please input the number of partitions: ")
        if ip=='x': return
        n = int(ip)
        ls = []
        for i in range(n):
            i0 = float(input(f"Partition {i+1} size / total_item: "))
            i1 = float(input(f'Partition {i+1} probability: '))
            ls.append([i0,i1])
        result = partition_entropy(ls)
        print(f"Entropy of this partition is: {result}.")

if __name__ == "__main__":

    while True:
        print("1. Entropy Loss")
        print("2. Partition Entropy")
        print("x. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            call_entropy()
        elif choice == '2':
            call_partition_entropy()
        elif choice.lower() == 'x':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")