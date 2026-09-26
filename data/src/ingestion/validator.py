def validate_mapping(mapping):
    required_fields = {
        "user_id",
        "applicant_id",
        "match_cost"
    }

    if not isinstance(mapping, list):
        raise ValueError("ID mapping data must be a list")

    for record in mapping:
        if not isinstance(record, dict):
            raise ValueError("Each ID mapping record must be a dictionary")

        missing = required_fields - set(record.keys())

        if missing:
            raise ValueError(
                f"ID mapping missing fields: {missing}"
            )

        if record["match_cost"] < 0:
            raise ValueError(
                f"Invalid match cost: {record['match_cost']}"
            )

    print("✅ ID mapping validation passed")


def validate_demographics(data):
    required_fields = {
        "user_id",
        "age",
        "education_level",
        "employment_status",
        "monthly_income",
        "city_tier",
        "applicant_id"
    }

    if not isinstance(data, list):
        raise ValueError("Demographic data must be a list")

    for record in data:
        if not isinstance(record, dict):
            raise ValueError(
                "Each demographic record must be a dictionary"
            )

        missing = required_fields - set(record.keys())

        if missing:
            raise ValueError(
                f"Demographic record missing fields: {missing}"
            )

        if record["age"] <= 0:
            raise ValueError(
                f"Invalid age: {record['age']}"
            )

        if record["monthly_income"] < 0:
            raise ValueError(
                f"Invalid income: {record['monthly_income']}"
            )

    print("✅ Demographic validation passed")


def validate_transactions(df):

    required_columns = {
        "transaction_id",
        "user_id",
        "date",
        "amount",
        "category",
        "type",
        "status",
        "applicant_id"
    }

    # Check required columns
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Transaction data missing columns: {missing}"
        )

    # Check duplicate transaction IDs
    if df["transaction_id"].duplicated().any():
        duplicates = df.loc[
            df["transaction_id"].duplicated(),
            "transaction_id"
        ].tolist()

        raise ValueError(
            f"Duplicate transaction IDs found: {duplicates}"
        )

    # Check missing values
    if df.isnull().any().any():
        missing_columns = df.columns[
            df.isnull().any()
        ].tolist()

        raise ValueError(
            f"Missing values found in columns: {missing_columns}"
        )

    # Check negative transaction amounts
    if (df["amount"] < 0).any():
        raise ValueError(
            "Negative transaction amounts found"
        )

    # Check transaction type
    valid_types = {"DEBIT", "CREDIT"}

    invalid_types = set(df["type"].unique()) - valid_types

    if invalid_types:
        raise ValueError(
            f"Invalid transaction types found: {invalid_types}"
        )

    print("✅ Transaction validation passed")


def validate_relationships(mapping, transactions):

    # Applicants available in ID mapping
    valid_applicants = {
        record["applicant_id"]
        for record in mapping
    }

    # Applicants present in transactions
    transaction_applicants = set(
        transactions["applicant_id"]
    )

    # Find transactions belonging to unknown applicants
    invalid = (
        transaction_applicants
        - valid_applicants
    )

    if invalid:
        raise ValueError(
            f"Unknown applicant IDs found: {invalid}"
        )

    print("✅ Relationship validation passed")