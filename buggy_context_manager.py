class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        # Bug fixed: handle file open errors and return file object
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except Exception:
            # Re-raise so caller can handle, but ensure attribute exists for __exit__
            self.file = None
            raise
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Bug fixed: ensure file is closed if it was opened
        try:
            if getattr(self, 'file', None):
                self.file.close()
        except Exception:
            pass
        # Do not suppress exceptions; propagate by returning False
        return False

# Usage example
try:
    with FileManager('nonexistent.txt', 'R') as f:
        print(f.read())
except Exception as e:
    print(f"Error: {e}")
