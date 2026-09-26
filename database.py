import sqlite3

DATABASE_NAME = "credit_scoring.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


# -----------------------------
# USERS TABLE
# -----------------------------
def create_users_table():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            age INTEGER,
            education TEXT,
            employment_status TEXT,
            monthly_income REAL,
            city_tier INTEGER,
            months_at_job INTEGER,
            housing TEXT,
            rent_on_time_months INTEGER,
            digital_payment_rate REAL,
            monthly_spend REAL,
            essential_pct REAL,
            cashflow_volatility REAL,
            savings_days INTEGER,
            on_time_rate REAL,
            dti REAL,
            credit_util REAL,
            delinq_90plus INTEGER,
            delinq_60plus INTEGER,
            delinq_30plus INTEGER,
            positive_habits INTEGER,
            risk_flags INTEGER,
            applicant_id TEXT
        )
    """)

    connection.commit()
    connection.close()


# -----------------------------
# GET USER
# -----------------------------
def get_user(user_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE user_id = ?",
        (user_id,)
    )

    user = cursor.fetchone()

    connection.close()

    if user:
        return dict(user)

    return None


# -----------------------------
# SCORES TABLE
# -----------------------------
def create_scores_table():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            credit_score INTEGER,
            breakdown TEXT
        )
    """)

    connection.commit()
    connection.close()


# -----------------------------
# SAVE SCORE
# -----------------------------
def save_score(user_id, credit_score, breakdown):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO scores (
            user_id,
            credit_score,
            breakdown
        )
        VALUES (?, ?, ?)
    """, (
        user_id,
        credit_score,
        str(breakdown)
    ))

    connection.commit()
    connection.close()


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    create_users_table()
    create_scores_table()

    print("Database tables created successfully.")

    user = get_user("USR_001")

    if user:
        print("User found:")
        print(user)
    else:
        print("User not found")