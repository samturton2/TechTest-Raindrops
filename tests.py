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

	# Run more tests, testing all output options
	def test_single(self):
		self.assertEqual(raindrops(6), "Pling")
		self.assertEqual(raindrops(5), "Plang")

	def test_doubles(self):
		self.assertEqual(raindrops(21), "PlingPlong")
		self.assertEqual(raindrops(35), "PlangPlong")

	def test_triples(self):
		self.assertEqual(raindrops(525), "PlingPlangPlong")

	# Test for some large numbers
	def test_largenumber(self):
		self.assertEqual(raindrops(9366046200), "PlingPlangPlong")
		self.assertEqual(raindrops(1016850019), "1016850019")

	# Test for more obscure inputs
	def test_obscure(self):
		self.assertEqual(raindrops(-5), "Plang")
		self.assertEqual(raindrops(-34.4594), "-34.4594")

	# Test for TypeErrors
	def test_type_error(self):
		# Test for string passing
		with self.assertRaises(TypeError):
			raindrops("Pling")
		# Test for list passing
		with self.assertRaises(TypeError):
			raindrops([2, 3, 5, 234])
		# Test for tuple passing
		with self.assertRaises(TypeError):
			raindrops((3, 5))

# Run unit tests if test file ran
if __name__ == "__main__":
	unittest.main()
