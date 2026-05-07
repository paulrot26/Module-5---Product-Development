import pandas as pd
from pathlib import Path


def enrich_date_duration(df, colA, colB):
    df["date_delta"] = (df[colA] - df[colB]).dt.days
    return df


def load_and_clean_books(path_books):
    df = pd.read_csv(path_books)

    df["Books"] = df["Books"].str.title()
    df = df.dropna(subset=["Books"])

    df["Book checkout"] = (df["Book checkout"].replace({'"': ""}, regex=True)
        .pipe(pd.to_datetime, format="%d/%m/%Y", errors="coerce")
    )

    df["Book Returned"] = pd.to_datetime(
        df["Book Returned"], format="%d/%m/%Y", errors="coerce"
    )

    df["Book Due Back"] = df["Book checkout"] + pd.Timedelta(days=14)
    df["Overdue"] = df["Book Returned"] > df["Book Due Back"]
    df["loan_duration"] = (df["Book Returned"] - df["Book checkout"]).dt.days

    return df


def load_and_clean_customers(path_customers):
    df1 = pd.read_csv(path_customers)
    return df1.dropna()


def clean_library_data(
    books_path="03_LibrarySystembook.csv",
    customers_path="03_LibrarySystemCustomers.csv",
    output_dir="/app/output",
):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Cleaning books dataset…")
    books_df = load_and_clean_books(books_path)

    print("Cleaning customers dataset…")
    customers_df = load_and_clean_customers(customers_path)

    print("Enriching books dataset…")
    books_df = enrich_date_duration(books_df, "Book Returned", "Book checkout")

    # Output paths
    books_out = output_dir / "Cleaned_03_LibrarySystembook.csv"
    customers_out = output_dir / "Cleaned_03_LibrarySystemCustomers.csv"

    print(f"Writing cleaned books CSV → {books_out}")
    books_df.to_csv(books_out, index=False)

    print(f"Writing cleaned customers CSV → {customers_out}")
    customers_df.to_csv(customers_out, index=False)

    print("\n===== CLEANED BOOKS DATA =====")
    print(books_df.head(10).to_string(index=False))

    print("\n===== CLEANED CUSTOMERS DATA =====")
    print(customers_df.head(10).to_string(index=False))

    print("\nCleaning complete. CSV files generated and printed.")

    return books_df, customers_df


if __name__ == "__main__":
    clean_library_data()
