import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="My Expense Tracker",
    page_icon="💰",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #ffffff 0%,
        #ffd6d6 45%,
        #ff4d4d 100%
    );
    min-height: 100vh;
}

header[data-testid="stHeader"] {
    background: linear-gradient(
        90deg,
        #4a0000,
        #8b0000
    ) !important;
}

div[data-testid="stToolbar"] {
    background: transparent !important;
}

h1 {
    background: linear-gradient(
        90deg,
        #8b0000,
        #c1121f
    ) !important;
    color: white !important;
    text-align: center !important;
    padding: 15px !important;
    border-radius: 10px !important;
    margin-bottom: 20px !important;
}

h2,h3,h4 {
    color: black !important;
    font-weight: bold !important;
}

.expense-heading {
    background: linear-gradient(
        90deg,
        #4a0000,
        #8b0000
    );
    color: white !important;
    padding: 12px;
    border-left: 7px solid #ff1e1e;
    border-radius: 8px;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 15px;
}

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #ffffff 0%,
        #ffd6d6 60%,
        #ffb3b3 100%
    );
    overflow-y: hidden !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1rem !important;
    padding-bottom: 0rem !important;
}

[data-testid="stSidebar"] .expense-heading {
    font-size: 19px;
    padding: 10px;
    margin-bottom: 10px;
}

[data-testid="stSidebar"] label {
    color: black !important;
    font-weight: bold !important;
    font-size: 14px !important;
}

[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
    color: black !important;
    font-weight: bold !important;
}

[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
    color: black !important;
    font-weight: bold !important;
}

[data-testid="stSidebar"] [data-testid="stNumberInput"],
[data-testid="stSidebar"] [data-testid="stTextInput"],
[data-testid="stSidebar"] [data-testid="stDateInput"] {
    margin-bottom: 4px !important;
}

[data-testid="stSidebar"] input {
    min-height: 34px !important;
}

[data-testid="stSidebar"] .stButton {
    margin-top: 8px !important;
}

[data-testid="stSidebar"] .stButton > button {
    height: 38px !important;
    min-height: 38px !important;
    padding: 5px 10px !important;
    background-color: red !important;
    color: white !important;
    border: 2px solid red !important;
    border-radius: 6px !important;
    width: 100%;
    font-weight: bold !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background-color: black !important;
    border-color: black !important;
    color: white !important;
}

[data-testid="stSidebar"] hr {
    margin-top: 8px !important;
    margin-bottom: 8px !important;
    border-color: #8b0000 !important;
}

label {
    color: black !important;
    font-weight: bold !important;
}

div[data-baseweb="input"] {
    border: 1px solid black;
}

.stButton > button {
    background-color: red !important;
    color: white !important;
    border: 2px solid red !important;
    border-radius: 6px !important;
    width: 100%;
    font-weight: bold !important;
}

.stButton > button:hover {
    background-color: black !important;
    color: white !important;
    border: 2px solid black !important;
}

.stButton > button:focus {
    background-color: black !important;
    color: white !important;
}

div[data-testid="stMetric"] {
    background: linear-gradient(
        90deg,
        #4a0000,
        #8b0000
    );
    border-left: 8px solid #ff1e1e;
    border-radius: 8px;
    padding: 18px;
    margin-top: 10px;
    margin-bottom: 20px;
}

div[data-testid="stMetric"] label {
    color: white !important;
    font-size: 24px !important;
    font-weight: bold !important;
}

div[data-testid="stMetricValue"] {
    color: #ff4d4d !important;
    font-size: 30px !important;
    font-weight: bold !important;
}

div[role="menu"] {
    background: #4a0000 !important;
    border: 2px solid #8b0000 !important;
    border-radius: 10px !important;
}

div[data-baseweb="popover"] {
    background: #4a0000 !important;
    border: 2px solid #8b0000 !important;
    border-radius: 10px !important;
}

div[role="menu"] div[role="menuitem"] {
    background: #5c1111 !important;
    color: white !important;
    border-radius: 6px !important;
}

div[role="menu"] div[role="menuitem"] * {
    color: white !important;
}

div[role="menu"] div[role="menuitem"]:hover {
    background: #7a2020 !important;
}

header[data-testid="stHeader"] button:hover {
    background-color: black !important;
    color: white !important;
    border-radius: 6px !important;
}

header[data-testid="stHeader"] button:hover * {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<h1>MY EXPENSE TRACKER 💸</h1>',
    unsafe_allow_html=True
)

csv_path = Path(__file__).parent / "expenses.csv"

try:
    df = pd.read_csv(csv_path)

except FileNotFoundError:

    df = pd.DataFrame(
        columns=[
            "Date",
            "Category",
            "Note",
            "Amount"
        ]
    )

required_columns = [
    "Date",
    "Category",
    "Note",
    "Amount"
]

for column in required_columns:

    if column not in df.columns:
        df[column] = ""

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
).dt.date

df["Amount"] = pd.to_numeric(
    df["Amount"],
    errors="coerce"
).fillna(0)

with st.sidebar:

    st.markdown(
        '<div class="expense-heading">Add Your Expense 👇</div>',
        unsafe_allow_html=True
    )

    amount = st.number_input(
        "Amount (₹)",
        min_value=0,
        step=10,
        value=0
    )

    category = st.text_input(
        "Category"
    )

    date = st.date_input(
        "Date"
    )

    note = st.text_input(
        "Note"
    )

    add_expense = st.button(
        "ADD EXPENSE"
    )

if add_expense:

    if amount <= 0:

        st.sidebar.error(
            "⚠️ Please enter a valid amount."
        )

    elif category.strip() == "":

        st.sidebar.error(
            "⚠️ Please enter a category."
        )

    elif note.strip() == "":

        st.sidebar.error(
            "⚠️ Please enter a note."
        )

    else:

        new_expense = {
            "Date": date,
            "Category": category.strip(),
            "Note": note.strip(),
            "Amount": amount
        }

        df.loc[len(df)] = new_expense

        df.to_csv(
            csv_path,
            index=False
        )

        st.sidebar.success(
            "✅ Expense added!"
        )

        st.rerun()

total_spent = float(
    df["Amount"].sum()
)

st.subheader(
    "TOTAL SPENT"
)

st.metric(
    label="Total amount spent",
    value=f"₹ {total_spent:,.0f}"
)

st.markdown(
    '<div class="expense-heading">Filter Expenses 🔎</div>',
    unsafe_allow_html=True
)

filter_col1, filter_col2, filter_col3 = st.columns(3)

with filter_col1:

    categories = (
        ["All"]
        +
        sorted(
            df["Category"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )
    )

    selected_category = st.selectbox(
        "Filter by Category",
        categories
    )

with filter_col2:

    if not df.empty:

        maximum_amount = int(
            df["Amount"].max()
        )

    else:

        maximum_amount = 0

    min_amount = st.number_input(
        "Minimum Amount (₹)",
        min_value=0,
        value=0,
        step=10
    )

with filter_col3:

    max_amount = st.number_input(
        "Maximum Amount (₹)",
        min_value=0,
        value=maximum_amount,
        step=10
    )

if (
    not df.empty
    and df["Date"].notna().any()
):

    min_date = df["Date"].dropna().min()

    max_date = df["Date"].dropna().max()

else:

    min_date = pd.Timestamp.today().date()

    max_date = pd.Timestamp.today().date()


date_col1, date_col2 = st.columns(2)

with date_col1:

    start_date = st.date_input(
        "From Date",
        value=min_date
    )

with date_col2:

    end_date = st.date_input(
        "To Date",
        value=max_date
    )

filtered_df = df.copy()

if selected_category != "All":

    filtered_df = filtered_df[
        filtered_df["Category"].astype(str)
        == selected_category
    ]

if min_amount <= max_amount:

    filtered_df = filtered_df[
        (filtered_df["Amount"] >= min_amount)
        &
        (filtered_df["Amount"] <= max_amount)
    ]

else:

    st.warning(
        "⚠️ Minimum amount cannot be greater than maximum amount."
    )

    filtered_df = filtered_df.iloc[0:0]

if start_date <= end_date:

    filtered_df = filtered_df[
        (filtered_df["Date"] >= start_date)
        &
        (filtered_df["Date"] <= end_date)
    ]

else:

    st.warning(
        "⚠️ From Date cannot be after To Date."
    )

    filtered_df = filtered_df.iloc[0:0]

st.markdown(
    f"""
    <div style="
        color: #4a0000;
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 10px;
    ">
        Showing {len(filtered_df)} expense(s)
    </div>
    """,
    unsafe_allow_html=True
)

filtered_total = float(
    filtered_df["Amount"].sum()
)

st.subheader(
    "FILTERED TOTAL"
)

st.metric(
    label="Amount after applying filters",
    value=f"₹ {filtered_total:,.0f}"
)

st.subheader(
    "Spending by Category"
)

if not filtered_df.empty:

    category_total = (
        filtered_df
        .groupby("Category")["Amount"]
        .sum()
    )

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    ax.bar(
        category_total.index,
        category_total.values,
        color="red"
    )

    ax.set_xlabel(
        "Category",
        labelpad=8
    )

    ax.set_ylabel(
        "Amount (₹)"
    )

    ax.set_title(
        "Expenses by Category"
    )

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

else:

    st.warning(
        "⚠️ No expenses found for the selected filters."
    )

st.subheader(
    "Recent Expenses"
)

if not filtered_df.empty:

    display_df = (
        filtered_df
        .sort_values(
            by="Date",
            ascending=False
        )
    )

    st.dataframe(
        display_df,
        width="stretch",
        hide_index=True
    )

else:

    st.info(
        "No expenses available to display."
    )