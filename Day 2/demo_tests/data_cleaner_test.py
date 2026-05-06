import unittest


class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        self.df =pd.DataFrame({
            "Book checkout": ["2024-01-01", "invalid", None],
            "Book Returned": ["2024-01-10", "2024-01-20", None]
        })
        self.cleaned = myFunction(self.df.copy())

#Test column exists
    def test_days_between_column_exists(self):
        self.assertIn("Days Between", self.cleaned.columns)

#test data is valid
    def test_days_between_correct_value(self):
        self.assertEqual(self.cleaned.loc[0, "Days Between"],9)


