import unittest
from Home import Home

class MyTestCase(unittest.TestCase):
  def test_default_greeting_set(self):
    hw = Home()
    self.assertEqual(hw.message, 'Project Wiian!')

if __name__ == '__main__':
  unittest.main()
