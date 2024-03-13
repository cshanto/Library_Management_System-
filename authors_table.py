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


def authorsTable():
    operation = st.sidebar.selectbox("Choose operation ",("CREATE","READ","UPDATE","DELETE"))
         # When CREATE operation is selected, following data fields are displayed
    if operation == "CREATE":
        st.subheader("Enter new Authors records")
        firstname = st.text_input("Enter firstname of the author")
        lastname = st.text_input("Enter lastname of the author")
        nationality = st.text_input("Enter Nationality")
        dob = st.date_input("Enter D.O.B of the author")
        # Construct the 'CREATE' button and its functionality
        if st.button("CREATE"):
            sqlQuery= "insert into authors(FIRSTNAME, LASTNAME, NATIONALITY, `D.O.B`) values(%s, %s, %s, %s)"
            val = (firstname, lastname, nationality, dob,)
            myCursor1.execute(sqlQuery,val)
            librarydb.commit()
            st.success("Record Created Successfully!!")
        print(f"DB operation successfull")

        # When READ operation is selected
    elif operation == "READ":
        st.subheader("Read Records of authors")
        if st.button("READ"):
            myCursor1.execute("select * from authors")
            result = myCursor1.fetchall()
            for i in result:
                st.write(i)
        print(f"DB operation successfull")

    # When UPDATE operation is selected
    elif operation == "UPDATE":
        st.subheader("Update a Record of an author")
        author_id = st.text_input("Enter authors ID")
        firstname = st.text_input("Enter firstname of the author")
        lastname = st.text_input("Enter lastname of the author")
        nationality = st.text_input("Enter Nationality")
        dob = st.date_input("Enter D.O.B of the author")
        # Constructing the 'UPDATE' button with its functionality
        if st.button("UPDATE"):
            sqlQuery = "update authors set FIRSTNAME=%s, LASTNAME=%s, NATIONALITY=%s, `D.O.B`=%s where author_id =%s"
            val = (firstname, lastname, nationality, dob,author_id,)
            myCursor1.execute(sqlQuery,val)
            librarydb.commit()
            st.success("Record updated Successfully!!")
        print(f"DB operation successfull")

        # When DELETE operation is selected
    elif operation == "DELETE":
        st.subheader("Delete a Record of an author")
        author_id = st.text_input("Enter authors id")
        # Constructing the 'DELETE' button with its functionality
        if st.button("DELETE"):
            sqlQuery = "delete from authors where author_id = %s"   
            val = (author_id,)
            myCursor1.execute(sqlQuery,val)
            librarydb.commit()
            st.success("Record Deleted Successfully!!")
        print(f"DB operation successfull")
