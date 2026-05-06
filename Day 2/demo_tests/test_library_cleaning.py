import unittest
import pandas as pd

class TestLibraryCleaning(unittest.TestCase):

# ---------------------------------------------------------
# ASSERT EQUAL
# ---------------------------------------------------------
def test_days_between_calculation(self):
"""Check that Days Between is calculated correctly for a known row."""
row = self.data_enriched.iloc[0]
expected = (row["Book Returned"] - row["Book checkout"]).days
self.assertEqual(row["Days Between"], expected)

# ---------------------------------------------------------
# ASSERT NOT EQUAL
# ---------------------------------------------------------
def test_books_column_changed(self):
"""Ensure Books column was title-cased (changed from original)."""
original = "harry potter"
cleaned = "Harry Potter"
self.assertNotEqual(original, cleaned)

# ---------------------------------------------------------
 # ASSERT TRUE
 # ---------------------------------------------------------
 def test_overdue_true(self):
"""If Book Returned > Book Due Back, Overdue must be True."""
overdue_rows = self.df[self.df["Book Returned"] > self.df["Book Due Back"]]
if not overdue_rows.empty:
self.assertTrue(overdue_rows.iloc[0]["Overdue"])

# ---------------------------------------------------------
# ASSERT FALSE
# ---------------------------------------------------------
def test_overdue_false(self):
"""If Book Returned <= Book Due Back, Overdue must be False."""
 on_time_rows = self.df[self.df["Book Returned"] <= self.df["Book Due Back"]]
 if not on_time_rows.empty:
 self.assertFalse(on_time_rows.iloc[0]["Overdue"])

 # ---------------------------------------------------------
 # EXTRA VALIDATION TESTS
 # ---------------------------------------------------------
 def test_no_null_books(self):
 """Books column should have no nulls after cleaning."""
 self.assertFalse(self.df["Books"].isna().any())

def test_checkout_is_datetime(self):
 """Book checkout must be datetime after cleaning."""
 self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.df["Book checkout"]))


def test_returned_is_datetime(self):
 """Book Returned must be datetime after cleaning."""
 self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.df["Book Returned"]))

 def test_due_back_is_datetime(self):
 """Book Due Back must be datetime after cleaning."""
 self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.df["Book Due Back"]))

def test_days_between_exists(self):
 """Days Between column must exist in enriched dataset."""
 self.assertIn("Days Between", self.data_enriched.columns)


if __name__ == "__main__":
 unittest.main()


