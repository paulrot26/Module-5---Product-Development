

df = pd.read_csv("03_Library Systembook.csv")   
df


df["Books"] = df["Books"].str.title()

df["Books"]

df = df.dropna(subset=["Books"])

df["Book checkout"] = df["Book checkout"].replace({'"': ''}, regex=True)

df["Book checkout_valid"] = pd.to_datetime(df["Book checkout"], errors="coerce")

df1 = pd.read_csv("03_Library SystemCustomers.csv")   
df1

df1 = df1.dropna()

df["Book checkout"] = pd.to_datetime(df["Book checkout"], errors="coerce")  
df["Book Returned"] = pd.to_datetime(df["Book Returned"], errors="coerce")

df["Book Due Back"] = df["Book checkout"] + pd.Timedelta(days=14)

df["Book Due Back"] = pd.to_datetime(df["Book Due Back"], errors="coerce")

df["Overdue"] = df["Book Returned"] > df["Book Due Back"]


df.to_csv("Cleaned_03_Library Systembook.csv", index=False)
df1.to_csv("Cleaned_03_Library SystemCustomers.csv", index=False)