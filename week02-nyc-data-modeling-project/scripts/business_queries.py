import os
import pandas as pd

# -----------------------------
# Load tables
# -----------------------------
fact_trips = pd.read_csv("data/processed/fact_trips.csv")
dim_location = pd.read_csv("data/processed/dim_location.csv")
dim_time = pd.read_csv("data/processed/dim_time.csv")

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

# Optional: create outputs folder for saving query results
os.makedirs("outputs", exist_ok=True)


def print_section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


# -----------------------------
# Query 1: Revenue by Borough
# -----------------------------
print_section("1. Revenue by Borough")

df1 = fact_trips.merge(
    dim_location,
    left_on="pickup_location_id",
    right_on="location_id",
    how="left"
)

df1["borough"] = df1["borough"].fillna("Unmapped")

result1 = (
    df1.groupby("borough", dropna=False)["total_amount"]
    .sum()
    .reset_index()
    .sort_values(by="total_amount", ascending=False)
)

print(result1.to_string(index=False))

top_borough = result1.iloc[0]["borough"]
top_revenue = result1.iloc[0]["total_amount"]
print(f"\nInsight: {top_borough} generated the highest revenue at ${top_revenue:,.2f}.")

result1.to_csv("outputs/revenue_by_borough.csv", index=False)


# -----------------------------
# Query 2: Trips per Hour
# -----------------------------
print_section("2. Trips per Hour")

df2 = fact_trips.merge(
    dim_time,
    left_on="pickup_datetime",
    right_on="datetime",
    how="left"
)

result2 = (
    df2.groupby("hour")["trip_id"]
    .count()
    .reset_index(name="total_trips")
    .sort_values(by="hour")
)

peak_row = result2.loc[result2["total_trips"].idxmax()]
print(f"\nPeak hour: {int(peak_row['hour'])}:00 with {int(peak_row['total_trips']):,} trips\n")

print(result2.to_string(index=False))

print(
    f"\nInsight: Peak demand occurs at {int(peak_row['hour'])}:00 "
    f"with {int(peak_row['total_trips']):,} trips."
)

result2.to_csv("outputs/trips_per_hour.csv", index=False)


# -----------------------------
# Query 3: Average Trip Distance per Day
# -----------------------------
print_section("3. Average Trip Distance per Day")

result3 = (
    df2.groupby("date")["trip_distance"]
    .mean()
    .reset_index(name="avg_trip_distance")
    .sort_values(by="date")
)

# Keep January only for cleaner reporting
result3["date"] = pd.to_datetime(result3["date"])
result3 = result3[
    (result3["date"] >= "2026-01-01") &
    (result3["date"] <= "2026-01-31")
]

print(result3.to_string(index=False))

max_day = result3.loc[result3["avg_trip_distance"].idxmax()]
min_day = result3.loc[result3["avg_trip_distance"].idxmin()]

print(
    f"\nInsight: Longest average trips occurred on {max_day['date'].date()} "
    f"({max_day['avg_trip_distance']:.2f} miles)."
)
print(
    f"Insight: Shortest average trips occurred on {min_day['date'].date()} "
    f"({min_day['avg_trip_distance']:.2f} miles)."
)

result3.to_csv("outputs/avg_trip_distance_per_day.csv", index=False)


# -----------------------------
# Query 4: Revenue by Weekday
# -----------------------------
print_section("4. Revenue by Weekday")

weekday_order = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

result4 = (
    df2.groupby("weekday")["total_amount"]
    .sum()
    .reset_index()
)

result4["weekday"] = pd.Categorical(
    result4["weekday"],
    categories=weekday_order,
    ordered=True
)
result4 = result4.sort_values("weekday")

print(result4.to_string(index=False))

top_day = result4.loc[result4["total_amount"].idxmax()]
print(f"\nInsight: {top_day['weekday']} generated the highest revenue at ${top_day['total_amount']:,.2f}.")

result4.to_csv("outputs/revenue_by_weekday.csv", index=False)


# -----------------------------
# Query 5: Top Pickup Zones
# -----------------------------
print_section("5. Top Pickup Zones")

df5 = fact_trips.merge(
    dim_location,
    left_on="pickup_location_id",
    right_on="location_id",
    how="left"
)

df5["zone"] = df5["zone"].fillna("Unmapped")

result5 = (
    df5.groupby("zone")["trip_id"]
    .count()
    .reset_index(name="total_trips")
    .sort_values(by="total_trips", ascending=False)
    .head(10)
)

print(result5.to_string(index=False))

top_zone = result5.iloc[0]["zone"]
top_zone_trips = result5.iloc[0]["total_trips"]
print(f"\nInsight: {top_zone} is the busiest pickup zone with {top_zone_trips:,} trips.")

result5.to_csv("outputs/top_pickup_zones.csv", index=False)