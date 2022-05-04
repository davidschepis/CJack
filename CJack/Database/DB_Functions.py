import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="cjack"
)

class DB:
    def login(username, password):
        myc = mydb.cursor()
        myc.execute(f"select username, id from users where username='{username}' and u_password='{password}'")
        result = myc.fetchall()
        if (len(result) < 1):
            return False
        return result[0]
    
    def signup(username, password):
        try:
            myc = mydb.cursor()
            myc.execute(f"insert into users (username, u_password) values ('{username}', '{password}')")
            mydb.commit()
            myc.execute(f"select username, id from users where id={myc.lastrowid}")
            result = myc.fetchall()
            _, id = result[0]
            myc.execute(f"insert into user_data (user_id) values ({id})")
            mydb.commit()
            return result[0]
        except mysql.connector.Error as e:
            print(e)
            return False
        
    def get_scores():
        myc = mydb.cursor()
        myc.execute(f"select id, username, joined, chips, wins, losses, chips_won, chips_lost from users join user_data on users.id=user_data.user_id")
        result = myc.fetchall()
        if (len(result) < 1):
            return ""
        return result