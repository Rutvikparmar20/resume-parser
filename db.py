import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="resumedb",
        user="postgres",
        password="123456"
    )
