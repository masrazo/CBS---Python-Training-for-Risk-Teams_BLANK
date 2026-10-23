##Configurations

# HTTPS links (default): read with pandas, e.g. pd.read_csv(pagila_datasets["actor"])
pagila_datasets = {

    "actor": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/actor.csv",
    "address": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/address.csv",
    "category": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/category.csv",
    "city": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/city.csv",
    "country": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/country.csv",
    "customer": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/customer.csv",
    "film_actor": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/film_actor.csv",
    "film_category": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/film_category.csv",
    "film": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/film.csv",
    "inventory": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/inventory.csv",
    "language": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/language.csv",

    "payments": {
        "payment2022_01": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_01.csv",
        "payment2022_02": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_02.csv",
        "payment2022_03": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_03.csv",
        "payment2022_04": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_04.csv",
        "payment2022_05": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_05.csv",
        "payment2022_06": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_06.csv",
        "payment2022_07": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_07.csv"
    }
}

# HTTPS links (default): read with pandas, e.g. pd.read_csv(session_datasets["Salaries"])
session_datasets = {
    "Production.Product": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/Production.Product.csv",
    "customer": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/customer.csv",
    "payment": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/payment.csv",
    "Salaries": "https://rockborne-bucket-01-cbs.s3.eu-west-2.amazonaws.com/Data_Sources_CBS_Risk/Salaries.csv"
}

# S3 links (Databricks/Spark only), e.g. spark.read.csv(pagila_datasets_s3["actor"], header=True)
pagila_datasets_s3 = {
    
    "actor": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/actor.csv",
    "address": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/address.csv",
    "category": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/category.csv",
    "city": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/city.csv",
    "country": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/country.csv",
    "customer": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/customer.csv",
    "film_actor": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/film_actor.csv",
    "film_category": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/film_category.csv",
    "film": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/film.csv",
    "inventory": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/inventory.csv",
    "language": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/language.csv",
    
    "payments": {
        "payment2022_01": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_01.csv",
        "payment2022_02": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_02.csv",
        "payment2022_03": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_03.csv",
        "payment2022_04": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_04.csv",
        "payment2022_05": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_05.csv",
        "payment2022_06": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_06.csv",
        "payment2022_07": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/pagila_csv/payment_p2022_07.csv"
    }
}

# S3 links (Databricks/Spark only), e.g. spark.read.csv(session_datasets_s3["Salaries"], header=True)
session_datasets_s3 = {
    "Production.Product": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/Production.Product.csv",
    "customer": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/customer.csv",
    "payment": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/payment.csv",
    "Salaries": "s3a://rockborne-bucket-01-cbs/Data_Sources_CBS_Risk/Salaries.csv"
}

# Aliases kept for consistency with the Session 4 and 5 config files.
pagila_datasets_http = pagila_datasets
session_datasets_http = session_datasets
