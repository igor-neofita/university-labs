import unittest
def count_vowels(text):
    vowels = "аеєиіїоуюя"
    count = 0

    for letter in text.lower():
        if letter in vowels:
            count += 1

    return count
class TestCountVowels(unittest.TestCase):

    def test_normal_text(self):
        self.assertEqual(count_vowels("Привіт"), 2)

    def test_empty_text(self):
        self.assertEqual(count_vowels(""), 0)

    def test_digits(self):
        self.assertEqual(count_vowels("12345"), 0)

    def test_ukrainian_letters(self):
        self.assertEqual(count_vowels("Україна"), 4)
if __name__ == "__main__":
    unittest.main()
