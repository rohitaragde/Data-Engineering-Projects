import pandas as pd 

# Step 01: Load Trips Data
trips=pd.read_parquet("data/raw/yellow_tripdata_2026-01.parquet")

# Step 02: Convert pickup datetime
trips["tpep_pickup_datetime"]=pd.to_datetime(trips["tpep_pickup_datetime"])

# Step 03: Round pickup datetime to hour
# This is done so it can match dim_time.datetime

trips["pickup_datetime"]=trips["tpep_pickup_datetime"].dt.floor("h")

# Step 04: Select only required columns

fact_trips=trips[[
    "pickup_datetime",
    "PULocationID",
    "DOLocationID",
    "passenger_count",
    "trip_distance",
    "fare_amount",
    "tip_amount",
    "total_amount",  
]].copy()

# Step 05: Rename columns for cleaner modeling

fact_trips=fact_trips.rename(columns={
    "PULocationID":"pickup_location_id",
    "DOLocationID":"dropoff_location_id"
    })

# Step 06: Create trip_id
fact_trips.insert(0,"trip_id",range(1,len(fact_trips)+1))

# Step 07: Validate
print("Preview: ")
print(fact_trips.head())

print("\nShape:")
print(fact_trips.shape)

print("\nNull values:")
print(fact_trips.isnull().sum())

# Step 08: Save
fact_trips.to_csv("data/fact-trips.csv",index=False)

print("\n✅ fact_trips created successfully!")