from reader import read_json, read_csv
from validator import (
    validate_mapping,
    validate_demographics,
    validate_transactions,
    validate_relationships
)
from reader import read_json, read_csv

from validator import (
    validate_mapping,
    validate_demographics,
    validate_transactions,
    validate_relationships
)
from transformer import (
    transform_transactions,
    save_processed_transactions,
    transform_applicants,
    save_applicants,
    transform_products,
    save_products
)
DATA_DIR = "raw"


def load_data():

    id_mapping = read_json(
        f"{DATA_DIR}/id_mapping.json"
    )

    demographic_data = read_json(
        f"{DATA_DIR}/demographic_data.json"
    )

    product_catalog = read_json(
        f"{DATA_DIR}/product_catalog.json"
    )

    merged_data = read_json(
        f"{DATA_DIR}/merged_data.json"
    )

    new_age_data = read_json(
        f"{DATA_DIR}/new_age_sample_data.json"
    )

    transactions = read_csv(
        f"{DATA_DIR}/transactional_data.csv"
    )

    return {
        "id_mapping": id_mapping,
        "demographic": demographic_data,
        "products": product_catalog,
        "merged": merged_data,
        "new_age": new_age_data,
        "transactions": transactions
    }


if __name__ == "__main__":

    data = load_data()

    print("Data ingestion successful!")

    for name, value in data.items():

        if hasattr(value, "shape"):
            print(name, value.shape)

        else:
            print(name, len(value))

    print("\nStarting validation...\n")

    validate_mapping(
        data["id_mapping"]
    )

    validate_demographics(
        data["demographic"]
    )

    validate_transactions(
        data["transactions"]
    )

    validate_relationships(
        data["id_mapping"],
        data["transactions"]
    )

    print("\n🎉 ALL VALIDATIONS PASSED!")
    print("\nStarting transformation...")

data["transactions"] = transform_transactions(
    data["transactions"]
)

print("✅ Transaction transformation completed")

print("\nTransformed transaction data:")
print(data["transactions"].head())
save_processed_transactions(
    data["transactions"],
    "processed/transactions.csv"
)
print("\nStarting applicant transformation...")

data["demographic"] = transform_applicants(
    data["merged"]
)

save_applicants(
    data["demographic"],
    "processed/applicants.csv"
)
print("\nStarting product transformation...")

data["products"] = transform_products(
    data["products"]
)

save_products(
    data["products"],
    "processed/products.csv"
)