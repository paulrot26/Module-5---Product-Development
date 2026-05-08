import pandas as pd
from pathlib import Path


def enrich_date_duration(df, colA, colB):
    df["date_delta"] = (df[colA] - df[colB]).dt.days
    return df


def generate_metrics(before_df, after_df, dataset_name):
    metrics = {}

    metrics["dataset"] = dataset_name
    metrics["rows_before"] = len(before_df)
    metrics["rows_after"] = len(after_df)
    metrics["rows_removed"] = len(before_df) - len(after_df)

    # Null handling
    metrics["nulls_before"] = before_df.isna().sum().sum()
    metrics["nulls_after"] = after_df.isna().sum().sum()

    # Duplicate handling
    metrics["duplicates_before"] = before_df.duplicated().sum()
    metrics["duplicates_after"] = after_df.duplicated().sum()

    # Schema info
    metrics["columns"] = len(after_df.columns)
    metrics["memory_mb"] = round(after_df.memory_usage(deep=True).sum() / 1_000_000, 3)

    # Date quality metrics (only for books dataset)
    if dataset_name == "books":
        metrics["invalid_checkout_dates"] = after_df["Book checkout"].isna().sum()
        metrics["invalid_return_dates"] = after_df["Book Returned"].isna().sum()
        metrics["overdue_count"] = after_df["Overdue"].sum()

        # Loan duration stats
        metrics["loan_duration_min"] = after_df["loan_duration"].min()
        metrics["loan_duration_max"] = after_df["loan_duration"].max()
        metrics["loan_duration_avg"] = round(after_df["loan_duration"].mean(), 2)

    return metrics


def load_and_clean_books(path_books):
    df = pd.read_csv(path_books)
    before_df = df.copy()

    df["Books"] = df["Books"].str.title()
    df = df.dropna(subset=["Books"])

    df["Book checkout"] = (
        df["Book checkout"]
        .replace({'"': ""}, regex=True)
        .pipe(pd.to_datetime, format="%d/%m/%Y", errors="coerce")
    )

    df["Book Returned"] = pd.to_datetime(
        df["Book Returned"], format="%d/%m/%Y", errors="coerce"
    )

    df["Book Due Back"] = df["Book checkout"] + pd.Timedelta(days=14)
    df["Overdue"] = df["Book Returned"] > df["Book Due Back"]
    df["loan_duration"] = (df["Book Returned"] - df["Book checkout"]).dt.days

    return before_df, df


def load_and_clean_customers(path_customers):
    df = pd.read_csv(path_customers)
    before_df = df.copy()
    return before_df, df.dropna()


def clean_library_data(
    books_path="03_LibrarySystembook.csv",
    customers_path="03_LibrarySystemCustomers.csv",
    output_dir="/app/output",
):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Cleaning books dataset…")
    books_before, books_df = load_and_clean_books(books_path)

    print("Cleaning customers dataset…")
    customers_before, customers_df = load_and_clean_customers(customers_path)

    print("Enriching books dataset…")
    books_df = enrich_date_duration(books_df, "Book Returned", "Book checkout")

    # Output paths
    books_out = output_dir / "Cleaned_03_LibrarySystembook.csv"
    customers_out = output_dir / "Cleaned_03_LibrarySystemCustomers.csv"
    metrics_out = output_dir / "DataEngineeringMetrics.csv"

    print(f"Writing cleaned books CSV → {books_out}")
    books_df.to_csv(books_out, index=False)

    print(f"Writing cleaned customers CSV → {customers_out}")
    customers_df.to_csv(customers_out, index=False)

    # Generate metrics
    metrics_list = []
    metrics_list.append(generate_metrics(books_before, books_df, "books"))
    metrics_list.append(generate_metrics(customers_before, customers_df, "customers"))

    metrics_df = pd.DataFrame(metrics_list)
    metrics_df.to_csv(metrics_out, index=False)

    print("\n===== DATA ENGINEERING METRICS =====")
    print(metrics_df.to_string(index=False))

    print("\nCleaning complete. CSV files generated and printed.")

    return books_df, customers_df, metrics_df


if __name__ == "__main__":
    clean_library_data()
