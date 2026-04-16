import polars as pl

# 1. Create a dummy dataset in memory and make it 'Lazy'
# This mimics scanning a real file
df = pl.DataFrame({
    "user_id": [1, 2, 1, 3, 2],
    "year": [2019, 2021, 2022, 2023, 2020],
    "spend": [10, 50, 20, 100, 40],
    "unused_col": ["a", "b", "c", "d", "e"]
}).lazy()

# 2. Define a messy plan
plan = (
    df.filter(pl.col("year") > 2020)   # Filter rows
    .select(["user_id", "spend"])     # Only keep 2 columns
    .group_by("user_id")              # Aggregate
    .agg(pl.col("spend").sum())
)

# 3. This will now work!
print("--- OPTIMIZED PLAN ---")
print(plan.explain())

# 4. To see the actual result:
# print(plan.collect())