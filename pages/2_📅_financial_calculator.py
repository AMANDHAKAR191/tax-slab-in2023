import streamlit as st
import numpy as np
#from menu import menu_with_redirect

# Render the navigation menu with redirect
#menu_with_redirect()

def calculate_ppf(principal, annual_interest_rate, years):
    total = principal * ((1 + annual_interest_rate / 100) ** years)
    return total

def calculate_epf(monthly_contribution, annual_interest_rate, years):
    total = monthly_contribution * 12 * ((1 + annual_interest_rate / 100) ** years)
    return total

def calculate_fd(principal, annual_interest_rate, years):
    total = principal * ((1 + annual_interest_rate / 100) ** years)
    return total

def calculate_rd(monthly_contribution, annual_interest_rate, years):
    total = monthly_contribution * 12 * years * (years + 1) / 2 + monthly_contribution * 12 * years * annual_interest_rate / 100 * (years + 1) / 2
    return total

def calculate_sip(monthly_investment, annual_interest_rate, years):
    total = monthly_investment * 12 * years * ((1 + annual_interest_rate / 100) ** years - 1) / (annual_interest_rate / 100)
    return total

def calculate_mutual_fund(principal, annual_interest_rate, years):
    total = principal * ((1 + annual_interest_rate / 100) ** years)
    return total

def calculate_emi(loan_amount, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    emi = loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** (years * 12)) / (((1 + monthly_interest_rate) ** (years * 12)) - 1)
    return emi

def main():
    st.title("Income Tax Calculator")
    st.write("Introduction:")
    st.write("Welcome to our Financial Calculator! Whether you're planning for retirement, saving for a major purchase, or managing debt, our comprehensive tool has you covered. With a wide range of financial functions, you can calculate loan payments, investment returns, and much more with ease. Take control of your finances today and achieve your financial goals faster.")
    st.write("Feature:")
    st.write("-Calculate loan payments, including mortgages, auto loans, and personal loans")
    st.write("-Estimate investment returns based on different scenarios and investment vehicles")
    st.write("-Plan for retirement with retirement savings calculators")
    st.write("-Analyze debt repayment strategies to pay off debt faster")
    st.write("-Evaluate lease vs. buy decisions for major purchases")
    st.write("-User-friendly interface with customizable inputs and detailed results")
    st.write("How To Use:")
    st.write("1. Select the financial calculator tool you need based on your specific financial goal.")
    st.write("2. Input relevant details such as loan amount, interest rate, term, investment amount, etc.")
    st.write("3. Adjust inputs to explore different scenarios and compare outcomes.")
    st.write("4. Review the detailed results, including amortization schedules, investment growth projections, and more.")
    st.write("5. Use the insights gained to make informed financial decisions and achieve your objectives.")


    calculator = st.selectbox("Select Calculator:", ("PPF", "EPF", "FD", "RD", "SIP", "Mutual Fund", "EMI"))

    if calculator == "PPF":
        st.subheader("Public Provident Fund (PPF) Calculator")
        principal = st.number_input("Enter Principal Amount:", min_value=0.0, step=1000.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            total_amount = calculate_ppf(principal, annual_interest_rate, years)
            st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    elif calculator == "EPF":
        st.subheader("Employee Provident Fund (EPF) Calculator")
        monthly_contribution = st.number_input("Enter Monthly Contribution:", min_value=0.0, step=100.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            total_amount = calculate_epf(monthly_contribution, annual_interest_rate, years)
            st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    elif calculator == "FD":
        st.subheader("Fixed Deposit (FD) Calculator")
        principal = st.number_input("Enter Principal Amount:", min_value=0.0, step=1000.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            total_amount = calculate_fd(principal, annual_interest_rate, years)
            st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    elif calculator == "RD":
        st.subheader("Recurring Deposit (RD) Calculator")
        monthly_contribution = st.number_input("Enter Monthly Contribution:", min_value=0.0, step=100.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            total_amount = calculate_rd(monthly_contribution, annual_interest_rate, years)
            st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    elif calculator == "SIP":
        st.subheader("Systematic Investment Plan (SIP) Calculator")
        monthly_investment = st.number_input("Enter Monthly Investment:", min_value=0.0, step=100.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            total_amount = calculate_sip(monthly_investment, annual_interest_rate, years)
            st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    elif calculator == "Mutual Fund":
        st.subheader("Mutual Fund Return Calculator")
        principal = st.number_input("Enter Principal Amount:", min_value=0.0, step=1000.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            total_amount = calculate_mutual_fund(principal, annual_interest_rate, years)
            st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    elif calculator == "EMI":
        st.subheader("Equated Monthly Installment (EMI) Calculator")
        loan_amount = st.number_input("Enter Loan Amount:", min_value=0.0, step=1000.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            emi = calculate_emi(loan_amount, annual_interest_rate, years)
            st.write(f"Monthly EMI: {emi:.2f}")
    
    st.write("Our Financial Calculator empowers you to take control of your finances and plan for a secure financial future. Start crunching the numbers now!")

if __name__ == "__main__":
    main()
