if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem

from code.menuitem import MenuItem

def clean_price(price:str) -> float:
    #clean prices by removing $ and , and converting to float
    price = price.replace("$", "")
    price = price.replace(",", "")
    return float(price)

def clean_scraped_text(scraped_text: str) -> list[str]:
    # clean text by removing new lines, lines of text that are "NEW!" or "NEW", and lines of text that are indications of Spicy, Vegan, Gluten-Free or peanut items
    lines = [line.strip() for line in scraped_text.split("\n") if line.strip()]

    # Define unwanted lines
    unwanted_lines = {"NEW!", "NEW", "S", "V", "GS", "P"}

    # Filter out unwanted lines
    cleaned_lines = [line for line in lines if line not in unwanted_lines]

    return cleaned_lines


def extract_menu_item(title:str, scraped_text: str) -> MenuItem:
    cleaned_text = clean_scraped_text(scraped_text)
    item_name = cleaned_text[0]
    item_price = clean_price(cleaned_text[1])
    item_description = cleaned_text[2] if len(cleaned_text) > 2 else "No description available"
    return MenuItem(
        category=title,
        name=item_name, 
        price=item_price, 
        description=item_description 
        )




if __name__=='__main__':
    pass
