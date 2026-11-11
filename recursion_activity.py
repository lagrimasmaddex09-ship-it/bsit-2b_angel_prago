def sum_array(arr):
    # Base case: empty array
    if len(arr) == 0:
        return 0
    # Recursive step: first element + sum of the rest
    return arr[0] + sum_array(arr[1:])

# Tests
print("--- Sum Tests ---")
print(sum_array([]))                   # Expected: 0
print(sum_array([5]))                  # Expected: 5
print(sum_array([1, 2, 3, 4, 5]))      # Expected: 15
print(sum_array([10, -5, 3, -2]))      # Expected: 6

def find_max(arr):
    # Input rule documented: requires a nonempty array
    if len(arr) == 0:
        raise ValueError("Array must contain at least one number.")
    
    # Base case: only one element left
    if len(arr) == 1:
        return arr[0]
    
    # Recursive step: compare current element with max of the rest
    max_of_rest = find_max(arr[1:])
    if arr[0] > max_of_rest:
        return arr[0]
    else:
        return max_of_rest

# Tests
print("\n--- Find Max Tests ---")
print(find_max([42]))                   # Expected: 42 (one-number array)
print(find_max([10, 5, 2, 1]))          # Expected: 10 (largest at beginning)
print(find_max([1, 5, 2, 10]))          # Expected: 10 (largest at end)
print(find_max([-5, -2, -10, -8]))      # Expected: -2 (all negative numbers)
try:
    find_max([])
except ValueError as e:
    print(f"Empty array test: {e}")

def count_target(arr, target):
    # Base case: no numbers left to examine
    if len(arr) == 0:
        return 0
    
    # Check if current number matches the target
    if arr[0] == target:
        match = 1
    else:
        match = 0
        
    # Recursive step: current match + count in the rest of the array
    return match + count_target(arr[1:], target)

# Tests
print("\n--- Count Target Tests ---")
print(count_target([], 5))                      # Expected: 0 (empty array)
print(count_target([1, 2, 3, 2, 4, 2], 2))      # Expected: 3 (appears several times)
print(count_target([1, 2, 3, 4, 5], 9))         # Expected: 0 (does not appear)