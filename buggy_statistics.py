def calculate_statistics(data):
    # Bug fixed: handle empty lists
    if not data:
        return {
            'mean': None,
            'median': None,
            'variance': None,
            'std_dev': None,
            'count': 0
        }
    
    total = sum(data)
    count = len(data)
    mean = total / count
    
    # Bug fixed: reuse sorted data instead of sorting again
    sorted_data = sorted(data)
    if count % 2 == 0:
        median = (sorted_data[count//2 - 1] + sorted_data[count//2]) / 2
    else:
        median = sorted_data[count//2]
    
    # Bug fixed: use sample variance (n-1) for better estimation
    if count > 1:
        variance = sum((x - mean) ** 2 for x in data) / (count - 1)
    else:
        variance = 0
    
    return {
        'mean': mean,
        'median': median,
        'variance': variance,
        'std_dev': variance ** 0.5,
        'count': count
    }

def find_outliers(data, threshold=2):
    # Bug fixed: handle edge cases properly
    if not data or len(data) < 2:
        return []
    
    stats = calculate_statistics(data)
    if stats['std_dev'] == 0:  # All values are the same
        return []
    
    outliers = []
    for value in data:
        # Bug fixed: using sample standard deviation
        z_score = abs(value - stats['mean']) / stats['std_dev']
        if z_score > threshold:
            outliers.append(value)
    
    return outliers

def moving_average(data, window_size):
    # Bug fixed: handle invalid window sizes
    if not data:
        return []
    
    if window_size <= 0:
        raise ValueError("Window size must be positive")
    
    if window_size > len(data):
        raise ValueError(f"Window size ({window_size}) cannot be larger than data length ({len(data)})")
    
    averages = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        avg = sum(window) / len(window)
        averages.append(avg)
    return averages

# Test with properly handled edge cases
empty_data = []
single_data = [5]
normal_data = [1, 2, 3, 4, 5, 100, 6, 7, 8, 9]

print("Testing with empty data:")
result = calculate_statistics(empty_data)
print(f"Empty data stats: {result}")

print("\nTesting with single data point:")
result = calculate_statistics(single_data)
print(f"Single data stats: {result}")

print("\nTesting outlier detection:")
outliers = find_outliers(normal_data)
print(f"Outliers in {normal_data}: {outliers}")

print("\nTesting moving average with valid window:")
try:
    ma = moving_average(normal_data, 3)
    print(f"Moving average (window=3): {ma}")
except ValueError as e:
    print(f"Moving average error: {e}")

print("\nTesting moving average with invalid window:")
try:
    ma = moving_average(normal_data, 15)  # Window larger than data
    print(f"Moving average: {ma}")
except ValueError as e:
    print(f"Moving average error: {e}")
