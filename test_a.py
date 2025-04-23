import unittest
import subprocess
import os

class TestAdithyaScript(unittest.TestCase):
    def test_output(self):
        script_path = os.path.join(os.path.dirname(__file__), 'a.py')  # ✅ ensures correct path
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        print("Captured Output:", result.stdout)
        self.assertIn("Hello from Adithya Python", result.stdout)

if __name__ == '__main__':
    unittest.main()
