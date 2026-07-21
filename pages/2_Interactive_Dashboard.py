import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Interactive Analytics Dashboard",
    layout="wide"
)

# ==================================================
# LOAD DATA
# ==================================================

@st.cache_data
def load_data():
    return pd.read_pickle(
        "models/dashboard_data.pkl"
    )

product_df = load_data()

# ==================================================
# PAGE TITLE
# ==================================================

st.title("📊 Interactive Analytics Dashboard")

st.markdown(
    "Explore inventory behavior, sales trends, supplier performance, and stock movement through interactive analytics."
)
st.caption(
    "Insights update dynamically based on selected filters."
)

# ==================================================
# FILTER SESSION STATE
# ==================================================

if "selected_company" not in st.session_state:
    st.session_state.selected_company = "All"

if "selected_type" not in st.session_state:
    st.session_state.selected_type = "All"

if "selected_product" not in st.session_state:
    st.session_state.selected_product = "All"

# ==================================================
# DASHBOARD FILTERS
# ==================================================

st.subheader("🔍 Dashboard Filters")

f1, f2, f3, f4 = st.columns([3, 3, 3, 1])

# ==================================================
# COMPANY FILTER
# ==================================================

with f1:

    company_options = (
        ["All"]
        + sorted(
            product_df["Company"]
            .dropna()
            .unique()
            .tolist()
        )
    )

    selected_company = st.selectbox(
        "Company",
        company_options,
        key="selected_company"
    )

# ==================================================
# TYPE FILTER
# ==================================================

company_filtered = product_df.copy()

if selected_company != "All":
    company_filtered = company_filtered[
        company_filtered["Company"] == selected_company
    ]

available_types = (
    ["All"]
    + sorted(
        company_filtered["type"]
        .dropna()
        .unique()
        .tolist()
    )
)

if st.session_state.selected_type not in available_types:
    st.session_state.selected_type = "All"

with f2:

    selected_type = st.selectbox(
        "Product Type",
        available_types,
        key="selected_type"
    )

# ==================================================
# PRODUCT FILTER
# ==================================================

product_filtered = company_filtered.copy()

if selected_type != "All":
    product_filtered = product_filtered[
        product_filtered["type"] == selected_type
    ]

available_products = (
    ["All"]
    + sorted(
        product_filtered["Name"]
        .dropna()
        .unique()
        .tolist()
    )
)

if st.session_state.selected_product not in available_products:
    st.session_state.selected_product = "All"

with f3:

    selected_product = st.selectbox(
        "Product",
        available_products,
        key="selected_product"
    )

# ==================================================
# RESET BUTTON
# ==================================================

def reset_filters():

    st.session_state.selected_company = "All"
    st.session_state.selected_type = "All"
    st.session_state.selected_product = "All"


with f4:

    st.write("")

    st.button(
        "🔄 Reset",
        use_container_width=True,
        on_click=reset_filters
    )


# ==================================================
# APPLY FILTERS
# ==================================================

filtered_df = product_df.copy()

if selected_company != "All":
    filtered_df = filtered_df[
        filtered_df["Company"] == selected_company
    ]

if selected_type != "All":
    filtered_df = filtered_df[
        filtered_df["type"] == selected_type
    ]

if selected_product != "All":
    filtered_df = filtered_df[
        filtered_df["Name"] == selected_product
    ]

# ==================================================
# EMPTY DATASET PROTECTION
# ==================================================

if filtered_df.empty:
    st.error(
        "No records found for the selected filters."
    )
    st.stop()

# ==================================================
# NUMBER FORMATTER
# ==================================================

def format_currency(value):

    if value >= 10000000:
        return f"₹ {value/10000000:.2f} Cr"

    elif value >= 100000:
        return f"₹ {value/100000:.2f} Lakh"

    elif value >= 1000:
        return f"₹ {value/1000:.2f} K"

    return f"₹ {value:.0f}"

# ==================================================
# KPI CARDS FUNCTION
# ==================================================

def kpi_card(title, value, subtitle="", color="#60A5FA"):

    st.markdown(
        f"""
<div style="
background: linear-gradient(135deg,#111827,#1f2937);
padding:25px;
border-radius:18px;
border-left:5px solid {color};
text-align:center;
height:200px;
box-shadow:0 6px 15px rgba(0,0,0,0.25);
">

<h4 style="
color:#d1d5db;
margin-bottom:10px;
">
{title}
</h4>

<h1 style="
color:{color};
font-size:38px;
font-weight:bold;
margin-bottom:5px;
">
{value}
</h1>

<p style="
color:#9ca3af;
font-size:13px;
">
{subtitle}
</p>

</div>
""",
        unsafe_allow_html=True
    )

# ==================================================
# KPI CALCULATIONS
# ==================================================

total_products = filtered_df["Name"].nunique()

total_companies = filtered_df["Company"].nunique()

# Quantity Metrics
total_sales_units = filtered_df["SaleTot"].sum()
avg_sales_units = filtered_df["SaleTot"].mean()
avg_purchase_units = filtered_df["PurTot"].mean()

# Value Metrics
total_inventory_value = filtered_df["QohValue"].sum()

# Business KPI
inventory_turnover = (
    total_sales_units / filtered_df["Qoh"].sum()
    if filtered_df["Qoh"].sum() != 0
    else 0
)

# Overstock KPI
overstock_count = len(
    filtered_df[
        filtered_df["Qoh"] >
        filtered_df["SaleTot"] * 2
    ]
)

overstock_percentage = (
    (overstock_count / len(filtered_df)) * 100
    if len(filtered_df) > 0
    else 0
)

# Inventory Coverage KPI
inventory_coverage = (
    filtered_df["Qoh"].sum()
    /
    filtered_df["SaleTot"].sum()
    if filtered_df["SaleTot"].sum() != 0
    else 0
)

# ==================================================
# KPI ROW 1
# ==================================================

row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)

with row1_col1:
    kpi_card(
        "📦 Products",
        f"{total_products:,}",
        "Inventory Items",
        "#22C55E"
    )

with row1_col2:
    kpi_card(
        "🏢 Companies",
        f"{total_companies:,}",
        "Manufacturers",
        "#3B82F6"
    )

with row1_col3:
    kpi_card(
        "📈 Sales Units",
        f"{total_sales_units:,.0f}",
        "Total Units Sold",
        "#F59E0B"
    )

with row1_col4:
    kpi_card(
        "💰 Inventory Value",
        format_currency(total_inventory_value),
        "Current Inventory Worth",
        "#EF4444"
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==================================================
# KPI ROW 2
# ==================================================

row2_col1, row2_col2, row2_col3, row2_col4 = st.columns(4)

with row2_col1:
    kpi_card(
        "📊 Avg Sales",
        f"{avg_sales_units:.1f}",
        "Units Sold Per Product",
        "#06B6D4"
    )

with row2_col2:
    kpi_card(
    "📅 Stock-to-Sales Ratio",
    f"{inventory_coverage:.2f}x",
    "Current Stock / Sales",
    "#F97316"
)

with row2_col3:
    kpi_card(
        "🔄 Inventory Turnover",
        f"{inventory_turnover:.2f}x",
        "Sales / Stock Ratio",
        "#8B5CF6"
    )

with row2_col4:
    kpi_card(
        "⚠️ Overstock Risk",
        f"{overstock_percentage:.2f}%",
        "Products Flagged",
        "#EF4444"
    )

st.markdown("<br>", unsafe_allow_html=True)

st.divider()

# ==================================================
# CHART 1 - FAST MOVING PRODUCTS
# ==================================================

top_products = (
    filtered_df.groupby("Name")["SaleTot"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.bar(
    top_products,
    x="SaleTot",
    y="Name",
    orientation="h",
    title="🚀 Fast Moving Products",
    text_auto=".0f"
)

fig1.update_layout(
    height=500,
    yaxis=dict(categoryorder="total ascending"),
    xaxis_title="Units Sold",
    yaxis_title="Product"
)

# ==================================================
# CHART 2 - TOP REVENUE COMPANIES
# ==================================================

top_companies = (
    filtered_df.groupby("Company")["SaleTot"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    top_companies,
    x="SaleTot",
    y="Company",
    orientation="h",
    title="🏢 Top Companies by Sales Volume",
    text_auto=".0f"
)

fig2.update_layout(
    height=500,
    yaxis=dict(categoryorder="total ascending"),
    xaxis_title="Units Sold",
    yaxis_title="Company"
)

# ==================================================
# DISPLAY CHARTS ROW 1
# ==================================================

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)

# ==================================================
# CHART 3 - PURCHASE VS SALES
# ==================================================

fig3 = px.scatter(
    filtered_df,
    x="PurTot",
    y="SaleTot",
    color="type",
    hover_name="Name",
    title="💰 Purchase Quantity vs Sales Quantity",
    opacity=0.7,
    render_mode="webgl"
)

fig3.update_traces(
    marker=dict(size=8)
)

fig3.update_layout(
    height=550,
    xaxis_title="Purchased Units",
    yaxis_title="Sold Units"
)

# ==================================================
# CHART 4 - STOCK VS SALES
# ==================================================

fig4 = px.scatter(
    filtered_df,
    x="Qoh",
    y="SaleTot",
    color="type",
    hover_name="Name",
    title="📦 Stock Availability vs Sales Performance",
    opacity=0.7,
    render_mode="webgl"
)

fig4.update_traces(
    marker=dict(size=8)
)

fig4.update_layout(
    height=550,
    xaxis_title="Current Stock",
    yaxis_title="Units Sold"
)

# ==================================================
# DISPLAY CHARTS ROW 2
# ==================================================

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.plotly_chart(fig4, use_container_width=True)

# ==================================================
# CHART 5 - INVENTORY DISTRIBUTION
# ==================================================

inventory_dist_df = filtered_df.copy()

inventory_dist_df["LogQohValue"] = np.log1p(
    inventory_dist_df["QohValue"].clip(lower=0)
)

fig5 = px.histogram(
    inventory_dist_df,
    x="LogQohValue",
    nbins=30,
    title="📊 Inventory Value Distribution (Log Scale)"
)

fig5.update_layout(
    height=500,
    xaxis_title="Log Inventory Value",
    yaxis_title="Product Count"
)

# ==================================================
# CHART 6 - INVENTORY EXPOSURE
# ==================================================

overstock_df = (
    filtered_df.sort_values(
        by="QohValue",
        ascending=False
    )
    .head(10)
)

fig6 = px.bar(
    overstock_df,
    x="QohValue",
    y="Name",
    orientation="h",
    title="⚠️ Highest Inventory Exposure Products",
    text_auto=".0f"
)

fig6.update_layout(
    height=500,
    yaxis=dict(categoryorder="total ascending"),
    xaxis_title="Inventory Value",
    yaxis_title="Product"
)

# ==================================================
# DISPLAY CHARTS ROW 3
# ==================================================

col5, col6 = st.columns(2)

with col5:
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    st.plotly_chart(fig6, use_container_width=True)

st.divider()

# ==================================================
# DASHBOARD INSIGHTS
# ==================================================

st.subheader("📈 Business Insights")

c1, c2, c3 = st.columns(3)

with c1:
    st.success(
        f"""
🚀 Fast Movers

Top Product:
{top_products.iloc[0]['Name']}

Units Sold:
{top_products.iloc[0]['SaleTot']:.0f}
"""
    )

with c2:
    st.info(
        f"""
🏢 Revenue Leader

{top_companies.iloc[0]['Company']}

Total Sales:
{top_companies.iloc[0]['SaleTot']:.0f}
"""
    )

with c3:
    st.warning(
        f"""
⚠️ Inventory Exposure

{overstock_count:,} Products

Require inventory review.
"""
    )

# ==================================================
# EXECUTIVE SUMMARY VARIABLES
# ==================================================

high_inventory_product = (
    filtered_df.groupby("Name")["QohValue"]
    .sum()
    .idxmax()
)

# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

st.subheader("🎯 Executive Summary")

st.markdown(
    f"""
### Key Findings

- **{top_products.iloc[0]['Name']}** is the highest selling product with **{top_products.iloc[0]['SaleTot']:.0f} units sold**.

- **{top_companies.iloc[0]['Company']}** is the leading company contributing **{top_companies.iloc[0]['SaleTot']:.0f} units**.

- **{high_inventory_product}** currently carries the highest inventory exposure.

- **{overstock_count:,} products** have stock levels significantly higher than their sales volume.

### Recommended Actions

✅ Prioritize replenishment of fast-moving products.

✅ Monitor high inventory exposure products.

✅ Review overstocked inventory to reduce carrying costs.

✅ Focus procurement planning around top-performing suppliers.
"""
)

# ==================================================
# CONFIDENTIALITY NOTICE
# ==================================================

st.warning(
    """
### Confidentiality Notice

The dataset used in this project contains proprietary medical inventory records and cannot be publicly distributed.

All dashboards, analytics, machine learning models, KPIs, and business insights displayed in this application were developed using the original dataset while maintaining data confidentiality.
"""
)