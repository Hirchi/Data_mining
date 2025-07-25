import csv
import sqlite3

# Connect to the database
conn = sqlite3.connect('formation.db')

# Create a table to store the courses
conn.execute('''CREATE TABLE courses
             (id INTEGER PRIMARY KEY,
              titre TEXT,
              description TEXT,
              prix TEXT,
              note TEXT,
              duree TEXT,
              modalite TEXT)''')

# Read the CSV files and insert the data into the courses table
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        conn.execute("INSERT INTO courses (titre, description, prix, note, duree, modalite) VALUES (?, ?, ?, ?, ?, ?)", row)

with open('data_Edu.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        conn.execute("INSERT INTO courses (titre, description, prix, note, duree, modalite) VALUES (?, ?, ?, ?, ?,'' )", row)
with open('data_demos.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        conn.execute("INSERT INTO courses (titre, description, prix, note, duree, modalite) VALUES (?, ?, ?, ?, ?, ?)", row)
# Commit the changes and close the connection
conn.commit()
conn.close()