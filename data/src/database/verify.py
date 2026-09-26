from connection import get_connection


def verify_database():

    connection = get_connection()
    cursor = connection.cursor()

    print("\n📊 DATABASE VERIFICATION\n")

    # Count applicants
    cursor.execute(
        "SELECT COUNT(*) FROM applicants"
    )
    applicants = cursor.fetchone()[0]

    # Count transactions
    cursor.execute(
        "SELECT COUNT(*) FROM transactions"
    )
    transactions = cursor.fetchone()[0]

    # Count products
    cursor.execute(
        "SELECT COUNT(*) FROM products"
    )
    products = cursor.fetchone()[0]

    print(f"Applicants     : {applicants}")
    print(f"Transactions   : {transactions}")
    print(f"Products       : {products}")

    # Foreign key check
    cursor.execute(
        "PRAGMA foreign_key_check"
    )

    foreign_key_errors = cursor.fetchall()

    if foreign_key_errors:
        print(
            f"\n❌ Foreign key errors: "
            f"{foreign_key_errors}"
        )
    else:
        print("\n✅ Foreign key integrity passed")

    # Sample applicant
    cursor.execute("""
        SELECT applicant_id, user_id, monthly_income
        FROM applicants
        LIMIT 1
    """)

    print("\nSample applicant:")
    print(cursor.fetchone())

    # Sample transaction
    cursor.execute("""
        SELECT transaction_id, applicant_id, amount
        FROM transactions
        LIMIT 1
    """)

    print("\nSample transaction:")
    print(cursor.fetchone())

    # Sample product
    cursor.execute("""
        SELECT product_id, product_name, interest_rate
        FROM products
        LIMIT 1
    """)

    print("\nSample product:")
    print(cursor.fetchone())

    connection.close()


if __name__ == "__main__":
    verify_database()