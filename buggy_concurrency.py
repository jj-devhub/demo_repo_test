import threading
import time

class Counter:
    def __init__(self):
        self.value = 0
        # Bug fixed: add thread synchronization with lock
        self.lock = threading.Lock()
    
    def increment(self):
        # Bug fixed: use lock to prevent race conditions
        with self.lock:
            temp = self.value
            time.sleep(0.001)  # Simulate some processing
            self.value = temp + 1
    
    def get_value(self):
        with self.lock:
            return self.value

def worker(counter, iterations):
    for i in range(iterations):
        counter.increment()

# Bug fixed: threads now work correctly with synchronization
counter = Counter()
threads = []

for i in range(5):
    thread = threading.Thread(target=worker, args=(counter, 100))
    threads.append(thread)
    thread.start()

# Threads are properly synchronized now
for thread in threads:
    thread.join()

print(f"Final counter value: {counter.get_value()}")
print("Expected: 500, and now we get exactly 500 due to proper synchronization")
