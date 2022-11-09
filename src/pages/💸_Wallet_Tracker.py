import streamlit as st


# ------------- SETTINGS -------------
INCOMES = ['Salary', 'Investment', 'Trade', 'Projects', 'Other incomes']
EXPENSES = ['Rent', 'Bank loan installments', 'Car', 'Utilities', 'Travel',
            'Interest', 'Savings', 'Other expenses']
CURRENCY = 'IRR'
PAGE_TITLE = 'WALLET TRACKER'
PAGE_ICON = '💸'


# ---------- Config & Title -----------
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout='centered')
st.title(PAGE_TITLE + "\t" + PAGE_ICON)
st.markdown("""
Wallet Tracker is an open-source project that allows you to track your wallet balances and transactions.

Wallet Tracker is designed to be easy to use and easy to extend.
""")
'---'

# -------------- Forms -----------------
