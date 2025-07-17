# Interactive Sales Dashboard with Streamlit

## Project Overview

This project is a web-based, interactive dashboard built to analyze and visualize the "Sample - Superstore" sales dataset. The application allows users to dynamically filter data by Region, Category, and Order Date, and instantly view updated KPIs and charts.

This project demonstrates the ability to transform a raw CSV dataset into a user-friendly, interactive data exploration tool using Python.

**Live Demo:** *(We will add this link later if you deploy it on Streamlit Community Cloud)*

## Key Features

- **Interactive Filtering:** Users can filter the entire dataset using multi-select widgets for Region and Category, and a date range selector.
- **Dynamic KPI Display:** Key Performance Indicators (Total Sales, Total Profit, Profit Margin) are calculated and displayed in real-time based on filter selections.
- **Interactive Visualizations:** The dashboard features two dynamic charts created with Plotly:
    - A horizontal bar chart showing sales by product sub-category.
    - A line chart illustrating daily sales trends.
- **Efficient Data Handling:** Utilizes Streamlit's caching (`@st.cache_data`) to ensure fast performance and prevent re-loading the dataset on every interaction.

## Screenshot

*(We will add a screenshot of the dashboard here)*

![Dashboard Screenshot](path/to/screenshot.png) 

## Tech Stack

- **Language:** Python
- **Libraries:**
    - **Streamlit:** For building the interactive web application.
    - **Pandas:** For data loading, cleaning, and manipulation.
    - **Plotly Express:** For creating interactive data visualizations.

## How to Run Locally

1.  Clone this repository: `git clone [your-repo-url]`
2.  Navigate to the project directory: `cd dashboard_project`
3.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate  # On Windows
    ```
4.  Install the required dependencies:
    ```bash
    pip install streamlit pandas plotly
    ```
5.  Run the Streamlit application:
    ```bash
    streamlit run dashboard.py
    ```
6.  The application will open in your web browser.
