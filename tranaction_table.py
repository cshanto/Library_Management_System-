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

def transactionTable():
    operation = st.sidebar.selectbox("Choose operation ",("CREATE","READ","UPDATE","DELETE"))
    if operation == "CREATE":
        st.subheader("Enter new transactions records")
        transaction_id = st.text_input("Enter Transaction id")
        user_id = st.text_input("Enter User id")
        book_id = st.text_input("Enter Book id")
        borrow_date = st.date_input("Enter Borrow date")
        return_date = st.date_input("Enter Return date")
        late_fee = st.text_input("Enter late fee amount")
        #TRANSACTION_ID, USER_ID, BOOK_ID, BORROW_DATE, RETURN_DATE, `LATE_FEE(₹)`
        if st.button("CREATE"):
            sqlQuery = "insert into transactions(TRANSACTION_ID, USER_ID, BOOK_ID, BORROW_DATE, RETURN_DATE, `LATE_FEE(₹)`) values(%s,%s,%s,%s,%s,%s)"
            val = (transaction_id, user_id, book_id, borrow_date, return_date, late_fee,)
            myCursor1.execute(sqlQuery,val)
            librarydb.commit()
            st.success("Record Created Successfully!!")
        print(f"DB operation successfull") 
        

    elif operation == "READ":
        st.subheader("Read book records")
        if st.button("READ"):
               myCursor1.execute("select * from transactions")
               result = myCursor1.fetchall()
               for i in result:
                      st.write(i)
        print(f"DB operation successfull") 

    elif operation == "UPDATE":
        st.subheader("Update book records")
        transaction_id = st.text_input("Enter Transaction id")
        user_id = st.text_input("Enter U id")
        book_id = st.text_input("Enter B id")
        borrow_date = st.date_input("Enter Borrow date")
        return_date = st.date_input("Enter Return date")
        late_fee = st.text_input("Enter late fee amount")
        #TRANSACTION_ID, USER_ID, BOOK_ID, BORROW_DATE, RETURN_DATE, `LATE_FEE(₹)`
        if st.button("CREATE"):
            sqlQuery = "insert into transactions(TRANSACTION_ID, USER_ID, BOOK_ID, BORROW_DATE, RETURN_DATE, `LATE_FEE(₹)`) values(%s,%s,%s,%s,%s,%s)"
            val = (transaction_id, user_id, book_id, borrow_date, return_date, late_fee,)
            myCursor1.execute(sqlQuery,val)
            librarydb.commit()
            st.success("Record Created Successfully!!")
        print(f"DB operation successfull") 

    elif operation == "DELETE":
                st.subheader("Delete transactions records")
                transaction_id = st.text_input("Enter transaction id")
                if st.button("DELETE"):
                    sqlQuery = "Delete from transactions where transaction_id = %s"
                    val = (transaction_id,)
                    try:
                        myCursor1.execute(sqlQuery,val,)
                        librarydb.commit()
                        st.success("Transaction deleted successfully!!!")
                    except Exception as e:
                         print(f"Error occured : {e}")
                    print("Success")