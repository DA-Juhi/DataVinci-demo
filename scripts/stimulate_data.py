import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# So we get the same "random" data every time we run
random.seed(42)
np.random.seed(42)

print("Loading products...")
products = pd.read_csv('C:\Juhi the DATA ANALYAT!\DataVinci-demo\data/products.csv')

# ============================================================
# TABLE 1 — GA4 SESSIONS (1000 rows)
# Who visited the website and how
# ============================================================
print("Simulating 1000 GA4 sessions...")

NUM_SESSIONS = 1000

# These are the exact channels DataVinci tracks for real clients
channels = ['organic', 'paid_search', 'social', 'email', 'direct']
channel_weights = [0.35, 0.25, 0.20, 0.10, 0.10]  # organic is always highest

# DataVinci's clients are US/EU/SG based - this matches their real work
countries = ['US', 'UK', 'DE', 'SG', 'AU']
country_weights = [0.45, 0.20, 0.15, 0.12, 0.08]

devices = ['mobile', 'desktop', 'tablet']
device_weights = [0.55, 0.35, 0.10]  # mobile always dominates

# Generate random dates across 3 months (Jan - Mar 2024)
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=random.randint(0, 89)) for _ in range(NUM_SESSIONS)]

# Build the sessions table row by row
sessions = []
for i in range(NUM_SESSIONS):
    channel = random.choices(channels, weights=channel_weights)[0]
    device = random.choices(devices, weights=device_weights)[0]
    country = random.choices(countries, weights=country_weights)[0]

    # Email and paid search convert better than social - realistic business logic!
    if channel == 'email':
        conversion_chance = 0.08
    elif channel == 'paid_search':
        conversion_chance = 0.06
    elif channel == 'organic':
        conversion_chance = 0.05
    elif channel == 'direct':
        conversion_chance = 0.07
    else:  # social
        conversion_chance = 0.03

    # Desktop converts better than mobile - classic e-commerce insight
    if device == 'desktop':
        conversion_chance *= 1.4
    elif device == 'tablet':
        conversion_chance *= 1.1

    converted = 1 if random.random() < conversion_chance else 0
    pages_viewed = random.randint(3, 12) if converted else random.randint(1, 5)

    sessions.append({
        'session_id': f'sess_{str(i+1).zfill(4)}',
        'user_id': f'user_{str(random.randint(1, 700)).zfill(3)}',
        'channel': channel,
        'device': device,
        'country': country,
        'session_date': dates[i].strftime('%Y-%m-%d'),
        'pages_viewed': pages_viewed,
        'converted': converted
    })

sessions_df = pd.DataFrame(sessions)
print(f"Sessions created: {len(sessions_df)}")
print(f"Total conversions: {sessions_df['converted'].sum()} ({sessions_df['converted'].mean()*100:.1f}% conversion rate)")



# ============================================================
# TABLE 2 — ORDERS (one order per converted session)
# What they actually bought
# ============================================================

print("\nSimulating orders for every converted session...")

converted_sessions = sessions_df[sessions_df['converted'] == 1].copy()

orders = []
for idx, session in converted_sessions.iterrows():

    # Pick a random product from our REAL products table
    product = products.sample(1).iloc[0]
    quantity = random.choices([1, 2, 3], weights=[0.70, 0.20, 0.10])[0]
    revenue = round(product['price_usd'] * quantity, 2)

    orders.append({
        'order_id': f'ord_{str(len(orders)+1).zfill(4)}',
        'session_id': session['session_id'],  # links back to sessions table
        'user_id': session['user_id'],
        'product_id': int(product['product_id']),  # links back to products table
        'quantity': quantity,
        'revenue': revenue,
        'order_date': session['session_date']
    })

orders_df = pd.DataFrame(orders)
print(f"Orders created: {len(orders_df)}")
print(f"Total revenue: ${orders_df['revenue'].sum():,.2f}")
print(f"Average order value: ${orders_df['revenue'].mean():.2f}")

# ============================================================
# SAVE BOTH TO CSV
# ============================================================
sessions_df.to_csv('C:\Juhi the DATA ANALYAT!\DataVinci-demo\data/ga4_sessions.csv', index=False)
orders_df.to_csv('C:\Juhi the DATA ANALYAT!\DataVinci-demo\data/orders.csv', index=False)

print("\nSUCCESS! Files saved:")
print("  data/ga4_sessions.csv")
print("  data/orders.csv")
print("\nPreview of sessions:")
print(sessions_df.head(3))
print("\nPreview of orders:")
print(orders_df.head(3))