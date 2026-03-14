import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

dbname = os.getenv("MAIL_DB_NAME", "mail")
user = os.getenv("MAIL_DB_USER", "postgres")
password = os.getenv("MAIL_DB_PASSWORD", "")
host = os.getenv("MAIL_DB_HOST", "localhost")
port = os.getenv("MAIL_DB_PORT", "5432")

# Specify the table name you want to read from
def get_events():
    table_name = "event"

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )

    # Create a cursor
    cursor = conn.cursor()

    # Construct and execute a SQL query to select data from the table
    query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Print the fetched data
    events = []
    count = 0
    for my_tuple in rows:
        if count == 20:
            break
        result_dict = {
        "Event": my_tuple[1],
        "Time": my_tuple[3] +"-"+ my_tuple[2]
        }
        events.append(result_dict)
        count += 1
    cursor.close()
    conn.close()
    return events

# Close the cursor and connection
# print(json.dumps(events))

def get_mails():
    table_name = "mail"

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )

    # Create a cursor
    cursor = conn.cursor()

    # Construct and execute a SQL query to select data from the table
    query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Print the fetched data
    emails = []
    count = 0
    for my_tuple in rows:
        if count == 40:
            break
        result_dict = {
        "from": my_tuple[2],
        "time": my_tuple[5],
        "subject": my_tuple[4],
        "message": my_tuple[6]
        }
        emails.append(result_dict)
        count += 1
    cursor.close()
    conn.close()
    return emails

get_mails()
