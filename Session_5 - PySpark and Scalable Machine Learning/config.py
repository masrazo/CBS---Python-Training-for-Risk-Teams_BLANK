"""
Dataset locations and loading helpers for Session 5 (PySpark and Scalable Machine Learning).

During the session the data is read from the PUBLIC S3 bucket. Every dataset has one
relative path (`DATASETS` below); the path dicts are derived from it so they never
drift out of sync:

    session_datasets       S3 URIs for Spark          spark.read.csv(session_datasets["train_titanic"], ...)
    session_datasets_http  HTTPS URLs for pandas      pd.read_csv(session_datasets_http["train_titanic"])
    local_datasets         repo-root datasets/ copy   (trainer use only, not in the notebooks)

The repo-root `datasets/` folder mirrors the bucket layout, so the same relative path works
for all three.

Typical use in a notebook:

    from config import session_datasets, pandas_bridge

    # Default (the "pandas bridge"): pandas downloads over HTTPS, Spark takes the result
    df = pandas_bridge(spark, "train_titanic")

    # Alternative: Spark reads straight from S3 (needs S3 access on the compute)
    # df = spark.read.csv(session_datasets["train_titanic"], header=True, inferSchema=True)

Why the pandas bridge is the default: many clusters cannot read the bucket with
`spark.read` (missing S3 credentials/permissions, or serverless/shared compute that blocks
direct S3 access). pandas only needs HTTPS, which always works for a public bucket. The
trade-off: pandas loads the whole file into the driver's memory first, so it is only
suitable for small and medium files like the training datasets, never for real big data.

On Databricks, keep this file in the same folder as the notebook (or a Repo on the Python
path), or load it with:  %run ./config

All files sit on a PUBLIC bucket, so this file holds no secrets and is safe to share.
NOTE: trainer-only files are intentionally NOT listed here.
"""

# --- One place to change the bucket, region or prefix ---
_HTTPS_ROOT = "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/"
_S3_ROOT    = "s3://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/"
# Note: open-source Spark (not Databricks) needs the "s3a://" scheme plus the hadoop-aws package.
_LOCAL_ROOT = "../../datasets/"   # relative to a notebook inside a Session 5 topic folder

# Single source of truth: short name -> {file (relative to the roots above), description}
DATASETS = {
    # --- PySpark fundamentals and data wrangling ---
    "train_titanic": {
        "file": "Session_5/train_titanic.csv",
        "description": "Titanic passengers with the survival label (Kaggle training set).",
    },
    "test_titanic": {
        "file": "Session_5/test_titanic.csv",
        "description": "Titanic passengers without the survival label (Kaggle test set).",
    },
    # The pandas walkthrough data (Session 2), reused by the PySpark walkthrough (notebook 01.03)
    "customer": {
        "file": "customer.csv",
        "description": "Pagila customers (599 rows): name, email, store_id, active flag.",
    },
    "payment": {
        "file": "payment.csv",
        "description": "Pagila payments, Jan-May 2007 (16,049 rows): customer_id, staff_id, amount, payment_date.",
    },
    "orders_2017": {
        "file": "orders_2017.csv",
        "description": "Superstore orders 2017. Column-name typos on purpose: dhip_date, country_segment.",
    },
    "orders_2018": {
        "file": "orders_2018.csv",
        "description": "Superstore orders 2018. Column-name typo on purpose: county_region.",
    },
    "orders_2019": {
        "file": "orders_2019.csv",
        "description": "Superstore orders 2019 (clean column names). Profit is text such as '$1,234.56'.",
    },
    "superstore": {
        "file": "superstore.csv",
        "description": "Superstore retail orders: one row per order line with sales, profit and region.",
    },
    "eu_sales": {
        "file": "eu_sales.csv",
        "description": "Expected result of the EU Sales practical: total paid per EU country (Pagila), 18 rows.",
    },
    "sales_reps": {
        "file": "sales_reps.csv",
        "description": "Sales representatives and the regions they cover (join examples).",
    },
    # Pagila DVD-rental database exported to CSV (the tables used in Session 2), for joins and unions
    "pagila_customer": {
        "file": "pagila_csv/customer.csv",
        "description": "Pagila customers: name, email, address_id, active flag.",
    },
    "pagila_address": {
        "file": "pagila_csv/address.csv",
        "description": "Pagila addresses: address, district, city_id, postal code.",
    },
    "pagila_city": {
        "file": "pagila_csv/city.csv",
        "description": "Pagila cities with their country_id.",
    },
    "pagila_country": {
        "file": "pagila_csv/country.csv",
        "description": "Pagila countries.",
    },
    "pagila_payment": {
        # One table split into 7 monthly files. Spark reads them all with the wildcard path;
        # the pandas bridge downloads each part and stacks them.
        "file": "pagila_csv/payment_p2022_0*.csv",
        "parts": [f"pagila_csv/payment_p2022_0{m}.csv" for m in range(1, 8)],
        "description": "Pagila payments Jan-Jul 2022 (7 monthly files): customer_id, amount, payment_date.",
    },
    # --- MLlib ---
    "cal_housing": {
        "file": "Session_5/cal_housing.data",
        "description": "California housing (1990 census), raw header-less file read with an explicit schema.",
    },
    "california_housing": {
        "file": "Session_5/california_housing.csv",
        "description": "California housing (1990 census), named-column version.",
    },
    "automobile": {
        "file": "Session_5/automobile.csv",
        "description": "1985 auto imports with specifications and price (regression practical).",
    },
    "german_credit": {
        "file": "Session_5/german_credit.csv",
        "description": "Statlog German Credit: 1,000 loan applicants labelled good/bad risk.",
    },
    "telco_churn": {
        "file": "Session_5/telco_churn.csv",
        "description": "Telco customer churn: account, services and monthly charges, churn Yes/No.",
    },
    # --- Capstone project data (attendee-facing: training + unseen validation sets) ---
    "credit_default_data": {
        "file": "Session_5/projects_datasets/credit_default_data.csv",
        "description": "Default of Credit Card Clients (Taiwan, 2005): training split with the 'default' target.",
    },
    "credit_default_unseen": {
        "file": "Session_5/projects_datasets/credit_default_unseen.csv",
        "description": "Default of Credit Card Clients: unseen validation split (target withheld).",
    },
    "brain_stroke_data": {
        "file": "Session_5/projects_datasets/brain_stroke_data.csv",
        "description": "Brain stroke risk factors with the stroke label (training split).",
    },
    "brain_stroke_unseen": {
        "file": "Session_5/projects_datasets/brain_stroke_unseen.csv",
        "description": "Brain stroke risk factors, unseen validation split (target withheld).",
    },
    "airplane_crashes_data": {
        "file": "Session_5/projects_datasets/airplane_crashes_data.csv",
        "description": "Airplane crashes (1908-2009) with fatalities (training split).",
    },
    "airplane_crashes_unseen": {
        "file": "Session_5/projects_datasets/airplane_crashes_unseen.csv",
        "description": "Airplane crashes, unseen validation split (Fatalities target withheld).",
    },
}

# Spark paths may contain a wildcard (Spark expands it); HTTPS cannot, so multi-file
# datasets get a LIST of URLs in session_datasets_http.
session_datasets      = {name: _S3_ROOT + meta["file"]    for name, meta in DATASETS.items()}
local_datasets        = {name: _LOCAL_ROOT + meta["file"] for name, meta in DATASETS.items()}
session_datasets_http = {
    name: [_HTTPS_ROOT + p for p in meta["parts"]] if "parts" in meta else _HTTPS_ROOT + meta["file"]
    for name, meta in DATASETS.items()
}


def pandas_bridge(spark, name, schema=None, **read_csv_kwargs):
    """Read a dataset with pandas over HTTPS and hand it to Spark as a DataFrame.

    This is the DEFAULT way the course notebooks load data: it only needs HTTPS, so it works on
    every Databricks compute (serverless included), even where Spark cannot read S3 directly.
    The alternative, `spark.read.csv(session_datasets[name], ...)`, is the big-data way and is
    shown commented out under each read.

    schema: optional, the same as `spark.read.csv(..., schema=...)`: a DDL string such as
        "id INT, amount DECIMAL(5,2)" or a StructType. Columns are matched BY POSITION, renamed
        and cast to the given types, so the result has exactly that schema.
    read_csv_kwargs: passed to pandas.read_csv (e.g. encoding="latin-1", index_col=0, header=None).

    pandas marks every missing value as NaN. In text columns that confuses Spark's type
    inference, so they become None before the hand-over; in numeric columns NaN is turned
    into a real null afterwards (Spark treats NaN as a value, not as missing).
    Multi-file datasets (e.g. "pagila_payment") are downloaded part by part and stacked.
    Fine for training-size files; real big data must be read by Spark itself, because here the
    whole file passes through the driver's memory.
    """
    import pandas as pd
    from pyspark.sql import functions as F

    urls = session_datasets_http[name]
    if isinstance(urls, list):
        pdf = pd.concat([pd.read_csv(u, **read_csv_kwargs) for u in urls], ignore_index=True)
    else:
        pdf = pd.read_csv(urls, **read_csv_kwargs)
    for col in pdf.columns:
        if not pd.api.types.is_numeric_dtype(pdf[col]):          # text columns (any pandas version)
            pdf[col] = pdf[col].astype(object).where(pdf[col].notna(), None)
    sdf = spark.createDataFrame(pdf)

    # Missing NUMBERS arrive from pandas as NaN, which Spark keeps as a value (isNull() is
    # False for NaN). Turn them into real nulls so the result matches a direct Spark read.
    for col, dtype in sdf.dtypes:
        if dtype in ("double", "float"):
            sdf = sdf.withColumn(col, F.when(F.isnan(F.col(col)), None).otherwise(F.col(col)))

    if schema is not None:
        if isinstance(schema, str):                               # DDL string -> StructType
            schema = spark.createDataFrame([], schema).schema
        if len(schema.fields) != len(sdf.columns):
            raise ValueError(f"schema has {len(schema.fields)} columns, the file has {len(sdf.columns)}")
        sdf = sdf.toDF(*[f.name for f in schema.fields]).select(
            [F.col(f.name).cast(f.dataType).alias(f.name) for f in schema.fields])
    return sdf
