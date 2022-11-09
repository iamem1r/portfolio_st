import streamlit as st
import calendar
from datetime import datetime


# ------------- SETTINGS -------------
INCOMES = ['Salary', 'Investment', 'Trade', 'Projects', 'Other incomes']
EXPENSES = ['Rent', 'Bank loan installments', 'Car', 'Utilities', 'Travel',
            'Interest', 'Savings', 'Other expenses']
CURRENCY = 'USD'
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
month = list(calendar.month_name[1:])

with st.form("wallet_form"):
    year_picker_col, month_picker_col = st.columns(2)
    with year_picker_col:
        st.selectbox("Select Year", year, key="year")
    with month_picker_col:
        st.selectbox("Select Year", month, key="month")
    '---'
    with st.expander("Incomes"):
        for income in INCOMES:
            st.number_input(
                f"{income}",
                min_value=0,
                step=50,
                key=income,
                format="%i"
            )
    with st.expander("Expense"):
        for expense in EXPENSES:
            st.number_input(
                f"{expense}",
                min_value=0,
                step=50,
                key=expense,
                format="%i"
            )
    with st.expander("Comments"):
        st.text_area(" ", placeholder="Leave your comments here")

    '---'

    submit_btn = st.form_submit_button("submit")

if submit_btn:
    period = str(str(st.session_state["year"]) + ' ' + st.session_state["month"])
    incomes = {income: st.session_state[income] for income in INCOMES}
    expenses = {expense: st.session_state[expense] for expense in EXPENSES}
    st.write(period)
    st.write(incomes)
    st.write(expenses)
