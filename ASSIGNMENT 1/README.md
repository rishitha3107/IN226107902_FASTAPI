# E-commerce Product API

A simple **FastAPI-based E-commerce API** that provides endpoints for managing and viewing products in an online store.

---

## Features

- View all available products  
- Filter products based on category  
- Search products by name (**case-insensitive**)  
- Retrieve only **in-stock products**  
- View **store summary with statistics**  
- Get **best deals** including the cheapest and most expensive products  

---

## Installation

### Clone the Repository

Clone the project repository to your system.

### Create a Virtual Environment

python -m venv venv

### Activate the Virtual Environment

**Windows**

venv\Scripts\activate

**Mac / Linux**

source venv/bin/activate

### Install Dependencies

pip install fastapi uvicorn

---

## Running the Application

Start the FastAPI server with the following command:

uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000

---

## API Endpoints

### Products

**GET /products**  
Returns all available products.

**GET /products/category/{category_name}**  
Filter products by category.

**GET /products/instock**  
Returns only products that are currently in stock.

**GET /products/search/{keyword}**  
Search products by name.

**GET /products/deals**  
Returns the cheapest product (**Best Deal**) and the most expensive product (**Premium Pick**).

---

### Store

**GET /store/summary**  
Returns store statistics including:

- Total products  
- In-stock products  
- Out-of-stock products  
- Available categories  

---

## Testing the API

Open the interactive API documentation in your browser:

http://127.0.0.1:8000/docs

Swagger UI allows you to test all API endpoints easily.

---

## Sample Data

The API contains **7 sample products** across the following categories:

- Electronics  
- Stationery  

Each product includes:

- id  
- name  
- price  
- category  
- in_stock  
