from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]
mycoll=mydb["dbtable"]

mylist = [
  {
    'id' : 1, 
    'author' : 'Arijit Gayen', 
    'title' : 'MySQL vs MongoDB', 
    'content': 'MySQL is a Structural DataBase Management System whereas MongoDB is a Non-Structural DataBase Management System.\nThis Website is using MongoDB.\n', 
    'date_posted' : 'October 17, 2020'
  },

  {
    'id' : 2, 
    'author' : 'Arijit Gayen', 
    'title' : 'Tableau', 
    'content': 'Tableau is a new Data Visualization software providing relevant information and insights from given Dataset.\n', 
    'date_posted' : 'October 15, 2020'
  },

  {
    'id' : 3, 
    'author' : 'Arijit Gayen', 
    'title' : 'NetworkX', 
    'content': 'NetworkX is a package in Python which deals with Graphs and their various Operations and Functions. They use Python Dictionaries and thus for large cases Time becaomes a constraint.\n', 
    'date_posted' : 'October 10, 2020'
  }
]

x = mycoll.insert_many(mylist)

