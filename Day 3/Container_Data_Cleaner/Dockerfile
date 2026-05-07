FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your cleaning module + input CSVs
COPY data_cleaner_test.py .
COPY 03_LibrarySystembook.csv .
COPY 03_LibrarySystemCustomers.csv .

# Output directory for cleaned CSVs
RUN mkdir -p /app/output

# Run the cleaner
CMD ["python", "data_cleaner_test.py"]
