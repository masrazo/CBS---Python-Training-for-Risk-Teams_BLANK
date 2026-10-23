#Configurations:

# HTTPS links (default): read with pandas, e.g. pd.read_csv(session_datasets["Salaries"])
session_datasets = {
    "Production.Product": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/Production.Product.csv",
    "Salaries": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/Salaries.csv",
    "train_titanic": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/train_titanic.csv",
    "superstore": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/superstore.csv"
}

# S3 links (Databricks/Spark only), e.g. spark.read.csv(session_datasets_s3["Salaries"], header=True)
session_datasets_s3 = {
    "Production.Product": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/Production.Product.csv",
    "Salaries": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/Salaries.csv",
    "train_titanic": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/train_titanic.csv",
    "superstore": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/superstore.csv"
}

# Aliases kept for consistency with the Session 4 and 5 config files.
session_datasets_http = session_datasets
