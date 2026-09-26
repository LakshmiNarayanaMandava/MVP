import pandas as pd
import re

def transform_transactions(df):
    df = df.copy()

    # Convert date to datetime
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    # Clean text columns
    df["category"] = (
        df["category"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    df["type"] = (
        df["type"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    df["status"] = (
        df["status"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    # Ensure amount is numeric
    df["amount"] = pd.to_numeric(
        df["amount"],
        errors="coerce"
    )

    return df


def save_processed_transactions(df, output_path):

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"✅ Processed transactions saved to: {output_path}"
    )
def transform_applicants(data):

    records = []

    for record in data:

        applicant = {
            "applicant_id": record["applicant_id"],
            "user_id": record["user_id"],
            "age": int(record["age"]),
            "education_level": str(
                record["education_level"]
            ).strip(),
            "employment_status": str(
                record["employment_status"]
            ).strip(),
            "monthly_income": float(
                record["monthly_income"]
            ),
            "city_tier": int(
                record["city_tier"]
            ),
            "months_at_job": int(
                record["months_at_job"]
            ),
            "housing": str(
                record["housing"]
            ).strip(),
            "rent_on_time_months": int(
                record["rent_on_time_months"]
            ),
            "digital_payment_rate": float(
                record["digital_payment_rate"]
            ),
            "monthly_spend": float(
                record["monthly_spend"]
            ),
            "essential_pct": float(
                record["essential_pct"]
            ),
            "cashflow_volatility": float(
                record["cashflow_volatility"]
            ),
            "savings_days": int(
                record["savings_days"]
            ),
            "on_time_rate": float(
                record["on_time_rate"]
            ),
            "dti": float(
                record["dti"]
            ),
            "credit_util": float(
                record["credit_util"]
            ),
            "delinq_90plus": int(
                record["delinq_90plus"]
            ),
            "delinq_60plus": int(
                record["delinq_60plus"]
            ),
            "delinq_30plus": int(
                record["delinq_30plus"]
            ),
            "positive_habits": int(
                record["positive_habits"]
            ),
            "risk_flags": int(
                record["risk_flags"]
            )
        }

        records.append(applicant)

    return records
def save_applicants(data, output_path):

    df = pd.DataFrame(data)

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"✅ Applicants saved to: {output_path}"
    )
def transform_products(data):

    records = []

    for record in data:

        # Extract numeric interest rate
        # Examples:
        # "12% APR"  -> 12.0
        # "17.00 PA" -> 17.0
        # "15% PA"   -> 15.0
        rate_text = str(record["interest_rate"])

        match = re.search(
            r"\d+(?:\.\d+)?",
            rate_text
        )

        if not match:
            raise ValueError(
                f"Invalid interest rate: {rate_text}"
            )

        interest_rate = float(match.group())

        product = {
            "product_id": record["product_id"],

            "product_name": str(
                record["product_name"]
            ).strip(),

            "min_score": float(
                record["min_score"]
            ),

            "type": str(
                record["type"]
            ).strip(),

            "interest_rate": interest_rate
        }

        records.append(product)

    return records

def save_products(data, output_path):

    df = pd.DataFrame(data)

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"✅ Products saved to: {output_path}"
    )