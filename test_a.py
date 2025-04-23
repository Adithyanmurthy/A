import unittest
import subprocess

class TestAdithyaScript(unittest.TestCase):
    def test_output(self):
        result = subprocess.run(['python', 'a.py'], capture_output=True, text=True)
        self.assertIn("Hello from Adithya Python", result.stdout)

if __name__ == '__main__':
    unittest.main()