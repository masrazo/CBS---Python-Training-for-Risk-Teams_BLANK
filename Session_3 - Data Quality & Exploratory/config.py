#Configurations:

# HTTPS links: use with pandas, e.g. pd.read_csv(session_datasets_http["Salaries"])
session_datasets_http = {
    "Production.Product": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/Production.Product.csv",
    "Salaries": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/Salaries.csv",
    "train_titanic": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/train_titanic.csv",
    "superstore": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/superstore.csv"
}

# S3 links: use with Spark, e.g. spark.read.csv(session_datasets["Salaries"], header=True)
session_datasets = {
    "Production.Product": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/Production.Product.csv",
    "Salaries": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/Salaries.csv",
    "train_titanic": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/train_titanic.csv",
    "superstore": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/superstore.csv"
}
