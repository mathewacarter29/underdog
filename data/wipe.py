"""
This script will wipe the database so it can be re-populated
"""

import psycopg2


def main():
    """
    This function connects to the database and wipes the underdog schema, clearing the database
    """
    try:
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="password",
            host="localhost",
            port=5432,
        )
        cursor = conn.cursor()
        wipe_query = """
            DROP SCHEMA underdog CASCADE;
        """
        cursor.execute(wipe_query)
        conn.commit()
        print("Successfully wiped...")
        conn.close()
        cursor.close()
    except psycopg2.OperationalError:
        print("Error creating database connection - ensure database is running")
    except psycopg2.DatabaseError:
        print("The database has already been wiped")


if __name__ == "__main__":
    main()
