import streamlit as st
import calendar
from datetime import datetime


# ------------- SETTINGS -------------
INCOMES = ['Salary', 'Investment', 'Trade', 'Projects', 'Other incomes']
EXPENSES = ['Rent', 'Bank loan installments', 'Car', 'Utilities', 'Travel',
            'Interest', 'Savings', 'Other expenses']
CURRENCY = 'IRR'
PAGE_TITLE = 'WALLET TRACKER'
PAGE_ICON = ':dollar:'


# ---------- Config & Title -----------
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout='centered'
)
st.title(PAGE_TITLE + "\t" + PAGE_ICON)
st.markdown("""
Wallet Tracker is an open-source project that allows you to track your wallet
balances and transactions.

Wallet Tracker is designed to be easy to use and easy to extend.
""")

'---'

# -------------- Forms -----------------
year = [datetime.now().year - 1, datetime.now().year, datetime.now().year + 1]
month = list(calendar.month())

# with st.form("wallet_form"):
#     year, month = st.columns(2)
#     year = st.selectbox("Select Year", datetime.now().year)
st.write(year)
st.write(month)
