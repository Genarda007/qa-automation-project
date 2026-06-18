class InventoryPage:
    def __init__(self, page):
        self.page = page

    def get_title(self):
        return self.page.locator(".title").inner_text()

    def get_product_names(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def add_item_to_cart(self, item_name):
        self.page.locator(f"[data-test='add-to-cart-{item_name}']").click()

    def get_cart_count(self):
        return self.page.locator(".shopping_cart_badge").inner_text()

