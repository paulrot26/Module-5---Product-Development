import pandas as pd
import unittest
from data_cleaner import enrich_dateDuration

data = [
    ["2026-01-01", "2026-01-14"],["2026-02-01", "2026-02-14"],["2026-02-14", "2026-02-28"],
    ["2026-01-10", "2026-01-24"],["2026-02-10", "2026-02-24"],["2026-03-15", "2026-03-29"],
    ["2026-03-12", "2026-03-26"]
]

df = pd.DataFrame(data, columns=["Checkout", "Return"])
df["Checkout"] = pd.to_datetime(df["Checkout"])
df["Return"] = pd.to_datetime(df["Return"])


class TestDateData(unittest.TestCase):

    def test_checkout_dates(self):
        df = pd.DataFrame({
            "Checkout": [
                "2026-01-01",
                "2026-02-01",
                "2026-02-01",
                "2026-01-10",
                "2026-02-10",
                "2026-03-01",
                "2026-03-10"
            ]
        })

        df["Checkout"] = pd.to_datetime(df["Checkout"])

        # Example assertEqual checks
        self.assertEqual(len(df), 7)  # row count
        # Check first date value
        self.assertEqual(df.loc[0, "Checkout"], pd.Timestamp("2026-01-01"))
        # Check that all years are the same
        self.assertEqual(df["Checkout"].dt.year.nunique(), 1)
        # Check the year value itself
        self.assertEqual(df["Checkout"].dt.year.iloc[0], 2026)

    def test_14_day_difference(self):
        # Use the df created at the top of the file
        df_local = df.copy()

        # Calculate the difference in days
        df_local["Days_Between"] = (df_local["Return"] - df_local["Checkout"]).dt.days

        # Assert all differences are exactly 14 days
        self.assertEqual(df_local["Days_Between"].nunique(), 1)
        self.assertEqual(df_local["Days_Between"].iloc[0], 14)

if __name__ == "__main__":
    unittest.main()


print(df.head())
