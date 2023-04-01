import mysql.connector as mysql
import pandas as pd

# Connect to the database
User_Name="root"
Password = "yourpassword"
myhost = "localhost"
mydatabase="first_database"
db_connection = mysql.connect(user=User_Name, password=Password,
                              host=myhost, database=mydatabase)
cursor = db_connection.cursor()

# Read data from the Excel file into a pandas DataFrame
df = pd.read_excel("E:\Jupyter notebook\Linked_in learning DS\sales.xlsx")
# Define the table name and column names/types
table_name = "sales_report"
column_names = list(df.columns)
column_types = ["VARCHAR(255)" for i in range(len(column_names))]

# Create the new table
query = f"CREATE TABLE {table_name} ("
for i in range(len(column_names)):
    query += f"{column_names[i]} {column_types[i]}, "
query = query[:-2] + ")"
cursor.execute(query)

# Insert each row into the new table
query = f"INSERT INTO {table_name} ("
for col in column_names:
    query += col + ", "
query = query[:-2] + ") VALUES ("
for i in range(len(column_names)):
    query += "%s, "
query = query[:-2] + ")"

for index, row in df.iterrows():
    values = tuple(row)
    cursor.execute(query, values)

# Commit the changes and close the cursor and connection
db_connection.commit()
cursor.close()
db_connection.close()