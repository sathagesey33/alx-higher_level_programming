#!/usr/bin/python3

"""
Module: list_states
Function: list_states
Purpose: Connect to MySQL database and retrieve a list of states from the hbtn_0e_0_usa database, sorted by ID
"""

import MySQLdb
import sys


def list_states(mysql_username: str, mysql_password: str, database_name: str) -> None:
    """
    Retrieve and display a list of states sorted by ID from the specified database.

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

        query = "SELECT * FROM states ORDER BY id ASC;"
        cursor.execute(query)

        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python list_states.py <mysql_username> <mysql_password> <database_name>")
    else:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
