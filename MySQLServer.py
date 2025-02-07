import mysql.connector

try:
    # Connect to MySQL Server (without specifying a database)
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",  # Replace with your MySQL username
        password="yourpassword"  # Replace with your MySQL password
    )

    mycursor = mydb.cursor()

    # Create database if it doesn't exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Ensure database connection is closed
    if 'mycursor' in locals():
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("Database connection closed.")

