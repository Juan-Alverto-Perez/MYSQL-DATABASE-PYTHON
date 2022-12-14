import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database ="gamestore"
)
mycursor = mydb.cursor()

def user():
  action = input(
    """What will you like to do:
  1: Create User
  2: Buy a game\n"""
  )
  while (action != '1' and action != '2'):
    action = input(
    """Error with choice! Try Again.
    What will you like to do:
    1: Create User
    2: Buy a game\n"""
  )
  if action == '1':
    createUser()
  elif action == '2':
    userId = int(input("What is ur ID number: "))
    realId = False
    mycursor.execute("SELECT userId FROM Users")
    IDS = mycursor.fetchall()

    for id in IDS:
      if userId in id:
        realId = True

    if realId:
      buyGame(userId)
    else:
      answer = input(
        """ID not found! Would you like to create User or exit:
          1:Create User
          2:Exit
          """)
      while(answer != '1' and answer != '2'):
        answer = input(
          """Error with option choice! Try Again.
          ID not found! Would you like to create User or exit:
          1:Create User
          2:Exit
          """)
      if answer == '1':
        createUser()
      elif answer == '2':
        exit()
def createUser():
  userInformation = input("Enter the following information on one line serperated by commas: (First Name, Last Name, username, password, email, address)\n")
  userInformation  = userInformation.replace(' ', '')
  userInformation = userInformation.split(',')
  
  

  sql = "INSERT INTO users (firstName, lastName, username, passwrd, email, address) VALUES ( %s, %s, %s, %s, %s, %s)"
  values = userInformation
  
  
  mycursor.execute(sql, values)
  mydb.commit()
  print("Your user has been added to the database")
def buyGame(userId):
  print('List of games you can buy:')
  mycursor.execute('SELECT gameId, gameName FROM games')
  games = mycursor.fetchall()
  for game in games:
    print(game)
  gameWant = int(input('Enter the Id of the game you would like from above'))
  today = date.today()
  
  sql = f"INSERT INTO library (userId, gameId, datePurchased) VALUES ({userId},{gameWant},{today})"
  mycursor.execute(sql)
  mydb.commit()
  print("Your game has been added to your library!")
  

def gameCompany():
  action = input(
    """What will you like to do:
  1: Create Game Company
  2: Make Game\n"""
  )
  while (action != '1' and action != '2'):
    action = input(
    """Error with choice! Try Again.
    What will you like to do:
    1: Create Game Company
    2: Make Game\n"""
  )
  if action == '1':
    createGameCompany()
  elif action == '2':
    studioId = int(input("What is ur ID number: "))
    realId = False
    mycursor.execute("SELECT studioId FROM gameStudio")
    IDS = mycursor.fetchall()


    for id in IDS:
      if studioId in id:
        realId = True

    if realId:
      makeGame(studioId)
    else:
      answer = input(
        """ID not found! Would you like to create User or exit:
          1:Create Game Company
          2:Exit
          """)
      while(answer != '1' and answer != '2'):
        answer = input(
          """Error with option choice! Try Again.
          ID not found! Would you like to create User or exit:
          1:Create Game Company
          2:Exit
          """)
      if answer == '1':
        createGameCompany()
      elif answer == '2':
        exit()
def createGameCompany():
  userInformation = input("Enter the following information on one line serperated by commas: (Studio Name, studio number, studio email, Rep. name, Rep. email, Rep. number, address)\n")
  userInformation  = userInformation.replace(' ', '')
  userInformation = userInformation.split(',')
  
  

  sql = "INSERT INTO gameStudio (studioName, contactNumber, contactEmail, representativeName, representativeEmail, representativeNumber, address) VALUES ( %s, %s, %s, %s, %s, %s, %s)"
  values = userInformation
  
  
  mycursor.execute(sql, values)
  mydb.commit()
  print("Your sutdio has been added to the database")
def makeGame(studioId):
  userInformation = input("Enter the following information of the game in one line serperated by commas: (Game Name, genre, synopsis, download size, Price, picture link)\n")
  
  userInformation = userInformation.split(',')
  for x in userInformation:

    x = x.strip()
  
  userInformation.insert(0, studioId)

  sql = "INSERT INTO games (studioID, gameName, genre, synopsis, downloadSize, price, picture) VALUES ( %s, %s, %s, %s, %s, %s, %s)"
  values = userInformation
  
  
  mycursor.execute(sql, values)
  mydb.commit()
  print("Your game has been added to the database.")




typeOfUser = input("""Who are you(Enter a number):
1: User
2: Game Company\n""")
while (typeOfUser != '1' and typeOfUser != '2'):
  typeOfUser = input("""Error with choice! Try Again.
   Enter a number:
    1: User
    2: Game Company\n""")
if typeOfUser == '1':
  user()
elif typeOfUser == '2':
  gameCompany()



