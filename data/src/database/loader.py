import pandas as pd

from connection import get_connection


def load_applicants():

    df = pd.read_csv(
        "processed/applicants.csv"
    )

    connection = get_connection()

    df.to_sql(
        "applicants",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print(
        f"✅ Loaded {len(df)} applicants"
    )


def load_transactions():

    df = pd.read_csv(
        "processed/transactions.csv"
    )

    connection = get_connection()

    df.to_sql(
        "transactions",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print(
        f"✅ Loaded {len(df)} transactions"
    )


def load_products():

    df = pd.read_csv(
        "processed/products.csv"
    )

    connection = get_connection()

    df.to_sql(
        "products",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print(
        f"✅ Loaded {len(df)} products"
    )