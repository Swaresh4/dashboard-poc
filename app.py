import streamlit as st
import pandas as pd

# Page title
st.title("Financial Dashboard POC")

# Read Excel
file_path = "HCL.xlsx"

# Read sheet
raw_data = pd.read_excel(file_path, sheet_name="Profit_Loss", header=None)

# Clean data
cleaned = raw_data.dropna()
cleaned.columns = ["Particulars", "Value"]

# Remove non-numeric rows
cleaned = cleaned[pd.to_numeric(cleaned["Value"], errors="coerce").notnull()]

# Convert values
cleaned["Value"] = cleaned["Value"].astype(float)

# Show table
st.subheader("Financial Data")
st.dataframe(cleaned)

# Metrics
revenue = cleaned[cleaned["Particulars"] == "Revenues"]
profit = cleaned[cleaned["Particulars"] == "Gross profit"]

col1, col2 = st.columns(2)

with col1:
    if not revenue.empty:
        st.metric("Revenue", f"₹ {revenue.iloc[0]['Value']:,.0f} Mn")

with col2:
    if not profit.empty:
        st.metric("Gross Profit", f"₹ {profit.iloc[0]['Value']:,.0f} Mn")

# Chart
st.subheader("Financial Overview")

chart_data = cleaned.head(10)

st.bar_chart(chart_data.set_index("Particulars"))