import unittest
import roman_numerals_encoder

class TestRomanNumeralEncoder(unittest.TestCase):

    def test_solution(self):
 
        self.assertEqual(roman_numerals_encoder.solution(3999), "MMMCMXCIX")
        self.assertEqual(roman_numerals_encoder.solution(2400), "MMCD")
        self.assertEqual(roman_numerals_encoder.solution(1449), "MCDXLIX")
        self.assertEqual(roman_numerals_encoder.solution(350), "CCCL")
        self.assertEqual(roman_numerals_encoder.solution(74), "LXXIV")
        self.assertEqual(roman_numerals_encoder.solution("74"), "LXXIV")

        with self.assertRaises(ValueError):
            roman_numerals_encoder.solution("three thousand")


if __name__ == "__main__":
    unittest.main()