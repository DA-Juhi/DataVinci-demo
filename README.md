# E-Commerce Analytics Pipeline
### Raw store data → a live dashboard that shows what's actually working

A complete, end-to-end analytics pipeline that takes e-commerce data from source to decision: pulled from an API, processed in Python, warehoused in BigQuery, queried with advanced SQL, and delivered as a client-facing Looker Studio dashboard a non-technical owner can read at a glance.

**🔗 [View the live dashboard →](https://datastudio.google.com/reporting/e8aa75d8-6c29-4bb7-826e-613718e7eda9)**

---

## What it does

It mirrors how real data products get built for online stores — the full path from raw source data to a dashboard that drives decisions.

- Fetches product data from a REST API
- Builds a realistic GA4-style dataset — 1,000 web sessions and 55 orders modelled on real e-commerce behaviour
- Loads everything into Google BigQuery
- Runs four analytical SQL queries (JOINs, CTEs, window functions)
- Surfaces the results in a live Looker Studio dashboard

> The session and order data is modelled to mirror real GA4 e-commerce patterns, so the pipeline, queries, and dashboard run exactly as they would on a live store's data.

---

## The pipeline

`REST API → Python → BigQuery → SQL → Looker Studio`

| Stage | Tool | What happens |
|---|---|---|
| Ingest | Python (Requests) | Pull product data from the API |
| Model | Python (Pandas) | Clean data + build GA4-style sessions and orders |
| Warehouse | Google BigQuery | Store as queryable tables |
| Analyse | SQL (JOINs, CTEs, window functions) | Turn rows into business questions |
| Visualise | Looker Studio | Client-facing dashboard |

---

## Data model

| Table | Source | Rows |
|---|---|---|
| `products` | REST API | 20 |
| `ga4_sessions` | Modelled (GA4-style) | 1,000 |
| `orders` | Modelled | 55 |

---

## The questions it answers

1. **Revenue by category** — which product lines actually drive the money *(JOIN + GROUP BY)*
2. **Channel performance** — which marketing channels convert, by revenue and rate *(3-table JOIN)*
3. **Week-over-week revenue** — momentum and trend *(LAG window function + DATE_TRUNC)*
4. **Device performance** — where the funnel leaks *(CTE + LEFT JOIN + conversion analysis)*

All four are saved as reusable BigQuery views in the `ecom` dataset:
`v_revenue_by_category`, `v_channel_performance`, `v_week_over_week`, `v_device_performance`.

---

## What the data revealed

- **Electronics drove 62% of revenue** ($8,648) — a handful of products carrying the store
- **Paid search and email converted at 7%** — the highest-ROI channels
- **Social pulled 201 sessions but converted at just 2%** — high traffic, lowest return
- **Desktop converted 40% better than mobile** — a clear sign of mobile checkout friction worth fixing

Each finding maps to a decision: where to put ad budget, which channel to cut, what to fix in the funnel.

---

## Project structure

```
├── scripts/
│   ├── fetch_python.py      # Pulls products from the API
│   ├── simulate_data.py     # Builds sessions + orders
│   └── upload_to_bq.py      # Loads tables into BigQuery
├── sql/
│   ├── revenue_by_category.sql
│   ├── channel_performance.sql
│   ├── week_over_week.sql
│   └── device_performance.sql
└── README.md
```

---

## Tech stack

Python (Pandas, Requests) · Google BigQuery · SQL · Looker Studio

---

## About

Built by **Juhi Shriwastav** — data analyst working across Excel, SQL, Python, Power BI, BigQuery, and Looker Studio. I build pipelines and dashboards that turn raw data into decisions a business can act on.

**Open to data analyst roles and freelance dashboard / analytics work.**
📧 juhiishriwastav@gmail.com · [LinkedIn](https://linkedin.com/in/juhiiishriwastav)
