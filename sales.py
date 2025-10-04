import pandas as pd

def clean_amazon_data(input_file, output_file):
    # 1. Load dataset
    print("Loading dataset...")
    df = pd.read_csv(input_file)

    # 2. Columns check
    print("\nColumns in dataset:")
    print(df.columns)

    # 3. Keep only useful columns if they exist
    useful_cols = ['Order ID', 'Date', 'Category', 'Qty', 'Amount', 'ship-city', 'ship-state', 'ship-country']
    df = df[useful_cols]

    # Rename columns for consistency
    df = df.rename(columns={
        'Date': 'Order Date',
        'Amount': 'Sales',
        'Qty': 'Quantity',
        'ship-city': 'City',
        'ship-state': 'State',
        'ship-country': 'Country'
    })

    # 4. Missing values remove
    print("\nChecking for missing values...")
    print(df.isnull().sum())
    df = df.dropna()

    # 5. Remove duplicates
    print(f"\nBefore removing duplicates: {len(df)} rows")
    df = df.drop_duplicates()
    print(f"After removing duplicates: {len(df)} rows")

    # 6. Correct data types
    if 'Order Date' in df.columns:
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    if 'Ship Date' in df.columns:
        df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
    if 'Sales' in df.columns:
        df['Sales'] = df['Sales'].astype(float)
    if 'Profit' in df.columns:
        df['Profit'] = df['Profit'].astype(float)

    # 7. New columns - Year & Month
    if 'Order Date' in df.columns:
        df['Order Year'] = df['Order Date'].dt.year
        df['Order Month'] = df['Order Date'].dt.month

    # 8. Profit Margin calculate
    if 'Profit' in df.columns and 'Sales' in df.columns:
        df['Profit Margin %'] = (df['Profit'] / df['Sales']) * 100

    # 9. Save cleaned dataset
    df.to_csv(output_file, index=False)
    print(f"\n✅ Cleaned dataset saved as {output_file}")

    # ----------------- KPI Analysis -----------------
    print("\n📊 KPI Analysis for Amazon Sales Report\n")

    # Total Sales
    total_sales = df['Sales'].sum()
    print("💰 Total Sales (Revenue):", round(total_sales, 2))

    # Total Profit
    if 'Profit' in df.columns:
        total_profit = df['Profit'].sum()
        print("🏦 Total Profit:", round(total_profit, 2))

    # Monthly Revenue Trend
    if 'Order Year' in df.columns and 'Order Month' in df.columns:
        monthly_sales = df.groupby(['Order Year','Order Month'])['Sales'].sum()
        print("\n📅 Monthly Sales:\n", monthly_sales)

    # Top Categories by Sales
    if 'Category' in df.columns:
        top_categories = df.groupby('Category')['Sales'].sum().sort_values(ascending=False).head(5)
        print("\n📦 Top 5 Categories by Sales:\n", top_categories)

    # Region-wise Sales
    if 'Region' in df.columns:
        region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
        print("\n🌍 Region-wise Sales:\n", region_sales)

    # Orders Count
    if 'Order ID' in df.columns:
        order_count = df['Order ID'].nunique()
        print("\n🛒 Total Orders:", order_count)


if __name__ == "__main__":
    input_file = "AmazonSaleReport.csv"      # Your dataset
    output_file = "cleaned_AmazonSales.csv"   # Cleaned output
    clean_amazon_data(input_file, output_file)
