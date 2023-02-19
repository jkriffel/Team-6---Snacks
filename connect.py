<<<<<<< Updated upstream
import flask
import os
from flask import send_from_directory

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()

# import psycpog2

# class Adaptor():
#   def __init__(self):
#     pass
  
#   def create(self, first, last, code, playerID):
#     self.first = first
#     self.last = last
#     self.code = code
#     self.playerID = playerID
    
#     try:
#       myconnect = psycopg2.connect(dbname="", user="", password="", host="")
#       mycursor = myconnect.cursor()
      
#     except:
#        print("Can't connect")
        
#     entry = "INSERT INTO player (first, last, code, playerID) VALUES (%s, %s, %s, %s)"
#     playerValues = (self.first, self.last, self.code, self.playerID)
    
#     try:
#       mycursor.execute(entry, playerValues)
#       myconnect.commit()
    
#     except:
#       print("Error in adding player")
    
    
#     myconnect.close()
    
#     return 1
=======
from flask import Flask, redirect, url_for, render_template

#Making our application
app = Flask(__name__)
# When link is loaded go straight to splashPage
@app.route("/")
@app.route("/splashScreen")
def splashScreen():
    return render_template('proton.html','proton.py')

# Player entry route
@app.route("/playerEntry")
def playerScreen():
    return "Player Screen"

if __name__ == "__main__":
    app.run()
>>>>>>> Stashed changes
