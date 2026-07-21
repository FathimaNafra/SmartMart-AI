from src.ingesion.load_data import (
    load_train_data,
    load_store_data,
    load_test_data,
)

from src.validation.validate_data import validate_dataset

from src.preprocessing.clean_data import (
    clean_train_data,
    clean_store_data,
    clean_test_data,
)

from src.transformation.transform_data import transform_data

from src.utils.save_data import save_processed_data
from src.aws.upload_to_s3 import upload_processed_data

def main():
    # ==================================================
    # Step 1: Load Data
    # ==================================================
    print("\n==============================")
    print("STEP 1: LOADING DATA")
    print("==============================")

    train = load_train_data()
    store = load_store_data()
    test = load_test_data()

    print("✅ Data loaded successfully!\n")

    # ==================================================
    # Step 2: Validate Data
    # ==================================================
    print("==============================")
    print("STEP 2: VALIDATING DATA")
    print("==============================")

    validate_dataset(
        train,
        "Train",
        [
            "Store",
            "Date",
            "Sales",
            "Customers",
        ],
    )

    validate_dataset(
        store,
        "Store",
        [
            "Store",
            "StoreType",
            "Assortment",
        ],
    )

    validate_dataset(
        test,
        "Test",
        [
            "Id",
            "Store",
            "Date",
        ],
    )

    # ==================================================
    # Step 3: Clean Data
    # ==================================================
    print("==============================")
    print("STEP 3: CLEANING DATA")
    print("==============================")

    train = clean_train_data(train)
    store = clean_store_data(store)
    test = clean_test_data(test)

    print("✅ Data cleaning completed!\n")

    # ==================================================
    # Step 4: Transform Data
    # ==================================================
    print("==============================")
    print("STEP 4: TRANSFORMING DATA")
    print("==============================")

    sales_data = transform_data(train, store)

    print("✅ Data transformation completed!\n")

    # ==================================================
    # Step 5: Save Processed Dataset
    # ==================================================
    print("==============================")
    print("STEP 5: SAVING DATA")
    print("==============================")

    save_processed_data(sales_data)
    print("\n☁️ Uploading dataset to AWS S3...\n")

    upload_processed_data()

    print("✅ Upload completed!\n")

    print("✅ Processed dataset saved!\n")

    # ==================================================
    # Step 6: Pipeline Summary
    # ==================================================
    print("==============================")
    print("ETL PIPELINE SUMMARY")
    print("==============================")

    print("✅ Data Loading        : Completed")
    print("✅ Data Validation     : Completed")
    print("✅ Data Cleaning       : Completed")
    print("✅ Data Transformation : Completed")
    print("✅ Data Export         : Completed")

    print("\n========== FINAL DATASET ==========")

    print(f"Rows    : {sales_data.shape[0]:,}")
    print(f"Columns : {sales_data.shape[1]}")

    print("\nFirst 10 Columns")
    print("-" * 40)
    print(sales_data.columns[:10].tolist())

    print("\nLast 10 Columns")
    print("-" * 40)
    print(sales_data.columns[-10:].tolist())

    print("\nData Types")
    print("-" * 40)
    print(sales_data.dtypes.head(10))

    print("\nRemaining Missing Values")
    print("-" * 40)

    missing = sales_data.isnull().sum()
    missing = missing[missing > 0]

    if missing.empty:
        print("No missing values remaining.")
    else:
        print(missing)

    print("\nSample Data")
    print("-" * 40)
    print(sales_data.head())

    print("\n🎉 ETL Pipeline completed successfully!")


if __name__ == "__main__":
    main()