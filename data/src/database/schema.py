from connection import get_connection


def create_tables():

    connection = get_connection()
    cursor = connection.cursor()

    # Applicants table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applicants (
            applicant_id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            age INTEGER,
            education_level TEXT,
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
            risk_flags INTEGER
        )
    """)

    # Transactions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            date TEXT,
            amount REAL,
            category TEXT,
            type TEXT,
            status TEXT,
            applicant_id TEXT NOT NULL,

            FOREIGN KEY (applicant_id)
                REFERENCES applicants(applicant_id)
        )
    """)

    # Products table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,
            product_name TEXT NOT NULL,
            min_score REAL,
            type TEXT,
            interest_rate REAL
        )
    """)

    connection.commit()
    connection.close()

    print("✅ Database tables created successfully")