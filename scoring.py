import json


# ============================================================
# 1. LOAD MERGED DATA
# ============================================================

def load_merged_data(file_path):

    with open(file_path, "r") as file:
        data = json.load(file)

    return data


# ============================================================
# 2. FIND USER
# ============================================================

def get_user(data, user_id):

    for user in data:

        if user["user_id"] == user_id:
            return user

    raise ValueError(f"User {user_id} not found")


# ============================================================
# 3. RULE-BASED CREDIT SCORE
# ============================================================

def calculate_score(user):

    score = 0

    breakdown = {}

    # ========================================================
    # LIFESTYLE
    # ========================================================

    # --------------------------------------------------------
    # 1.1 Employment Stability
    # --------------------------------------------------------

    months_at_job = user["months_at_job"]

    if months_at_job >= 24:
        employment_score = 150

    elif months_at_job >= 12:
        employment_score = 100

    elif months_at_job >= 6:
        employment_score = 50

    else:
        employment_score = 0

    score += employment_score

    breakdown["employment_stability"] = employment_score


    # --------------------------------------------------------
    # 1.2 Housing Status
    # --------------------------------------------------------

    housing = user["housing"].lower()

    rent_on_time_months = user["rent_on_time_months"]

    if housing == "own":
        housing_score = 80

    elif housing == "rent" and rent_on_time_months >= 12:
        housing_score = 60

    elif housing == "rent" and rent_on_time_months < 12:
        housing_score = 30

    else:
        housing_score = 0

    score += housing_score

    breakdown["housing_status"] = housing_score


    # --------------------------------------------------------
    # 1.3 Digital Footprint
    # --------------------------------------------------------

    digital_rate = user["digital_payment_rate"] * 100

    if digital_rate >= 95:
        digital_score = 70

    elif digital_rate >= 80:
        digital_score = 45

    elif digital_rate >= 60:
        digital_score = 20

    else:
        digital_score = 0

    score += digital_score

    breakdown["digital_footprint"] = digital_score


    # --------------------------------------------------------
    # 1.4 Education / Skill
    # --------------------------------------------------------

    education = user["education"].lower()

    if education in ["master", "master's", "phd", "doctorate"]:
        education_score = 50

    elif education in ["bachelor", "bachelor's"]:
        education_score = 40

    elif education == "professional":
        education_score = 30

    elif education == "high school":
        education_score = 20

    else:
        education_score = 0

    score += education_score

    breakdown["education_skill"] = education_score


    # ========================================================
    # SPENDING BEHAVIOR
    # ========================================================

    # --------------------------------------------------------
    # 2.1 Spend-to-Income Ratio
    # --------------------------------------------------------

    monthly_income = user["monthly_income"]
    monthly_spend = user["monthly_spend"]

    if monthly_income > 0:

        spend_income_ratio = (
            monthly_spend / monthly_income
        ) * 100

    else:
        spend_income_ratio = 0


    if spend_income_ratio <= 30:
        spending_score = 120

    elif spend_income_ratio <= 50:
        spending_score = 80

    elif spend_income_ratio <= 70:
        spending_score = 40

    else:
        spending_score = 0

    score += spending_score

    breakdown["spend_to_income"] = spending_score


    # --------------------------------------------------------
    # 2.2 Expense Diversity
    # --------------------------------------------------------

    essential_percentage = user["essential_pct"] * 100

    if essential_percentage >= 70:
        diversity_score = 80

    elif essential_percentage >= 55:
        diversity_score = 45

    elif essential_percentage >= 40:
        diversity_score = 20

    else:
        diversity_score = 0

    score += diversity_score

    breakdown["expense_diversity"] = diversity_score


    # --------------------------------------------------------
    # 2.3 Cash-flow Volatility
    # --------------------------------------------------------

    volatility = user["cashflow_volatility"] * 100

    if volatility <= 5:
        volatility_score = 70

    elif volatility <= 10:
        volatility_score = 40

    elif volatility <= 20:
        volatility_score = 15

    else:
        volatility_score = 0

    score += volatility_score

    breakdown["cash_flow_volatility"] = volatility_score


    # --------------------------------------------------------
    # 2.4 Savings / Emergency Fund
    # --------------------------------------------------------

    savings_days = user["savings_days"]

    if savings_days >= 180:
        savings_score = 80

    elif savings_days >= 90:
        savings_score = 50

    elif savings_days >= 30:
        savings_score = 20

    else:
        savings_score = 0

    score += savings_score

    breakdown["savings_emergency_fund"] = savings_score


    # ========================================================
    # REPAYMENT DISCIPLINE
    # ========================================================

    # --------------------------------------------------------
    # 3.1 On-time Payment Rate
    # --------------------------------------------------------

    on_time_rate = user["on_time_rate"] * 100

    if on_time_rate >= 98:
        payment_score = 200

    elif on_time_rate >= 95:
        payment_score = 150

    elif on_time_rate >= 90:
        payment_score = 100

    elif on_time_rate >= 80:
        payment_score = 50

    else:
        payment_score = 0

    score += payment_score

    breakdown["on_time_payment"] = payment_score


    # --------------------------------------------------------
    # 3.2 Debt-to-Income Ratio
    # --------------------------------------------------------

    dti = user["dti"] * 100

    if dti <= 20:
        dti_score = 120

    elif dti <= 35:
        dti_score = 80

    elif dti <= 50:
        dti_score = 40

    else:
        dti_score = 0

    score += dti_score

    breakdown["debt_to_income"] = dti_score


    # --------------------------------------------------------
    # 3.3 Credit Utilization
    # --------------------------------------------------------

    credit_util = user["credit_util"] * 100

    if credit_util <= 10:
        utilization_score = 100

    elif credit_util <= 30:
        utilization_score = 70

    elif credit_util <= 50:
        utilization_score = 30

    else:
        utilization_score = 0

    score += utilization_score

    breakdown["credit_utilization"] = utilization_score


    # --------------------------------------------------------
    # 3.4 Recent Delinquency Severity
    # --------------------------------------------------------

    delinq_90 = user["delinq_90plus"]
    delinq_60 = user["delinq_60plus"]
    delinq_30 = user["delinq_30plus"]

    if delinq_90 > 0:
        delinquency_score = 0

    elif delinq_60 > 0:
        delinquency_score = 50

    elif delinq_30 > 0:
        delinquency_score = 100

    else:
        delinquency_score = 150

    score += delinquency_score

    breakdown["delinquency"] = delinquency_score


    # ========================================================
    # BONUS / PENALTY
    # ========================================================

    # --------------------------------------------------------
    # 4.1 Positive Financial Behavior
    # --------------------------------------------------------

    positive_habits = user["positive_habits"]

    bonus_score = min(
        positive_habits * 20,
        50
    )

    score += bonus_score

    breakdown["positive_behavior_bonus"] = bonus_score


    # --------------------------------------------------------
    # 4.2 Risk Flags
    # --------------------------------------------------------

    risk_flags = user["risk_flags"]

    penalty_score = min(
        risk_flags * 20,
        50
    )

    score -= penalty_score

    breakdown["risk_penalty"] = penalty_score


    # ========================================================
    # FINAL SCORE
    # ========================================================

    final_score = max(
        0,
        min(score, 1000)
    )

    return final_score, breakdown


# ============================================================
# 4. TEST
# ============================================================

if __name__ == "__main__":

    data = load_merged_data(
        "data/merged_data.json"
    )

    user_id = "USR_001"

    user = get_user(
        data,
        user_id
    )

    final_score, breakdown = calculate_score(
        user
    )

    print("\n========================================")
    print("      NEW-AGE CREDIT SCORE")
    print("========================================")

    print(f"\nUser ID: {user_id}")

    print("\nScore Breakdown:")

    for factor, points in breakdown.items():

        print(
            f"{factor:<30} {points:>4}"
        )

    print("\n----------------------------------------")

    print(
        f"FINAL CREDIT SCORE: {final_score}/1000"
    )

    print("----------------------------------------")