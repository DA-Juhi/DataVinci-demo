import os
from google.cloud import bigquery
import pandas as pd

# This tells Python where your secret key file is
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../gcp_key.json'

# Your project details
PROJECT_ID = 'durable-pulsar-477509-k3'
DATASET_ID = 'datavinci_ecom'

# Connect to BigQuery
client = bigquery.Client(project=PROJECT_ID)
print("Connected to BigQuery!")

# Upload products
print("\nUploading products...")
products_df = pd.read_csv('../data/products.csv')
products_df.to_gbq(f'{DATASET_ID}.products', project_id=PROJECT_ID, if_exists='replace')
print(f"products: {len(products_df)} rows uploaded!")

# Upload ga4_sessions
print("\nUploading ga4_sessions...")
sessions_df = pd.read_csv('../data/ga4_sessions.csv')
sessions_df.to_gbq(f'{DATASET_ID}.ga4_sessions', project_id=PROJECT_ID, if_exists='replace')
print(f"ga4_sessions: {len(sessions_df)} rows uploaded!")

# Upload orders
print("\nUploading orders...")
orders_df = pd.read_csv('../data/orders.csv')
orders_df.to_gbq(f'{DATASET_ID}.orders', project_id=PROJECT_ID, if_exists='replace')
print(f"orders: {len(orders_df)} rows uploaded!")

print("\nALL 3 TABLES ARE LIVE IN BIGQUERY!")