import pandas as pd

# Step 01: Load the Lookup File
zones=pd.read_csv("data/raw/taxi_zone_lookup.csv")

# Step 02: Rename columns to match our model
dim_location=zones.rename(columns={
    "LocationID":"location_id",
    "Borough":"borough",
    "Zone":"zone",
    "Service_zone":"service_zone"
})

# Step 03: Keep only the required columns
dim_location=dim_location[["location_id","borough","zone","service_zone"]]

# Step 04: Validate data
print("Preview:")
print(dim_location.head())

print("\nShape:")
print(dim_location.shape)

print("\nNull values:")
print(dim_location.isnull().sum())

# Step 5: Save the dimension table
dim_location.to_csv("data/dim_location.csv", index=False)

print("\n✅ dim_location created successfully!")