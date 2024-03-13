
import mysql.connector
import streamlit as st
import passlib.hash

# Method to hash a password
def hashPassword(password):
    return passlib.hash.bcrypt.encrypt(password)

# Method to update records
def updateRecords(user_id, username, password, firstname, lastname, email, myCursor1, librarydb):
    hashedPassword = hashPassword(password)
    sqlQuery = "update users set USERNAME=%s, `PASSWORD(hashed)`=%s, FIRSTNAME=%s, LASTNAME=%s, EMAIL=%s where user_id =%s"
    val = (username, hashedPassword, firstname, lastname, email, user_id)

    try:
        myCursor1.execute(sqlQuery, val)
        librarydb.commit()
        print("DB operation successful!")
    except Exception as e:
        print(f"Error updating record: {e}")

# method to Create new records
def createRecords(username, password, firstname, lastname, email, myCursor1, librarydb):
    hashedPassword = hashPassword(password)
    sqlQuery= "insert into users(USERNAME, `PASSWORD(hashed)`, FIRSTNAME, LASTNAME, EMAIL) values(%s, %s, %s, %s, %s)"
    val = (username,hashedPassword,firstname,lastname,email,)

    try:
        myCursor1.execute(sqlQuery,val)
        librarydb.commit()
        print("DB connection successfull")
    except Exception as e:
        print(f"Error occured : {e}")

# Establish the Sql connection
librarydb = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="root",
    database="librarydb"
)

# Create a cursor
myCursor1 = librarydb.cursor()

def usersTable():
    operation = st.sidebar.selectbox("Choose operation ",("CREATE","READ","UPDATE","DELETE"))
    # When CREATE operation is selected, following data fields are displayed
    if operation == "CREATE":
        # need to add sign/login in button with OTP authentication system
        # need to add hashing to store password into DB
        st.subheader("Enter new Users records")
        username = st.text_input("Enter username")
        password = st.text_input("Enter password", type="password")
        firstname = st.text_input("Enter Firstname")
        lastname = st.text_input("Enter lastname")
        email = st.text_input("Enter Email")
              
        # Construct the 'CREATE' button and its functionality
        if st.button("CREATE"):
            createRecords(username, password, firstname, lastname, email, myCursor1, librarydb)
            st.success("Record Created Successfully!!")
        print(f"DB operation successfull")

    elif operation == "READ":
        st.subheader("Read users records")
        if st.button('READ'):
            sqlQuery = "select * from users"
            myCursor1.execute(sqlQuery,)
            result = myCursor1.fetchall()
            for i in result:
                st.write(i)
        print("DB operation successfull!")

    elif operation == "UPDATE":
        st.subheader("Update users records")
        user_id = st.text_input("Enter user_id")
        username = st.text_input("Enter username")
        password = st.text_input("Enter password", type="password")
        firstname = st.text_input("Enter firstname")
        lastname = st.text_input("Enter lastname")
        email = st.text_input("Enter Email")
        if st.button("UPDATE"):
            updateRecords(user_id, username, password, firstname, lastname, email, myCursor1, librarydb)
            st.success("Records updated successfully!!!")
        print("DB operation successfull!!")


    elif operation == "DELETE":
        st.subheader("Delete users records")
        user_id = st.text_input("Enter user ID")
        if st.button("DELETE"):
            sqlQuery = "delete from users where user_id = %s"
            val = (user_id,)
            myCursor1.execute(sqlQuery, val)
            librarydb.commit()
            st.success("Record deleted successfully!!")
        print("DB operation successfull!!")
