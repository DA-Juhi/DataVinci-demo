import requests
import pandas as pd

print("Fetching products from API...")
response = requests.get("https://fakestoreapi.com/products")
products = response.json()

df = pd.DataFrame(products)

df = df[['id', 'title', 'price', 'category', 'rating']]

df['rating_score'] = df['rating'].apply(lambda x: x['rate'])
df['rating_count'] = df['rating'].apply(lambda x: x['count'])
df = df.drop(columns=['rating'])

df = df.rename(columns={
    'id': 'product_id',
    'title': 'product_name',
    'price': 'price_usd',
    'category': 'category'
})

df.to_csv('C:\Juhi the DATA ANALYAT!\DataVinci-demo\data/products.csv', index=False)

print(f"\n SUCCESS! Fetched {len(df)} products from the API")
print("\nHere's a preview:")
print(df.head())
print("\nCategories found:", df['category'].unique())