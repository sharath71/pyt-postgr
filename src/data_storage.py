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
    # Execute CREATE TABLE statements
    cur.execute('''
        CREATE TABLE IF NOT EXISTS transformed_data (
        customer_id SERIAL PRIMARY KEY,
        order_date DATE,  
        product_id TEXT,
        sales INTEGER,
        temp NUMERIC,
        description TEXT,
        weather TEXT);''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS aggregated_data (
        customer_id PRIMARY KEY,
        total_sales INTEGER);''')
        conn.commit()
    
  except (Exception, psycopg2.DatabaseError) as error:
    logger.error(error)
    
  finally:
    cur.close()

def load_data(conn):

  sql = """INSERT INTO transformed_data 
            (date, product, sales, revenue) VALUES (%s, %s, %s, %s)"""
            
  try:  
    cur = conn.cursor()
    cur.execute(sql, (date, product, sales, revenue))
    conn.commit()
    
  except (Exception, psycopg2.DatabaseError) as error:
    logger.error(error)
  
  finally:
    cur.close()
    
def main():
  
  conn = create_connection()
  
  create_tables(conn)
  
  load_data(conn)

  conn.close()
  
if __name__ == '__main__':
    main()