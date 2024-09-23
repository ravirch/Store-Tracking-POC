# 🏬 Store Tracking POC - Sales Analysis

## Project Overview

This project is a **Store Tracking Proof of Concept (POC)** designed to provide sales analysis across multiple stores using a web application with **CRUD** functionality, PostgreSQL as the backend database, and Power BI for **data visualization**. 

The web app enables users to manage and track product sales, while Power BI visualizes sales insights with clear, interactive dashboards.

---

## Key Technologies

- **Flask** (Python) - Web framework for the CRUD-based application.
- **PostgreSQL** - Database for storing products, stores, and sales data.
- **Power BI** - Used for building the interactive sales dashboard.
- **HTML/CSS** - Frontend for the web application.

---

## Features

1. **Web Application**: 
   - Add, edit, delete, and view products, stores, and sales.
   - All data is stored and managed using PostgreSQL.

2. **Power BI Dashboard**:
   - **Total Sales by Store**
   - **Total Sales by Product**
   - **Sales Breakdown by Category**
   - **Sales Trend Over Time**

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/store-tracking-poc.git
   cd store-tracking-poc
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL**:
   - Create a database (e.g., `store_tracking_poc`).
   - Update the database connection URI in `app.py`.

4. **Initialize the Database**:
   ```bash
   flask shell
   from models import db
   db.create_all()
   exit()
   ```

5. **Run the Flask App**:
   ```bash
   python app.py
   ```

6. **Access** the app at `http://127.0.0.1:5000/`.

7. **Power BI**:
   - Open `PowerBI_Report.pbix`.
   - Connect it to your local PostgreSQL database and refresh the data.

---

## Dashboard Preview

![Power BI Dashboard](./screenshots/powerbi_dashboard.png)

---

## License

This project is open-source under the [Open Source License](LICENSE).

---
