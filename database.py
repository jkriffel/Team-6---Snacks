import psycopg2

DB_HOST = "ec2-52-201-124-168.compute-1.amazonaws.com"
DB_NAME = "daf852u68chkv6"
DB_USER = "ymvkfvfaiyyqrb"
DB_PASS = "0bb71cbd549be10c112e262649118e7fa139c06835b6417c3f20521868c00165"

def return_database():
    try:
        myData = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)
        return myData
    except Exception:
        print("connection failed")
        return 

def check_user_from_id(id):
    myConnection = return_database()
    myCurrent = myConnection.cursor()

    myCurrent.execute("SELECT * FROM player WHERE id = %s;", (id,))

    if myCurrent.fetchone():
        myCurrent.close()
        myConnection.close()
        return True
    else:
        myCurrent.close()
        myConnection.close()
        return False


def get_user_codename(id):
    #Create connection with heroku postgres add on
    myConnection = return_database()
    myCurrent = myConnection.cursor()

    #check if the user exists, if it does, fetch
    if check_user_from_id(id):
        myCurrent.execute("SELECT * FROM player WHERE id = %s;", (id,))
        data = myCurrent.fetchone()

        myCurrent.close()
        myConnection.close()
        return data[3]
    #if not, return error message
    else:
        myCurrent.close()
        myConnection.close()
        return "USER DNE"


def create_user(id, codename):
    #Create connection with heroku postgres add on
    myConnection = return_database()
    myCurrent = myConnection.cursor()

    #check if user is exists, if it does, error
    if check_user_from_id(id):
        myCurrent.close()
        myConnection.close()

        print("User exists already")
    #if not, add user to table
    else:
        myCurrent.execute("INSERT INTO player (id, first_name, last_name, codename) VALUES (%s, %s, %s, %s);",
                (id, None, None, codename))

        myConnection.commit()
        myCurrent.close()
        myConnection.close()


def remove_user(id, codename):
    #Create connection with heroku postgres add on
    myConnection = return_database()
    myCurrent = myConnection.cursor()

    #check if user is exists, if it does, error
    if check_user_from_id(id):
        myCurrent.close()
        myConnection.close()
        
        myCurrent.execute("DELETE FROM player (id, first_name, last_name, codename) VALUES (%s, %s, %s, %s);",
                (id, None, None, codename))

        myConnection.commit()
        myCurrent.close()
        myConnection.close()