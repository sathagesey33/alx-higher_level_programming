#!/usr/bin/python3

"""
Module: list_states_starting_with_N
Function: list_states_starting_with_N
Purpose: Connect to MySQL database and retrieve a distinct list of states whose
names start with an uppercase 'N' from the hbtn_0e_0_usa database
"""

import MySQLdb
import sys


def list_states_starting_with_N(
    mysql_username: str,
    mysql_password: str,
    database_name: str
) -> None:

    """
    Retrieve and display a distinct list of states whose names
    start with an uppercase 'N' from the specified database.

    Args:
        mysql_username: MySQL username (str)
        mysql_password: MySQL password (str)
        database_name: Database name (str)

    Returns:
        None
    """

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        cursor = db.cursor()

        query = "SELECT DISTINCT name FROM states WHERE name LIKE 'N%' ORDER BY name ASC;"
        cursor.execute(query)

        states = cursor.fetchall()

        for state in states:
            print(state[0])  # Printing only the state name

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
               "Usage: python list_states_starting_with_N.py "
               "<mysql_username> <mysql_password> <database_name>"
             )

    else:
        list_states_starting_with_N(sys.argv[1], sys.argv[2], sys.argv[3])
