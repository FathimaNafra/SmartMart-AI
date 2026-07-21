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


def main():
    # ==========================
    # Step 1: Load Data
    # ==========================
    train = load_train_data()
    store = load_store_data()
    test = load_test_data()

    print("\n✅ Data loaded successfully!\n")

    # ==========================
    # Step 2: Validate Data
    # ==========================
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

    # ==========================
    # Step 3: Clean Data
    # ==========================
    print("\n🧹 Cleaning datasets...\n")

    train = clean_train_data(train)
    store = clean_store_data(store)
    test = clean_test_data(test)

    print("✅ Data cleaning completed!\n")

    # ==========================
    # Step 4: Display Summary
    # ==========================
    print("========== Cleaned Dataset Summary ==========")

    print(f"Train Shape : {train.shape}")
    print(f"Store Shape : {store.shape}")
    print(f"Test Shape  : {test.shape}")

    print("\nTrain Data Types:")
    print(train.dtypes.head())

    print("\nStore Missing Values:")
    print(store.isnull().sum()[store.isnull().sum() > 0])

    print("\nTest Missing Values:")
    print(test.isnull().sum()[test.isnull().sum() > 0])

    print("\n🎉 ETL Pipeline (Load → Validate → Clean) completed successfully!")


if __name__ == "__main__":
    main()