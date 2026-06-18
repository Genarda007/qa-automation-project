from dbm import error

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "wrongpassword")
    error_message = page.locator("[data-test='error']").inner_text()
    assert "Username and password do not match" in error_message

def test_locked_out_user(page):
    login = LoginPage(page)
    login.navigate()
    login.login("locked_out_user", "secret_sauce")
    error_message = page.locator("[data-test='error']").inner_text()
    assert "Sorry, this user has been locked out" in error_message

def test_inventory_title(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    title = inventory.get_title()
    assert title == "Products"

def test_add_item_to_cart(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.add_item_to_cart("sauce-labs-backpack")
    count = inventory.get_cart_count()
    assert count == "1"

    
