
import pandas as pd

# Load dataset
df = pd.read_csv("amazon_transformed.csv")

print("AMAZON CUSTOMER ANALYSIS")
print("------------------------")

# Total customer records
if "user_id" in df.columns:
    print("\nTotal Customer Records:", len(df))
    print("Unique Customers:", df["user_id"].nunique())

# Customer review analysis
if "review_id" in df.columns:
    print("Total Reviews:", df["review_id"].nunique())

# Rating analysis
if "rating" in df.columns:
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    print("\nAverage Customer Rating:", round(df["rating"].mean(), 2))

# Rating category analysis
if "rating_category" in df.columns:
    print("\nRating Category Distribution:")
    print(df["rating_category"].value_counts())

# Most active reviewers
if "user_name" in df.columns:
    print("\nTop 10 Reviewers:")
    print(df["user_name"].value_counts().head(10))

# Save customer analysis report
df.describe(include="all").to_csv("customer_analysis_report.csv")

# Save rating category counts
if "rating_category" in df.columns:
    df["rating_category"].value_counts().to_csv(
        "customer_rating_report.csv",
        header=["Number of Records"]
    )

print("\nCustomer analysis completed successfully!")
print("Reports saved successfully.")
