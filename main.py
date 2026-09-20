from itertools import product
from unicodedata import category
from pyscript import document, display


def create_order(e):
    poké_puffs = document.getElementById("item1")
    brock_special_stew = document.getElementById("item2")
    malasadas = document.getElementById("item3")
    decorative_curry = document.getElementById("item4")
    rich_plenty_of_apples_toast_curry = document.getElementById("item5")

    subtotal = float(poké_puffs.value) * float(poké_puffs.checked) + float(brock_special_stew.value) * float(brock_special_stew.checked) + float(malasadas.value) * float(malasadas.checked) + float(decorative_curry.value) * float(decorative_curry.checked) + float(rich_plenty_of_apples_toast_curry.value) * float(rich_plenty_of_apples_toast_curry.checked)

    VAT = subtotal * 0.12
    total = subtotal + VAT

    display(f"Your subtotal is: ₱{subtotal: .2f}", target="show")
    display(f"Your VAT is: ₱{VAT: .2f}", target="show")
    display(f"Your total is: ₱{total: .2f}", target="show")


def generate_sku(e):
    product = document.getElementById("product_name")
    category = document.getElementById("category")
    stock = document.getElementById("stock_quantity")

    sku = category.value + "-" + product.value[:3].upper() + "-" + stock.value

    document.getElementById("sku-output").innerText = sku