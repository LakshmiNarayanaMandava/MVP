from fastapi import FastAPI, HTTPException
from scoring import load_merged_data, get_user, calculate_score


# ============================================================
# CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="New-Age Credit Scoring API",
    description="Rule-based alternative credit scoring system",
    version="1.0.0"
)


# ============================================================
# LOAD DATA
# ============================================================

DATA_FILE = "data/merged_data.json"

data = load_merged_data(DATA_FILE)


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
def home():
    return {
        "message": "New-Age Credit Scoring API is running"
    }


# ============================================================
# CREDIT SCORE ENDPOINT
# ============================================================

@app.get("/score/{user_id}")
def get_credit_score(user_id: str):

    try:

        # Find user
        user = get_user(
            data,
            user_id
        )

        # Calculate score
        final_score, breakdown = calculate_score(
            user
        )

        # Return response
        return {
            "user_id": user_id,
            "credit_score": final_score,
            "breakdown": breakdown
        }

    except ValueError:

        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found"
        )