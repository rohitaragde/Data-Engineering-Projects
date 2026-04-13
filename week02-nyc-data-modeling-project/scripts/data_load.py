import pandas as pd 

trips=pd.read_parquet("data/raw/yellow_tripdata_2026-01.parquet")
zones=pd.read_csv("data/raw/taxi_zone_lookup.csv")

print(trips.head())
print(trips.columns)

