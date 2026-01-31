import pandas as pd
import sqlite3

orders = pd.read_csv("data/orders.csv")

users = pd.read_json("data/users.json")

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

with open("data/restaurants.sql", "r") as f:
    sql_script = f.read()

cursor.executescript(sql_script)

restaurants = pd.read_sql("SELECT * FROM restaurants", conn)

merged = pd.merge(
    orders, users,
    on="user_id",
    how="left"
)

final_df = pd.merge(
    merged, restaurants,
    on="restaurant_id",
    how="left"
)

final_df.to_csv(
    "output/final_dataset.csv",
    index=False
)

print("✅ Final dataset created successfully!")
