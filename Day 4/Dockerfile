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

# Run the cleaner once at startup, then keep container alive
#CMD ["sh", "-c", "python data_cleaner_test.py && tail -f /dev/null"]

#Run the cleaner repeatedly (e.g., every 60 seconds)
#CMD ["sh", "-c", "while true; do python data_cleaner_test.py; sleep 60; done"]



