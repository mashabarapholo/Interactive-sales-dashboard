# In dashboard.py (Complete Version)

import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Interactive Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- DATA LOADING AND CLEANING ---
@st.cache_data
def load_data():
    df = pd.read_csv('superstore_data.csv', encoding='latin1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

df = load_data()

# --- SIDEBAR FOR FILTERS ---
st.sidebar.header("Dashboard Filters")

region = st.sidebar.multiselect(
    "Select Region:",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

# A date range selector
# Get the min and max dates from the dataframe to set the slider's range
min_date = df["Order Date"].min()
max_date = df["Order Date"].max()

date_range = st.sidebar.date_input(
    "Select Date Range:",
    value=(min_date, max_date), # Default range is all dates
    min_value=min_date,
    max_value=max_date,
)

# --- FILTER THE DATAFRAME BASED ON SELECTIONS ---
# We need to handle the date range tuple from the date_input widget
start_date, end_date = date_range

df_selection = df.query(
    "Region == @region & Category == @category & `Order Date` >= @start_date & `Order Date` <= @end_date"
)

# --- MAIN PAGE ---
st.title("📊 Superstore Sales Analysis")
st.markdown("---") # A horizontal line

# --- KEY PERFORMANCE INDICATORS (KPIs) ---
total_sales = int(df_selection["Sales"].sum())
total_profit = int(df_selection["Profit"].sum())

# Calculate profit margin. Handle division by zero case.
if total_sales > 0:
    profit_margin = (total_profit / total_sales) * 100
else:
    profit_margin = 0

# Display the KPIs in columns
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Total Sales")
    st.subheader(f"US $ {total_sales:,}")
with col2:
    st.subheader("Total Profit")
    st.subheader(f"US $ {total_profit:,}")
with col3:
    st.subheader("Profit Margin")
    st.subheader(f"{profit_margin:.2f}%")

st.markdown("---")

# --- CHARTS ---

# CHART 1: Sales by Sub-Category (Bar Chart)
sales_by_subcategory = df_selection.groupby(by=["Sub-Category"])[["Sales"]].sum().sort_values(by="Sales")

fig_subcategory_sales = px.bar(
    sales_by_subcategory,
    x="Sales",
    y=sales_by_subcategory.index, # Use the index (Sub-Category names) for the y-axis
    orientation="h", # Horizontal bar chart
    title="<b>Sales by Sub-Category</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_subcategory),
    template="plotly_white",
)
fig_subcategory_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)", # Transparent background
    xaxis=(dict(showgrid=False))
)

# CHART 2: Sales Over Time (Line Chart)
# Group sales by Order Date (daily)
daily_sales = df_selection.groupby(pd.Grouper(key='Order Date', freq='D'))[['Sales']].sum().reset_index()

fig_daily_sales = px.line(
    daily_sales,
    x="Order Date",
    y="Sales",
    title="<b>Daily Sales Trend</b>",
)
fig_daily_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

# Display the charts in columns
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_subcategory_sales, use_container_width=True)
right_column.plotly_chart(fig_daily_sales, use_container_width=True)


# --- HIDE STREAMLIT STYLE ---
# This is optional CSS to hide the default Streamlit branding
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Display the raw data table at the end
st.dataframe(df_selection)