import sqlite3
script = open("quiz.sql",'r')
script = script.read()
connection = sqlite3.connect('./quiz.db')
cursor_object = connection.cursor()
cursor_object.executescript(script)