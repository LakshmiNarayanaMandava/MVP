import json

from database import get_connection


JSON_FILE = "data/merged_data.json"


def import_users():

    # Read JSON file
    with open(JSON_FILE, "r") as file:
        users = json.load(file)

    connection = get_connection()
    cursor = connection.cursor()

    for user in users:

        cursor.execute("""
            INSERT OR REPLACE INTO users (
                user_id,
                age,
                education,
                employment_status,
                monthly_income,
                city_tier,
                months_at_job,
                housing,
                rent_on_time_months,
                digital_payment_rate,
                monthly_spend,
                essential_pct,
                cashflow_volatility,
                savings_days,
                on_time_rate,
                dti,
                credit_util,
                delinq_90plus,
                delinq_60plus,
                delinq_30plus,
                positive_habits,
                risk_flags,
                applicant_id
            )
            VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
        """, (
            user["user_id"],
            user["age"],
            user["education"],
            user["employment_status"],
            user["monthly_income"],
            user["city_tier"],
            user["months_at_job"],
            user["housing"],
            user["rent_on_time_months"],
            user["digital_payment_rate"],
            user["monthly_spend"],
            user["essential_pct"],
            user["cashflow_volatility"],
            user["savings_days"],
            user["on_time_rate"],
            user["dti"],
            user["credit_util"],
            user["delinq_90plus"],
            user["delinq_60plus"],
            user["delinq_30plus"],
            user["positive_habits"],
            user["risk_flags"],
            user["applicant_id"]
        ))

    connection.commit()
    connection.close()

    print(f"{len(users)} users imported successfully!")


if __name__ == "__main__":

    import_users()