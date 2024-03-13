import mysql.connector
import streamlit as st

# Establish the Sql connection
librarydb = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="root",
    database="librarydb"
)

# Create a cursor
myCursor1 = librarydb.cursor()

def booksTable():
    operation = st.sidebar.selectbox("Choose operation ",("CREATE","READ","UPDATE","DELETE"))
        # When CREATE operation is selected, following data fields are displayed
    if operation == "CREATE":
        st.subheader("Enter new book records")
        Title = st.text_input("Enter title of the book")
        ISBN = st.text_input("Enter ISBN number of the book")
        Publication_date = st.date_input("Enter Publication Date")
        genre = st.text_input("Enter Genre of the book")
        available = st.checkbox("Availability?")
        # Construct the 'CREATE' button and its functionality
        if st.button("CREATE"):
            sqlQuery= "insert into books(TITLE, ISBN, PUBLICATION_DATE, GENRE, AVAILABLE) values(%s, %s, %s, %s, %s)"
            val = (Title, ISBN, Publication_date, genre, available,)
            myCursor1.execute(sqlQuery,val)
            librarydb.commit()
            st.success("Record Created Successfully!!")
        print(f"DB operation successfull")

        # When READ operation is selected
    elif operation == "READ":
        st.subheader("Read all Records of books")
        # firstname = st.text_input("Enter firstname")
        # lastname = st.text_input("Enter lastname")
        # email = st.text_input("Enter email")
        if st.button("READ"):
            myCursor1.execute("select * from books")
            result = myCursor1.fetchall()
            for i in result:
                st.write(i)
        print(f"DB operation successfull")
        #         result = read_record(myCursor1, firstname)
        #         if result:
        #             st.write(result)
        #         else:
        #             st.warning("No records found matching the entered firstname.")

        # When UPDATE operation is selected
    elif operation == "UPDATE":
        st.subheader("Update a Record of a book")
        book_id = st.text_input("Enter Book ID")
        Title = st.text_input("Enter title of the book")
        ISBN = st.text_input("Enter ISBN number of the book")
        Publication_date = st.date_input("Enter Publication Date")
        genre = st.text_input("Enter Genre of the book")
        available = st.checkbox("Availability?")
        # Constructing the 'UPDATE' button with its functionality
        if st.button("UPDATE"):
            sqlQuery = "update books set TITLE=%s, ISBN=%s, PUBLICATION_DATE=%s, GENRE=%s, AVAILABLE=%s where book_id =%s"
            val = (Title, ISBN, Publication_date, genre, available,book_id,)
            myCursor1.execute(sqlQuery,val)
            librarydb.commit()
            st.success("Record updated Successfully!!")
        print(f"DB operation successfull")

        # When DELETE operation is selected
    elif operation == "DELETE":
        st.subheader("Delete a Record of a book")
        book_id = st.text_input("Enter book id")
        # Constructing the 'DELETE' button with its functionality
        if st.button("DELETE"):
            sqlQuery = "delete from books where book_id = %s"   
            val = (book_id,)
            myCursor1.execute(sqlQuery,val)
            librarydb.commit()
            st.success("Record Deleted Successfully!!")
        print(f"DB operation successfull")
