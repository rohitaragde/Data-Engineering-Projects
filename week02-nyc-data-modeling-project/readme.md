# 🚕 NYC Taxi Data Modeling & Analytics (Week 02)

## 📌 Project Overview
This project focuses on building a **data model and analytical dashboard** using NYC Taxi trip data (January 2026).

The objective was to simulate a **real-world data engineering workflow**:
- Transform raw data into structured datasets
- Design fact and dimension tables
- Generate business insights using Power BI

## 🏗️ Data Architecture

This project follows a **medallion-style architecture**:

### 🔹 Raw Layer (Bronze)
- `yellow_tripdata_2026-01.parquet`
- `taxi_zone_lookup.csv`

### 🔹 Processed Layer (Silver)
- `dim_location.csv`
- `dim_time.csv`
- `fact_trips.csv

  ### 🔹 Output Layer (Gold)
- `revenue_by_borough.csv`
- `revenue_by_weekday.csv`
- `trips_per_hour.csv`
- `top_pickup_zones.csv`
- `avg_trip_distance_per_day.csv`

  ## Star Schema Architecture

```markdown
```mermaid
flowchart TB

    FT["fact_trips
    -------------------------
    trip_id (PK)
    pickup_datetime_hour (FK)
    pickup_location_id (FK)
    dropoff_location_id (FK)
    passenger_count
    trip_distance
    fare_amount
    tip_amount
    total_amount"]

    DT["dim_time
    -------------------------
    datetime (PK)
    date
    year
    month
    day
    hour
    weekday
    weekend_flag"]

    DLP["dim_location
    -------------------------
    location_id (PK)
    borough
    zone
    service_zone
    <<pickup role>>"]

    DLD["dim_location
    -------------------------
    location_id (PK)
    borough
    zone
    service_zone
    <<dropoff role>>"]

    DT --> FT
    DLP --> FT
    DLD --> FT

## ⚙️ Technologies Used
- Python (Pandas)
- Data Modeling (Fact & Dimension Tables)
- Power BI
- Parquet & CSV

  ## 📊 Dashboard

![Dashboard](images/dashboard_screenshot.png)

### Key Insights:
- Manhattan generates the highest revenue
- Airport zones (JFK, LaGuardia) are major contributors
- Peak trip demand occurs during evening hours (5 PM – 8 PM)
- Revenue is highest between Thursday and Saturday

  ## 📥 Dataset Source

NYC Taxi Data (January 2026)  
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

## 🚀 Learning Outcomes

- Designed a dimensional data model (Fact & Dimension Tables)
- Built an ETL pipeline using Python
- Created a business-driven analytics dashboard
- Simulated a real-world data engineering project workflow


