"""
Dataset locations for Session 4 (Machine Learning with scikit-learn).

The files live under the S3 prefix "Session_5/" for historical reasons (this module was
Session 5 in Cohort 1). The prefix is a single constant below, so it can be changed in one place.

Instead of hard-coding URLs in every notebook, import the paths from here:

    # pandas (HTTPS)
    from config import session_datasets_http
    import pandas as pd
    df = pd.read_csv(session_datasets_http["boston"])

    # Spark (S3)
    from config import session_datasets
    sdf = spark.read.csv(session_datasets["telco_churn"], header=True, inferSchema=True)

`DATASETS` below is the single source of truth: one entry per dataset with its file
name (relative to the Session_5 prefix) and a one-line description. The two path dicts
(`session_datasets_http`, `session_datasets`) are derived from it, so they can never
drift out of sync. Full column-by-column data dictionaries live in
`Setup/dataset_catalog.md`.

All files sit on a PUBLIC bucket, so this file holds no secrets and is safe to share
and commit. (Keep any API keys or credentials in a separate, gitignored file.)

On Databricks, put this file somewhere importable (same folder as the notebook, or a
Repo on the Python path), or load it with:  %run ./config

NOTE: trainer-only files are intentionally NOT listed here.
"""

# --- One place to change the bucket, region, or session prefix ---
_HTTPS_BASE = "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/Session_5/"
_S3_BASE    = "s3://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/Session_5/"
# Note: on open-source Spark (not Databricks) use the "s3a://" scheme instead of "s3://".

# Single source of truth: short name -> {file, description}
DATASETS = {
    # --- core datasets ---
    "50_Startups": {
        "file": "50_Startups.csv",
        "description": "Profit of 50 startups vs R&D, admin and marketing spend by US state.",
    },
    "KNN_Project_Data": {
        "file": "KNN_Project_Data.csv",
        "description": "Anonymised numeric features with a binary TARGET CLASS (KNN teaching set).",
    },
    "Mall_Customers": {
        "file": "Mall_Customers.csv",
        "description": "Mall customers: age, annual income and spending score for segmentation.",
    },
    "Position_Salaries": {
        "file": "Position_Salaries.csv",
        "description": "Salary by job level (teaching set for non-linear regression).",
    },
    "Salary_Data": {
        "file": "Salary_Data.csv",
        "description": "Salary vs years of experience (simple regression teaching set).",
    },
    "automobile": {
        "file": "automobile.csv",
        "description": "1985 auto imports with specifications and price (cleaned/engineered copy).",
    },
    "boston": {
        "file": "boston.csv",
        "description": "Boston housing (1970): neighbourhood features and median home value. Contains the ethically problematic 'B' feature.",
    },
    "breast_cancer": {
        "file": "breast_cancer.csv",
        "description": "Breast Cancer Wisconsin (Diagnostic): cell-nucleus measurements, malignant/benign.",
    },
    "cal_housing": {
        "file": "cal_housing.data",
        "description": "California housing (1990 census), raw header-less file read with a schema in the Spark notebooks.",
    },
    "california_housing": {
        "file": "california_housing.csv",
        "description": "California housing (1990 census), named-column version.",
    },
    "diabetes": {
        "file": "diabetes.csv",
        "description": "Pima Indians Diabetes: diagnostic measurements with a diabetes outcome.",
    },
    "german_credit": {
        "file": "german_credit.csv",
        "description": "Statlog German Credit: 1,000 loan applicants labelled good/bad risk (decoded to readable labels).",
    },
    "iris_Random_Forest_Dataset": {
        "file": "iris_Random_Forest_Dataset.csv",
        "description": "Iris flowers: sepal/petal measurements for three species.",
    },
    "loan_data": {
        "file": "loan_data.csv",
        "description": "LendingClub loans: borrower features and whether the loan was not fully paid.",
    },
    "penguins": {
        "file": "penguins.csv",
        "description": "Palmer Penguins: body measurements for three penguin species.",
    },
    "postcodes_se": {
        "file": "postcodes_se.csv",
        "description": "UK South-East postcodes with town and latitude/longitude (travel-time clustering mini-project).",
    },
    "telco_churn": {
        "file": "telco_churn.csv",
        "description": "Telco customer churn: account, services and monthly charges, churn Yes/No.",
    },
    "test_titanic": {
        "file": "test_titanic.csv",
        "description": "Titanic passengers without the survival label (Kaggle test set).",
    },
    "tips": {
        "file": "tips.csv",
        "description": "Restaurant tips: bills and tips by party size, day and time.",
    },
    "train_titanic": {
        "file": "train_titanic.csv",
        "description": "Titanic passengers with the survival label (Kaggle training set).",
    },
    "visceral_fat": {
        "file": "visceral_fat.csv",
        "description": "Maternal health measurements incl. central (Armellini) visceral fat and pregnancy outcomes.",
    },
    "wine": {
        "file": "wine.csv",
        "description": "Wine recognition: chemical analysis of wines from three cultivars.",
    },
    # --- capstone project data (attendee-facing: training + unseen validation sets) ---
    "credit_default_data": {
        "file": "projects_datasets/credit_default_data.csv",
        "description": "Default of Credit Card Clients (Taiwan, 2005): training split with the 'default' target.",
    },
    "credit_default_unseen": {
        "file": "projects_datasets/credit_default_unseen.csv",
        "description": "Default of Credit Card Clients: unseen validation split (target withheld).",
    },
    "brain_stroke_data": {
        "file": "projects_datasets/brain_stroke_data.csv",
        "description": "Brain stroke risk factors with the stroke label (training split).",
    },
    "brain_stroke_unseen": {
        "file": "projects_datasets/brain_stroke_unseen.csv",
        "description": "Brain stroke risk factors, unseen validation split (target withheld).",
    },
    "airplane_crashes_data": {
        "file": "projects_datasets/airplane_crashes_data.csv",
        "description": "Airplane crashes (1908-2009) with fatalities (training split).",
    },
    "airplane_crashes_unseen": {
        "file": "projects_datasets/airplane_crashes_unseen.csv",
        "description": "Airplane crashes, unseen validation split (Fatalities target withheld).",
    },
}

# HTTPS URLs for pandas (pd.read_csv) and S3 URIs for Spark (spark.read.csv),
# both derived from DATASETS so they always stay in sync.
session_datasets_http = {name: _HTTPS_BASE + meta["file"] for name, meta in DATASETS.items()}
session_datasets      = {name: _S3_BASE + meta["file"]    for name, meta in DATASETS.items()}
