from fastapi import FastAPI

app = FastAPI()

# Initial Products List (4 existing + 3 new)
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 99, "category": "Stationery", "in_stock": False},
    {"id": 4, "name": "USB Cable", "price": 199, "category": "Electronics", "in_stock": True},

    # Added products (Q1)
    {"id": 5, "name": "Laptop Stand", "price": 799, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1299, "category": "Electronics", "in_stock": False},
]

# Q1 — Show All Products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }

# Q2 — Filter Products by Category
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):
    filtered_products = [
        product for product in products
        if product["category"].lower() == category_name.lower()
    ]

    if not filtered_products:
        return {"error": "No products found in this category"}

    return {"products": filtered_products}

# Q3 — Show Only In-Stock Products
@app.get("/products/instock")
def get_instock_products():
    instock_products = [product for product in products if product["in_stock"]]

    return {
        "in_stock_products": instock_products,
        "count": len(instock_products)
    }

# Q4 — Store Summary
@app.get("/store/summary")
def store_summary():
    total_products = len(products)
    instock_count = len([product for product in products if product["in_stock"]])
    out_of_stock_count = total_products - instock_count

    categories = list(set(product["category"] for product in products))

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": instock_count,
        "out_of_stock": out_of_stock_count,
        "categories": categories
    }

# Q5 — Search Products by Name
@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    matched_products = [
        product for product in products
        if keyword.lower() in product["name"].lower()
    ]

    if not matched_products:
        return {"message": "No products matched your search"}

    return {
        "matched_products": matched_products,
        "count": len(matched_products)
    }

# ⭐ Bonus — Cheapest & Most Expensive Product
@app.get("/products/deals")
def product_deals():
    cheapest_product = min(products, key=lambda product: product["price"])
    most_expensive_product = max(products, key=lambda product: product["price"])

    return {
        "best_deal": cheapest_product,
        "premium_pick": most_expensive_product
    }
