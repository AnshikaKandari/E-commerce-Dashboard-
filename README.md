# E-commerce Sales Dashboard

This project provides a Python script to clean and analyze e-commerce sales data from an Amazon sales report. It performs data cleaning, handles missing values, removes duplicates, and generates key performance indicators (KPIs) for sales insights.

## Features

- **Data Cleaning**: Loads the raw CSV dataset, selects relevant columns, handles missing values, removes duplicates, and converts data types.
- **KPI Analysis**: Calculates total sales revenue, monthly sales trends, top categories by sales, and total orders count.
- **Output**: Saves the cleaned dataset to a new CSV file and prints KPI summaries.

## Requirements

- Python 3.x
- Pandas library

## Installation

1. Ensure Python is installed on your system.
2. Install the required library:
   ```
   pip install pandas
   ```

## Usage

1. Place the raw dataset file `AmazonSaleReport.csv` in the project directory.
2. Run the script:
   ```
   python sales.py
   ```
3. The script will process the data and display the results in the console.
4. The cleaned dataset will be saved as `cleaned_AmazonSales.csv`.

## Dataset

The script expects a CSV file with the following relevant columns:
- Order ID
- Date
- Category
- Qty (Quantity)
- Amount (Sales)
- ship-city
- ship-state
- ship-country

Note: The script renames columns for consistency (e.g., 'Amount' to 'Sales', 'Qty' to 'Quantity').

## Output

- **Cleaned Dataset**: `cleaned_AmazonSales.csv` with processed data.
- **Console Output**:
  - Data loading and cleaning steps.
  - Missing values summary.
  - Duplicates removal summary.
  - KPI Analysis including:
    - Total Sales Revenue
    - Monthly Sales Trends
    - Top 5 Categories by Sales
    - Total Orders Count

## Example Output

```
Loading dataset...

Columns in dataset:
Index(['index', 'Order ID', 'Date', 'Status', 'Fulfilment', 'Sales Channel ',
       'ship-service-level', 'Style', 'SKU', 'Category', 'Size', 'ASIN',
       'Courier Status', 'Qty', 'currency', 'Amount', 'ship-city',
       'ship-state', 'ship-postal-code', 'ship-country', 'promotion-ids',
       'B2B', 'fulfilled-by', 'Unnamed: 22'],
      dtype='object')

Checking for missing values...
Order ID         0
Order Date       0
Category         0
Quantity         0
Sales         7795
City            33
State           33
Country         33
dtype: int64

Before removing duplicates: 121149 rows
After removing duplicates: 120107 rows

✅ Cleaned dataset saved as cleaned_AmazonSales.csv

📊 KPI Analysis for Amazon Sales Report

💰 Total Sales (Revenue): 77948774.59

📅 Monthly Sales:
 Order Year  Order Month
2022        3                101683.85
            4              28616442.52
            5              25971513.65
            6              23259134.57
Name: Sales, dtype: float64

📦 Top 5 Categories by Sales:
 Category
Set              38989830.89
kurta            21051705.24
Western Dress    11086930.16
Top               5312913.30
Ethnic Dress       789616.66
Name: Sales, dtype: float64

🛒 Total Orders: 113004
```

## Power BI Dashboard

A dashboard has been created in Power BI using the cleaned dataset (`cleaned_AmazonSales.csv`) to visualize key insights and KPIs. The dashboard includes interactive charts and reports for sales analysis.

### Features of the Dashboard

- **Sales Overview**: Total revenue, monthly trends, and category-wise performance.
- **Geographic Analysis**: Sales distribution by city, state, and country.
- **Order Insights**: Total orders and order trends over time.
- **Interactive Filters**: Filter data by date, category, or location for detailed analysis.

### How to Use the Dashboard

1. Open Power BI Desktop.
2. Load the `cleaned_AmazonSales.csv` file as a data source.
3. Use the pre-built visualizations or create custom reports based on the available columns.
4. Publish the dashboard to Power BI Service for sharing and collaboration.

## License

This project is open-source. Feel free to use and modify as needed.
