import requests
import psycopg2

# Define the API endpoint URL
api_url = "http://localhost:5000/data"

# Define PostgreSQL connection parameters
db_params = {
    "dbname": "your_db_name",
    "user": "your_user",
    "password": "your_password",
    "host": "localhost",
    "port": "5432",
}

# Fetch data from the API
try:
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Failed to fetch data from the API. Status code: {response.status_code}")
        data = []

except Exception as e:
    print(f"Error fetching data from the API: {str(e)}")
    data = []

# Insert fetched data into the PostgreSQL database
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    for item in data:
        # Adjust the table and column names as needed
        insert_query = "INSERT INTO my_data (name, description) VALUES (%s, %s)"
        cursor.execute(insert_query, (item.get("name", ""), item.get("description", "")))

    connection.commit()
    print("Data inserted into the PostgreSQL database.")

except Exception as e:
    print(f"Error inserting data into the PostgreSQL database: {str(e)}")

finally:
    cursor.close()
    connection.close()
