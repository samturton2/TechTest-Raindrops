# Import raindrops function
from main import raindrops

# Import unittest
import unittest

# Create class to apply testing
class Tests(unittest.TestCase):

	# Example tests
	def test_examples(self):
		self.assertEqual(raindrops(28), "Plong")
		self.assertEqual(raindrops(30), "PlingPlang")
		self.assertEqual(raindrops(34), "34")

# Run unit tests if test file ran
if __name__ == "__main__":
	unittest.main()

