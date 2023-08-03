import pymysql.cursors
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DbManager:

    def __init__(self):
        self.connection()

    def execute(self, sql_query):

        # Connect to the database
        connection = pymysql.connect(host='127.0.0.1',
                                    port = 33061,
                                    user='root',
                                    password='root',
                                    database='homestead',
                                    cursorclass=pymysql.cursors.DictCursor)

        with connection:
            # with connection.cursor() as cursor:
            #     # Create a new record

            #     # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"

            #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            # connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"

                cursor.execute(sql, ('webmaster@python.org',))

                result = cursor.fetchone()

                return result

    @staticmethod
    def connection():
        # Define the database connection
        database_url = "mysql://root:root@localhost/cjw_db"

        # Create the database engine
        engine = create_engine(database_url)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        # Declarar una clase base para tus modelos
        Base = declarative_base()

        return (SessionLocal, Base)