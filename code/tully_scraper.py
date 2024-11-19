import re
from playwright.sync_api import Playwright, sync_playwright
#from menuitemextractor import extract_menu_item
#from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    url="https://www.tullysgoodtimes.com/menus/"
    page.goto(url)
    
    # TODO Write code here
    menu_sections = page.query_selector_all("div.foodmenu__menu-section")
    menu_data = []
    for row in menu_sections:
        section_title=row.query_selector("h3.foodmenu__menu-section-title").inner_text()
        items = row.query_selector_all("div.foodmenu__menu-item")

        for item in items:
            item_name = item.query_selector("p.foodmenu__menu-item__name").inner_text()
            item_price = item.query_selector("span.foodmenu__menu-item__price").inner_text()
            item_description = item.query_selector("p.foodmenu__menu-item__desc").inner_text()
            menu_data.append({
                "section": section_title,
                "name": item_name, 
                "price": item_price, 
                "description": item_description})
    # ---------------------
    context.close()
    browser.close()
    for item in menu_data:
        print(item)

with sync_playwright() as playwright:
    tullyscraper(playwright)
