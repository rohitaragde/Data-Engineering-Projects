import pandas as pd 

# Step 01: Load Trips Data
trips=pd.read_parquet("data/raw/yellow_tripdata_2026-01.parquet")

# Step 02: Convert to DateTime
trips["tpep_pickup_datetime"]=pd.to_datetime(trips["tpep_pickup_datetime"])

# Step 03: Create dim_time using pickup time
dim_time=trips[["tpep_pickup_datetime"]].drop_duplicates()

# Step 04: Round to hour
dim_time["hour_timestamp"] = dim_time["tpep_pickup_datetime"].dt.floor("h")

# Keep only unique hours
dim_time = dim_time[["hour_timestamp"]].drop_duplicates()

# Step 05: Extract Time Components
dim_time["date"] = dim_time["hour_timestamp"].dt.date
dim_time["year"] = dim_time["hour_timestamp"].dt.year
dim_time["month"] = dim_time["hour_timestamp"].dt.month
dim_time["day"] = dim_time["hour_timestamp"].dt.day
dim_time["hour"] = dim_time["hour_timestamp"].dt.hour
dim_time["weekday"] = dim_time["hour_timestamp"].dt.day_name()
dim_time["weekend_flag"] = dim_time["weekday"].isin(["Saturday", "Sunday"])

# Step 06: Weekend Flag
dim_time["weekend_flag"]=dim_time["weekday"].isin(["Saturday","Sunday"])

# Step 07: Rename Column
dim_time = dim_time.rename(columns={"hour_timestamp": "datetime"})

# Step 08: Validate
print("Preview:")
print(dim_time.head())

print("\nShape:")
print(dim_time.shape)

print("\nNull values:")
print(dim_time.isnull().sum())

# Step 09: Save
dim_time.to_csv("data/dim_time.csv",index=False)

