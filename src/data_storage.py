import psycopg2
import logging
from psycopg2 import Error
import os

db_host = os.environ['DB_HOST']
db_name = os.environ['DB_NAME']
db_user = os.environ['DB_USER'] 
db_pass = os.environ['DB_PASS']

logger = logging.getLogger(__name__) 

def create_connection():
  # Setup database connection
  conn = psycopg2.connect(
   database=db_name,
   user=db_user,
   password=db_pass,
   host=db_host,
   port='5432' 
)
  return conn

def create_tables(conn):
  
  try:
    cur = conn.cursor()

    # Create table if not exists
    cur.execute('''CREATE TABLE IF NOT EXISTS Sales (
                        sale_id SERIAL PRIMARY KEY,
                        customer_id INTEGER,
                        product_id INTEGER,
                        sale_amount REAL,
                        sale_date TIMESTAMP,
                        name TEXT,
                        username TEXT,
                        email TEXT,
                        lat REAL,
                        lng REAL,
                        temperature REAL,
                        weather_conditions TEXT
                    )''')

    
  except (Exception, psycopg2.DatabaseError) as error:
    logger.error(error)
    
  finally:
    cur.close()
    
def main():
  
  conn = create_connection()
  
  create_tables(conn)
  
  #load_data(conn)

  conn.close()
  
if __name__ == '__main__':
    main()