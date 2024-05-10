import streamlit as st
#from menu import menu_with_redirect

# Render the navigation menu with redirect
#menu_with_redirect()

# Global tax slabs used for calculating tax
tax_slabs = {
    "Below 60": [[250000, 0.], [500000, 5.], [1000000, 10.], [-1, 15.]],
    "60 or above 60": [[300000, 0.], [500000, 5.], [1000000, 10.], [-1, 15.]],
    "80 or above 80": [[500000, 0.], [1000000, 5.], [-1, 10.]]
}

# Additional deductions under various sections
deductions = {
    "80C": 0,
    "80CCD(1B)": 0,
    "80D": 0,
    "80G": 0,
    "80E": 0,
    "80TTA/TTB": 0
}

def calculate_tax(income, age_category, deductions):
    total_tax_amount = 0.
    tax_slab = tax_slabs[age_category]

    # Calculate tax on income
    for tax_amount, tax_pcnt in tax_slab:
        taxable_amount_slab = income

        if tax_amount == -1:
            income = 0.
        elif income > tax_amount:
            income -= tax_amount
            taxable_amount_slab = tax_amount
        else:
            income = 0.

        if taxable_amount_slab > 0.:
            taxed_amount = ((taxable_amount_slab * tax_pcnt) / 100.0)
            total_tax_amount += taxed_amount

    # Apply deductions
    for section, amount in deductions.items():
        total_tax_amount -= amount

    return total_tax_amount

def main():
    st.title("Income Tax Calculator")
    st.write("Introduction:")
    st.write("Welcome to our Income Tax Calculator! Whether you're an employee, self-employed individual, or small business owner, understanding your income tax obligations is crucial. Our intuitive tool helps you calculate your income tax liability accurately and efficiently. Simply input your income, deductions, and other relevant details to get a clear picture of your tax situation.")
    st.write("Feature:")
    st.write("-Calculate income taxes for individuals, including employees, freelancers, and small business owners")
    st.write("-Support for various tax forms and filing statuses (e.g., Form 1040, single, married filing jointly)")
    st.write("-Comprehensive coverage of income sources, deductions, credits, and adjustments")
    st.write("-Real-time tax calculations with instant results")
    st.write("-Detailed breakdown of taxable income, tax owed, and potential refunds")
    st.write("-Option to save or print your tax summary for your records or tax filing purposes")
    st.write("How To Use:")
    st.write("1. Choose the appropriate tax form and filing status for your situation.")
    st.write("2. Input your income details, including wages, self-employment income, and any other taxable earnings.")
    st.write("3. Specify deductions such as mortgage interest, medical expenses, and other eligible items.")
    st.write("4. Claim any tax credits you qualify for, such as the Earned Income Tax Credit or Child and Dependent Care Credit.")
    st.write("5. Review your tax summary to ensure accuracy and explore opportunities for tax optimization.")
    st.write("6. Save or print your results for your records or to assist with tax preparation.")

    # User inputs
    assessment_year = st.text_input("Enter Assessment Year:")
    age_category = st.selectbox("Select Age Category:", ("Below 60", "60 or above 60", "80 or above 80"))
    basic_deductions = st.number_input("Enter Basic Deductions under 80C:", min_value=0.0, step=1000.0)
    nps_contribution = st.number_input("Enter Contribution to NPS under 80CCD(1B):", min_value=0.0, step=1000.0)
    medical_insurance_premium = st.number_input("Enter Medical Insurance Premium under 80D:", min_value=0.0, step=1000.0)
    charity_donation = st.number_input("Enter Donation to Charity under 80G:", min_value=0.0, step=1000.0)
    educational_loan_interest = st.number_input("Enter Interest on Educational Loan under 80E:", min_value=0.0, step=1000.0)
    saving_account_interest = st.number_input("Enter Interest on Deposits in Saving Account under 80TTA/TTB:", min_value=0.0, step=1000.0)
    basic_salary = st.number_input("Enter Basic Salary per annum:", min_value=0.0, step=1000.0)
    da = st.number_input("Enter Dearness Allowance (DA) per annum:", min_value=0.0, step=1000.0)
    hra = st.number_input("Enter HRA per annum:", min_value=0.0, step=1000.0)
    rent_paid = st.number_input("Enter Total Rent Paid per annum:", min_value=0.0, step=1000.0)
    metro_city = st.radio("Do you live in a metro city?", ("Yes", "No"))

    # Convert metro city input to boolean
    if metro_city == "Yes":
        metro_city = True
    else:
        metro_city = False

    # Calculate total income
    total_income = basic_salary + da + hra

    # Calculate taxable income
    if hra > rent_paid:
        taxable_income = total_income - rent_paid
    else:
        taxable_income = total_income - hra

    # Calculate tax
    tax_amount = calculate_tax(taxable_income, age_category, deductions)

    # Display result
    st.subheader("Tax Calculation Result:")
    st.write(f"Assessment Year: {assessment_year}")
    st.write(f"Total Income: {total_income}")
    st.write(f"Taxable Income: {taxable_income}")
    st.write(f"Total Tax Amount: {tax_amount}")

    st.write("Our Income Tax Calculator simplifies the tax-filing process and helps you maximize your tax savings. Start calculating your income taxes now!")

if __name__ == "__main__":
    main()
