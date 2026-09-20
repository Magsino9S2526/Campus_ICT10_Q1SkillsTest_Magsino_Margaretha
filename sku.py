from pyscript import display, document

def generate_sku(e):
    category = document.getElementById('category')
    product_name = document.getElementById('product_name')
    stock = document.getElementById('stock')

    category_value = category.value
    product_value = product_name.value
    stock_value = stock.value

    if category_value == '' or product_value == '' or stock_value == '':
        display('Please fill in all fields.', target='sku_result')
        return

    category_code = category_value[:3].upper()
    product_code = product_value[:3].upper()

    sku = f'{category_code}-{product_code}-{stock_value}'

    display(f'Your SKU is: {sku}', target='sku_result')
