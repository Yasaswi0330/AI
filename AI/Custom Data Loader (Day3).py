# For loading data from API, Database

# before loading Data lets create database using SQLLITE , SQLLITE is for practice only , in real time we use

#  postgrelsql, mysql etc   pip install pysqlite3


# Custom Loader - Database loader

import sqlite3

def setup_crm_database():
    conn = sqlite3. connect('crm.db')
    cursor = conn.cursor()

    cursor. execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,                 
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone_number TEXT,
        address TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """ )


    customers = [
        ("Priya", "Sharma", "priya. sharma@example. com", "9123456780", "456 Park Avenue"),
        ("Amit", I'Verma", "amit.verma@example.com", "9988776655", "789 Elm Street"),
        ("Neha", "Reddy", "neha. reddy@example.com", "9871234560", "12 Sunset Boulevard")
    ]


    cursor. executemany("""
        INSERT INTO customers (first_name, last_name, email, phone_number, address)
        VALUES (?, ?, ?, ?, ?)
        """
        , customers)

    conn.commit()
    conn.close()

setup_crm_database()


  # loading data 

from langchain_core.documents import Document

from langchain_community.document_loaders.base import BaseLoader

class CRMCustomerLoader(BaseLoader):
    
    def _init_(self, db_path, query):
    self.db_path = db_path
    self.query = query

    def load(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn. cursor()

        cursor.execute(self.query)

        rows = cursor. fetchall()

        print (rows)

        conn.close()

loader = CRMCustomerLoader(
    db_path='crm.db',
    query .= 'SELECT .* FROM customers'
)

loader. load()



--------## Example 2 ##-----------
import sqlite3

# Step 1: Setup a simple pets database
def setup_pets_database():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL
        )
    """)
    
    pets = [
        ("Bella", "Dog"),
        ("Milo", "Cat"),
        ("Charlie", "Bird")
    ]
    
    cursor.executemany("""
        INSERT INTO pets (name, type)
        VALUES (?, ?)
    """, pets)

    conn.commit()
    conn.close()

setup_pets_database()

# Step 2: Simple function to load and print pets
def load_and_print_pets():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM pets')
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    conn.close()

# Run the function to print pets
load_and_print_pets()





-------## loading document using API ##-------

# API response EXAMPLE:
# [
#   {
#     "userId": 1,
#     "id": 1,
#     "title": "my title",
#     "body": "my post content"
#   }
# ]

import requests
from langchain_core.documents import Document


class APILoader:

    def load(self):

        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts"
        )

        posts = response.json()

        docs = []

        for post in posts:

            docs.append(
                Document(
                    page_content=post["body"],
                    metadata={
                        "title": post["title"]
                    }
                )
            )

        return docs


loader = APILoader()

documents = loader.load()

print(documents[0].page_content)
print(documents[0].metadata)




