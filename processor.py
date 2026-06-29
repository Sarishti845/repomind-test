def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    def process(self):
        avg = calculate_average(self.data)
        max_val = find_max(self.data)
        return {"average": avg, "max": max_val}
