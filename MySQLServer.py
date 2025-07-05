import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server (replace user and password as needed)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="%Cari0n@Gugsa%",
        
    )

    cursor = connection.cursor()

    # Create database if it does not exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

