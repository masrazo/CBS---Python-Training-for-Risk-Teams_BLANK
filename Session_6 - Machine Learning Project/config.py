"""
Dataset locations and loading helpers for Session 6 (Machine Learning Project).

Same pattern as the Session 5 config: one relative path per dataset gives
    session_datasets       S3 URIs for Spark          spark.read.csv(session_datasets["credit_default_data"], ...)
    session_datasets_http  HTTPS URLs for pandas      pd.read_csv(session_datasets_http["credit_default_data"])
    local_datasets         repo-root datasets/ copy (trainer use only)
and pandas_bridge(spark, name) is the DEFAULT read in the notebooks (it only needs HTTPS);
spark.read.csv(session_datasets[...]) is the alternative where the compute can read S3.

The project files stay under the S3 prefix "Session_5/projects_datasets/" (historical: the projects were part
of the ML session in Cohort 1). Trainer-only files are intentionally NOT listed here.
"""

# --- One place to change the bucket, region or prefix ---
_HTTPS_ROOT = "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/"
_S3_ROOT    = "s3://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/"
# Note: open-source Spark (not Databricks) needs the "s3a://" scheme plus the hadoop-aws package.
_LOCAL_ROOT = "../../datasets/"   # relative to a notebook inside a Session 6 project folder

# Single source of truth: short name -> {file (relative to the roots above), description}
DATASETS = {
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
    "telco_churn": {
        "file": "Session_5/telco_churn.csv",
        "description": "Telco customer churn: account, services and monthly charges, churn Yes/No.",
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
