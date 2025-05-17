# ☁️ Retail Sales Analytics on AWS Cloud

This project demonstrates a complete cloud analytics pipeline using AWS services: ingesting sales data to S3, transforming it via Glue, querying with Athena, and visualizing with QuickSight.

## 🛠 Tech Stack
- AWS S3
- AWS Glue
- AWS Athena
- AWS QuickSight
- Python
- Apache Airflow (optional)

## 📁 Project Structure
- `data/raw_sales_data.csv` - Sample sales data
- `glue_jobs/transform_sales_data.py` - Glue ETL script
- `athena_queries/monthly_sales.sql` - SQL to query processed data
- `dashboard/` - (Optional) QuickSight visuals

## 🚀 Flow
1. Upload `raw_sales_data.csv` to S3.
2. Run Glue job to transform and output Parquet files.
3. Use Athena to query sales summaries.
4. Create dashboards in QuickSight.

## 📈 Sample Insights
- Total revenue by region and product
- Monthly sales trend
- Product performance dashboard

