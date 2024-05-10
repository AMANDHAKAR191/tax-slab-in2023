import streamlit as st
#from menu import menu_with_redirect

# Render the navigation menu with redirect
#menu_with_redirect()
# global tax_slabs used for calculating tax
tax_slabs = [[250000, 0.], [500000, 10.], [1000000, 20.], [-1, 30.]]

def str_amt_to_float(str_amt):
    '''
    Converts amount in string to float.
    String amount can have anything before and after.
    '''
    digits = []
    for c in str_amt:
        if c.isdigit() or c == ".":
            digits.append(c)
    return float(''.join(digits))

def amt_to_str(amount, currency="INR", end_amount_with="/-"):
    '''
    Converts input amount (in float/decimal) to formatted string with currency.
    '''
    str_amt = "{:,.2f}".format(amount)
    return f"{currency} {str_amt}{end_amount_with}"

def calc_tax(net_taxable_income):
    total_tax_amount = 0.
    for tax_amount, tax_pcnt in tax_slabs:
        taxable_amount_slab = net_taxable_income

        if tax_amount == -1:
            net_taxable_income = 0.
        elif net_taxable_income > tax_amount:
            net_taxable_income -= tax_amount
            taxable_amount_slab = tax_amount
        else:
            net_taxable_income = 0.

        if taxable_amount_slab > 0. :
            taxed_amount = ((taxable_amount_slab * tax_pcnt) / 100.0)
            total_tax_amount += taxed_amount

    return total_tax_amount

def reverse_tax(total_monthly_tax):
    yearly_tax_amount = total_monthly_tax * 12
    last_tax_amt = 0.
    for i in range(100000, 10000000, 10000):
        amt = i + 0.
        tax_amt = calc_tax(amt)

        if yearly_tax_amount >= last_tax_amt and yearly_tax_amount <= tax_amt:
            return amt

        last_tax_amt = tax_amt

def main():
    st.title("S🌟Tax Calculator")
    st.write("Introduction:")
    st.write("Welcome to our Tax Calculator! Our user-friendly tool helps you estimate your taxes quickly and accurately. Whether you're an individual or a business, understanding your tax liability is essential for financial planning. Simply input your income, deductions, and other relevant details to get an instant estimate of your tax obligations.")
    st.write("Feature:")
    st.write("-Calculate taxes for individuals or businesses")
    st.write("-Supports various tax systems (e.g., income tax, sales tax, property tax)")
    st.write("-Customizable inputs for income, deductions, credits, etc.")
    st.write("-Detailed breakdown of tax components")
    st.write("-Option to save or print your results for future reference")
    st.write("How To Use:")
    st.write("1. Enter your income details, including wages, salaries, and any additional sources of income.")
    st.write("2. Input deductions such as mortgage interest, charitable contributions, and other eligible expenses.")
    st.write("3. Specify any tax credits you qualify for, such as education credits or child tax credits.")
    st.write("4. Review your estimated tax liability and adjust inputs as needed.")
    st.write("5. Save or print your results for your records or to share with your accountant.")

    mode = st.radio("Select mode:", ("Calculate Tax", "Reverse Tax"))

    if mode == "Calculate Tax":
        income = st.text_input("Enter net taxable income:")
        if income:
            net_taxable_income = str_amt_to_float(income)
            total_tax_amount = calc_tax(net_taxable_income)
            st.write("Total Tax:", amt_to_str(total_tax_amount))
            st.write("Monthly:", amt_to_str(total_tax_amount / 12))
    elif mode == "Reverse Tax":
        monthly_tax = st.text_input("Enter total monthly tax:")
        if monthly_tax:
            total_monthly_tax = str_amt_to_float(monthly_tax)
            result = reverse_tax(total_monthly_tax)
            if result:
                st.write("Your Taxable Income:", amt_to_str(result))
    
    st.write("Our Tax Calculator provides a convenient way to plan your finances and make informed decisions. Start calculating your taxes now!")


if __name__ == "__main__":
    main()
