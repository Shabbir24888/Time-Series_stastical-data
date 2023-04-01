import pymysql
import pandas as pd

# Open database connection
db = pymysql.connect(host="localhost", user="yourusername", password="yourpassword", database="yourdatabase")

# execute SQL query
query = "SELECT * FROM yourtable"
df = pd.read_sql(query, db)

# print the dataframe
print(df)

# close the database connection
db.close()
