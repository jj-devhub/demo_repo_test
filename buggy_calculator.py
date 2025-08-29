class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        # Bug fixed: store operation in history
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def divide(self, a, b):
        # Bug fixed: check for division by zero
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        # Bug fixed: return copy of history to prevent external modification
        return self.history.copy()

calc = Calculator()
print(calc.add(5, 3))
print(calc.divide(10, 2))
try:
    print(calc.divide(10, 0))  # Will handle gracefully now
except ValueError as e:
    print(f"Error: {e}")
    
history = calc.get_history()
history.clear()  # Won't affect calculator history anymore
print(f"Calculator history still intact: {calc.get_history()}")
