import psycpog2

class Adaptor():
  def __init__(self):
    pass
  
  def create(self, first, last, code, playerID):
    self.first = first
    self.last = last
    self.code = code
    self.playerID = playerID
    
    try:
      myconnect = psycopg2.connect(dbname="", user="", password="", host="")
      mycursor = myconnect.cursor()
      
    except:
       print("Can't connect")
        
    entry = "INSERT INTO player (first, last, code, playerID) VALUES (%s, %s, %s, %s)"
    playerValues = (self.first, self.last, self.code, self.playerID)
    
    try:
      mycursor.execute(entry, playerValues)
      myconnect.commit()
    
    except:
      print("Error in adding player")
    
    
    myconnect.close()
    
    return 1
                               
