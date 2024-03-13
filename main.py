#import the modules and external files
import mysql.connector
import streamlit as st
import books_table
import authors_table
import users_table
import tranaction_table

# Establish the Sql connection
librarydb = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="root",
    database="librarydb"
)
# Create a cursor
myCursor1 = librarydb.cursor()
print(f"DB connection successfull")

# Create streamlit web app
def main():
    st.title("LIBRARY MANAGEMENT SYSTEM")
    # Create operation options
    tables = st.sidebar.selectbox("Choose table ",("BOOKS","AUTHORS","USERS","TRANSACTIONS"))
    # Perform the CRUD operations
    # when BOOKS table is selected
    if tables == "BOOKS":
        books_table.booksTable()
        
    elif tables == "AUTHORS":
        authors_table.authorsTable()

    elif tables == "USERS":
        users_table.usersTable()
        
    elif tables == "TRANSACTIONS":
        tranaction_table.transactionTable()

# Function for reading a record
def read_record(Cursor, firstname_):
  try:
    sqlQuery = "SELECT * FROM users1 WHERE firstname = %s"
    val = (firstname_,)
    Cursor.execute(sqlQuery, val)
    result = myCursor1.fetchone()
    return result
  except mysql.connector.Error as err:
    print("Error:", err)
    return None


if __name__ == "__main__":
    main()



