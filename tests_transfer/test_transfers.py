import allure
from pages.login_page import LoginPage
from pages.accounts_overview_page import AccountsOverviewPage
from pages.transfers_page import TransferPage


@allure.feature("Fund Transfer Workflow")
@allure.story("User can log in, check balance, and successfully transfer funds")
def test_parabank_transfer_funds(browser):
    with allure.step("Log into ParaBank with valid credentials"):
        login_page = LoginPage(browser)
        login_page.login("john", "demo")

    with allure.step("Verify account total balance is $1692.67"):
        accounts_page = AccountsOverviewPage(browser)
        total_balance = accounts_page.get_total_balance()
        assert total_balance == "$1692.67", f"Expected $1692.67, but got {total_balance}"

    with allure.step("Navigate to Transfer Funds and submit a $100 transfer"):
        transfer_page = TransferPage(browser)
        transfer_page.navigate_to_transfer()
        transfer_page.transfer_funds("100")

    with allure.step("Verify success message is displayed"):
        success_msg = transfer_page.get_success_message()
        assert success_msg == "Transfer Complete!", f"Expected 'Transfer Complete!', but got {success_msg}"