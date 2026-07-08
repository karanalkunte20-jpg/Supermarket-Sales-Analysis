"""
==========================================================
Supermarket Sales Analysis
Author: Karan Alkunte

Description:
This project analyzes supermarket sales data using
Pandas, Matplotlib, and Seaborn to answer business
questions and generate insightful visualizations.
==========================================================
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.makedirs("graphs", exist_ok=True)#folder to store graphs
#==========================================================
# Load dataset
#==========================================================
df = pd.read_csv("supermarket_sales.csv")
df.columns=(df.columns.str.strip().str.lower().str.replace(" ","_").str.replace("%","percent"))
df["date"] = pd.to_datetime(df["date"], format="mixed")
df["time"] = pd.to_datetime(df["time"], format="%H:%M")
# ==========================================================
# Create New Columns
# ==========================================================
df["month"] = df["date"].dt.month_name()
df["day"] = df["date"].dt.day_name()
df["hour"] = df["time"].dt.hour
# ==========================================================
#Q1 what is total revenue
# ==========================================================
total_revenue=df["revenue"].sum()
print(f"Total Revenue of the Supermarket: ₹{total_revenue:,.2f}")

# ==========================================================
#Q2 What is the total gross income (profit)?
# ==========================================================
total_gross_income=df["gross_income"].sum()
print(f"Total Gross income of the Supermarket(profit): ₹{total_gross_income:,.2f}")

# ==========================================================
#Q3.What is the average customer rating?
avg_customer_rating = df["rating"].mean()
print(f"Average Customer Rating: {avg_customer_rating:.2f}/10")

# ==========================================================
#Q4. Which branch generates the highest revenue?
# ==========================================================
branch_revenue = df.groupby('branch')['revenue'].sum()
highest_branch = branch_revenue.idxmax()
highest_revenue = branch_revenue.max()
print(f"Branch {highest_branch} generates the highest revenue: ₹{highest_revenue:,.2f}")

# ==========================================================
#Q5. Which city has the highest sales?
# ==========================================================
city_with_highest_rev = df.groupby('city')['revenue'].sum()
highest_city = city_with_highest_rev.idxmax()
high_city_rev=city_with_highest_rev.max()
print(f"City {highest_city} generates the highest revenue: ₹{high_city_rev:,.2f}")

# ==========================================================
#Q6. Which product line generates the highest revenue?
# ==========================================================

product_revenue = df.groupby("product_line")["revenue"].sum()
highest_product = product_revenue.idxmax()
highest_product_revenue = product_revenue.max()
print(f"{highest_product} generates the highest revenue: ₹{highest_product_revenue:,.2f}")
# ==========================================================
#Q7. Which product line has the highest average customer rating?
# ==========================================================
product_rating = df.groupby("product_line")["rating"].mean()
highest_rated_product = product_rating.idxmax()
highest_product_rating = product_rating.max()
print(f"{highest_rated_product} has the highest average rating of {highest_product_rating:.2f}")
# ==========================================================
#Q8.Which product line sells the highest quantity?
# ==========================================================
high_product_quantity = df.groupby('product_line')['quantity'].sum()
high_product = high_product_quantity.idxmax()
high_quantity=high_product_quantity.max()
print(f"{high_product} has the max no of quantity: {high_quantity:.2f}")
# ==========================================================
#Q9. Do male and female customers spend differently?
# ==========================================================
gender_revenue = df.groupby("gender_customer")["revenue"].sum()
male_revenue = gender_revenue["Male"]
female_revenue = gender_revenue["Female"]
if male_revenue > female_revenue:
    print(f"Yes. Male customers spend more (₹{male_revenue:,.2f}) than Female customers (₹{female_revenue:,.2f}).")
elif female_revenue > male_revenue:
    print(f"Yes. Female customers spend more (₹{female_revenue:,.2f}) than Male customers (₹{male_revenue:,.2f}).")
else:
    print("No. Male and Female customers spend the same amount.")
# ==========================================================
#Q10. Which customer type spends more?
# ==========================================================
cust_spend = df.groupby('customer_type')['revenue'].sum()
member_revenue = cust_spend['Member']
normal_revenue = cust_spend['Normal']
if member_revenue > normal_revenue:
    print(f"Member customers spend more (₹{member_revenue:,.2f}) than Normal customers (₹{normal_revenue:,.2f}).")
elif normal_revenue > member_revenue:
    print(f"Normal customers spend more (₹{normal_revenue:,.2f}) than Member customers (₹{member_revenue:,.2f}).")
else:
    print("Both customer types spend the same amount.")
# ==========================================================
# Q11. Which payment method is most preferred?
# ==========================================================
payment_prefered = df['payment_method'].value_counts()
payment_me = payment_prefered.idxmax()
total_transactions = payment_prefered.max()
print(f"{payment_me} is the most preferred payment method with {total_transactions} transactions.")
# ==========================================================
# Q12. Which month has the highest sales?
# ==========================================================
month_highest_sales=df.groupby('month')['revenue'].sum()
month_of_sales = month_highest_sales.idxmax()
revenue_in_month = month_highest_sales.max()
print(f"{month_of_sales} has the highest sales: ₹{revenue_in_month:,.2f}")
# ==========================================================
# Q13. At what hour are sales highest?
# ==========================================================
hour_highest_sales=df.groupby('hour')['revenue'].sum()
hour_of_sales = hour_highest_sales.idxmax()
revenue_in_hour = hour_highest_sales.max()
print(f"{hour_of_sales}:00 has the highest sales: ₹{revenue_in_hour:,.2f}")
# ==========================================================
# Q14. Does buying more quantity increase revenue?
# ==========================================================
plt.figure(figsize=(8,5))
sns.scatterplot(data = df,x='quantity',y='revenue')
plt.xlabel('quantity')
plt.ylabel('revenue')
plt.tight_layout()
plt.show()
# ==========================================================
# Q15. Which branch has the highest average customer rating?
# ==========================================================
branch_avg_rating = df.groupby("branch")["rating"].mean()
highest_rated_branch = branch_avg_rating.idxmax()
highest_branch_rating = branch_avg_rating.max()
print(f"Branch {highest_rated_branch} has the highest average customer rating: {highest_branch_rating:.2f}")
# ==========================================================
#Revenue by Product Line (Horizontal Bar)
# ==========================================================
product_revenue = (
    df.groupby("product_line")["revenue"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)
plt.figure(figsize=(8,5))
sns.barplot(data=product_revenue,x="revenue",y="product_line")
plt.xlabel("Revenue")
plt.ylabel("Product Line")
plt.title("Revenue by Product Line")
plt.tight_layout()
plt.savefig("graphs/revenue_by_product_line.png", dpi=300)
plt.show()
# ==========================================================
#Visualization 2: Monthly Sales Trend
# ==========================================================
monthly_sales = df.groupby('month')['revenue'].sum().reset_index()
month_order=['January','February','March']
monthly_sales["month"] = pd.Categorical(
    monthly_sales["month"],
    categories=month_order,
    ordered=True
)
monthly_sales = monthly_sales.sort_values("month")
plt.figure(figsize=(8,5))
sns.lineplot(
    data=monthly_sales,
    x="month",
    y="revenue",
    marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("graphs/monthly_sales_trend.png", dpi=300)
plt.show()
# ==========================================================
#Revenue by City
# ==========================================================
city_revenue=df.groupby('city')['revenue'].sum().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(data=city_revenue, x="city", y="revenue")
plt.title('Revenue by City')
plt.xlabel('city')
plt.ylabel('revenue')
plt.tight_layout()
plt.savefig("graphs/revenue_by_city.png", dpi=300)
plt.show()
# ==========================================================
# Payment Method Distribution
# ==========================================================
payment_distribution = df['payment_method'].value_counts()
plt.figure(figsize=(7,7))
plt.pie(
    payment_distribution.values,
    labels=payment_distribution.index,
    startangle= 90,
    autopct='%1.1f%%'
)
plt.title('Payment Method Distribution')
plt.tight_layout()
plt.savefig("graphs/payment_method_distribution.png", dpi=300)
plt.show()
# =========================================================
# Quantity vs Revenue
# ==========================================================
plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df,
    x="quantity",
    y="revenue"
)
plt.title("Quantity vs Revenue")
plt.xlabel("Quantity Purchased")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("graphs/quantity_vs_revenue.png", dpi=300)
plt.show()

# ==========================================================
# Business Insights
# ==========================================================
print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)
print(f"• Branch {highest_branch} generated the highest revenue (₹{highest_revenue:,.2f}).")
print(f"• {highest_city} recorded the highest city revenue (₹{high_city_rev:,.2f}).")
print(f"• '{highest_product}' generated the highest revenue among all product lines.")
print(f"• '{high_product}' sold the highest quantity ({high_quantity} units).")
print(f"• {month_of_sales} was the best-performing month with revenue of ₹{revenue_in_month:,.2f}.")
print(f"• Peak sales occurred at {hour_of_sales}:00 with revenue of ₹{revenue_in_hour:,.2f}.")
print(f"• {payment_me} was the most preferred payment method with {total_transactions} transactions.")
print(f"• Branch {highest_rated_branch} achieved the highest average customer rating ({highest_branch_rating:.2f}/10).")