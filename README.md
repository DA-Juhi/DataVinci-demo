# E-Commerce Digital Analytics Pipeline
### API → Python → BigQuery → Looker Studio

---

## What is this project?
A complete end-to-end analytics pipeline that mirrors exactly how DataVinci Private Limited builds data products for their US and European e-commerce clients.

I fetched real product data from a REST API, simulated 1000 GA4-style website sessions and 55 purchase orders, stored everything in Google BigQuery, wrote 4 advanced SQL queries, and visualised the insights in a Looker Studio dashboard.

---

## The Pipeline
REST API → Python → BigQuery → SQL → Looker Studio

---

## Tech Stack
| Tool | Purpose |
|------|---------|
| Python (Pandas, Requests) | API fetch, data cleaning, simulation |
| Fake Store API | Real product data (20 products) |
| Google BigQuery | Cloud data warehouse |
| SQL (Joins, CTEs, Window Functions) | Business insight queries |
| Looker Studio | Client-facing dashboard |

---

## The 3 Tables
| Table | Source | Rows |
|-------|--------|------|
| products | Fake Store API — real data | 20 |
| ga4_sessions | Python simulated | 1000 |
| orders | Python simulated | 55 |

---

## SQL Queries Written
1. **Revenue by Category** — JOIN + GROUP BY + SUM
2. **Channel Performance** — 3-table JOIN + conversion rate
3. **Week-over-Week Revenue** — LAG() window function + DATE_TRUNC
4. **Device Performance** — CTE + LEFT JOIN + conversion analysis

---

## Key Business Insights Found
- Electronics drives 62% of total revenue ($8,648)
- Paid search and email convert at 7% — highest performing channels
- Social media converts at only 2% despite 201 sessions — lowest ROI
- Desktop converts 40% better than mobile — checkout friction on mobile

---

## BigQuery Views Created
All 4 queries saved as Views in dataset `datavinci_ecom`:
- `v_revenue_by_category`
- `v_channel_performance`
- `v_week_over_week`
- `v_device_performance`

---

## Live Dashboard
[View Looker Studio Dashboard](#) ← will update after May 5

---

## Project Structure

├── scripts/
│   ├── fetch_python.py       # Fetches products from API
│   ├── simulate_data.py      # Generates sessions + orders
│   └── upload_to_bq.py       # Uploads tables to BigQuery
├── sql/
│   ├── revenue_by_category.sql
│   ├── channel_performance.sql
│   ├── week_over_week.sql
│   └── device_performance.sql
└── README.md

---

## About
Built by **Juhi Shriwastav** — targeting Junior Data Analyst role at DataVinci Private Limited.

[LinkedIn](https://linkedin.com/in/juhiiishriwastav)