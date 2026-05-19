# src/models/databaseModel.py

import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

load_dotenv()

class Database:

    @staticmethod
    def get_connection():
        host = os.getenv("DB_HOST", "localhost")
        user = os.getenv("DB_USER", "root")
        password = os.getenv("DB_PASSWORD", "")
        database = os.getenv("DB_NAME", "tienda_videojuegos")

        try:
            return mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                fallback_conn = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password
                )
                fallback_cursor = fallback_conn.cursor()
                fallback_cursor.execute(
                    f"CREATE DATABASE IF NOT EXISTS `{database}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
                )
                fallback_cursor.close()
                fallback_conn.close()
                return mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
            raise