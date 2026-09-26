from fastapi import FastAPI, HTTPException

from database import get_user, save_score, create_scores_table
from scoring import calculate_score


app = FastAPI(
    title="New-Age Credit Scoring API",
    description="Rule-based alternative credit scoring system",
    version="1.0.0"
)


# Create scores table when API starts
create_scores_table()


@app.get("/")
def home():

    return {
        "message": "New-Age Credit Scoring API is running"
    }


@app.get("/score/{user_id}")
def get_credit_score(user_id: str):

    # 1. Get user from database
    user = get_user(user_id)

    # 2. Check whether user exists
    if user is None:

        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found"
        )

    # 3. Calculate credit score
    final_score, breakdown = calculate_score(user)

    # 4. Store score in database
    save_score(
        user_id,
        final_score,
        breakdown
    )

    # 5. Return response
    return {
        "user_id": user_id,
        "credit_score": final_score,
        "breakdown": breakdown,
        "message": "Score calculated and stored successfully"
    }