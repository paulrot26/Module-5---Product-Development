import pandas as pd

df = pd.read_csv("03_Library Systembook.csv")   
df

df1 = pd.read_csv("03_Library SystemCustomers.csv")   
df1


df["Books"] = df["Books"].str.title()

df["Books"]

df = df.dropna(subset=["Books"])
df1 = df1.dropna()

df["Book checkout"] = df["Book checkout"].replace({'"': ''}, regex=True)

df["Book checkout_valid"] = pd.to_datetime(df["Book checkout"], errors="coerce")

df["Book checkout"] = pd.to_datetime(df["Book checkout"], errors="coerce")  
df["Book Returned"] = pd.to_datetime(df["Book Returned"], errors="coerce")

df["Book Due Back"] = df["Book checkout"] + pd.Timedelta(days=14)

df["Book Due Back"] = pd.to_datetime(df["Book Due Back"], errors="coerce")

df["Overdue"] = df["Book Returned"] > df["Book Due Back"]

# Creating and using a function to enrich the data by adding in the time a book was on loan.
data_enriched = df.copy()

def enrich_dateDuration(colA, colB, df=data_enriched):
    """
    Takes the two input columns and the dataframe to create a new column date_delta which is the difference, in days, between colA and colB.
    
    Note: ColA should be the highest of the expected date columns.
    """
    df['date_delta'] = (df[colA]-df[colB]).dt.days
    return df.head()

enrich_dateDuration(df=data_enriched, colA='Book Returned', colB='Book checkout')

data_enriched = df.copy()
data_enriched['loan_duration'] = (data_enriched['Book Returned'] - data_enriched['Book checkout']).dt.days
data_enriched.head()

data_enriched.to_csv("Cleaned_03_Library Systembook.csv", index=False)
df1.to_csv("Cleaned_03_Library SystemCustomers.csv", index=False)