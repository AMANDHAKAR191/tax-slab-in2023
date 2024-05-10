import streamlit as st

def main():
    st.set_page_config(
    page_title="Calculator App",
    page_icon=":moneybag",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
    )
    # st.set_page_config(page_title="Calculator App", layout="wide", page_icon=":moneybag",)

    st.title("Welcome to the Calculator App!")
    st.write("Introduction:")
    st.write("Welcome to our Financial Calculator Hub! Here, you'll find a suite of powerful calculators designed to help you navigate various financial scenarios with confidence. Whether you're budgeting, planning for retirement, or preparing your taxes, our collection of tools has everything you need to make informed decisions and achieve your financial goals.")
    st.write("Explore our range of calculators below:")
    st.write("1. *Tax Calculator:* Estimate your tax liability accurately and efficiently. Whether you're an individual or a business, our Tax Calculator simplifies the process of calculating taxes, providing you with instant insights into your tax situation.")
    st.write("2. *Financial Calculator:* Take control of your finances with our comprehensive Financial Calculator. From loan payments to investment returns, retirement planning to debt repayment strategies, our tool covers a wide range of financial scenarios, empowering you to make smarter financial decisions.")
    st.write("3. *Income Tax Calculator:* Calculate your income taxes with ease using our Income Tax Calculator. Whether you're an employee, freelancer, or small business owner, our intuitive tool helps you determine your taxable income, deductions, credits, and potential refunds, making tax preparation simpler and more efficient.")
    st.write("Features of our Financial Calculator Hub:")
    st.write("- Access all calculators in one convenient location")
    st.write("- User-friendly interface with customizable inputs and detailed results")
    st.write("- Real-time calculations for instant insights")
    st.write("- Comprehensive coverage of various financial scenarios")
    st.write("- Option to save or print results for future reference")
    st.write("Whether you're a financial novice or an experienced investor, our Financial Calculator Hub is your go-to resource for all your financial planning needs. Start exploring our calculators today and take the first step towards financial success!")


if __name__ == "__main__":
    main()
