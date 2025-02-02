from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, this is a Flask app running in Docker. Created by Aman Kumar"

@app.route("/db")
def check_db():
    try:
        connection = mysql.connector.connect(
            host="mysql-container",  
            user="root",
            password="rootpassword",
            database="test_db"
        )
        if connection.is_connected():
            return "Connected to MySQL successfully. AK!!! "
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

