 # Importing the mariadb module
import mariadb
# Importing the dbcreds module for connection parameters
import dbcreds
# created a function that takes two arguments , the sql  argument represents the SQL query that  we want to execute and  args  for arguments  that we want to pass to the SQL query.
def run_procedure(sql, args):
        try:
            results = None  # Created a Variable to store the query results
            # Establishing a connection to the database using the connection parameters
            conn = mariadb.connect(**dbcreds.conn_params)
            # Creating a cursor object to execute SQL queries
            cursor = conn.cursor()
            # Executing the SQL query with the provided arguments
            cursor.execute(sql, args)
             # Fetching all the results from the executed query
            results = cursor.fetchall()
            # Handling a programming error in the database code
        except mariadb.ProgrammingError as error:
            print('There is an issue with the DB code:', error)
            # Handling an error while connecting to the database
        except mariadb.OperationalError as error:
            print('There is an issue connecting to the DB:', error)
            # Handling any other unknown error
        except Exception as error:
            print('There was an unknown error:', error)
        finally:
            if(cursor != None):
            # Closing the cursor
             cursor.close()
        if(conn != None):
            # Closing the database connection
            conn.close()
             # Returning the query results
        return results
