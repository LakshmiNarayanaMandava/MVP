from schema import create_tables
from connection import get_connection

from loader import (
    load_applicants,
    load_transactions,
    load_products
)


def clear_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS transactions")
    cursor.execute("DROP TABLE IF EXISTS applicants")
    cursor.execute("DROP TABLE IF EXISTS products")

    connection.commit()
    connection.close()

    print("🧹 Existing database data cleared")


if __name__ == "__main__":

    print("Creating database...")

    clear_database()

    create_tables()

    print("\nLoading data...\n")

    load_applicants()
    load_transactions()
    load_products()

    print("\n🎉 SQLite database setup completed!")