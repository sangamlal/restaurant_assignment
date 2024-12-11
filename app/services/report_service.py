from sqlalchemy.orm import Session
from app.models.order import Order
from datetime import datetime
import json

def generate_sales_report(start_date: str, end_date: str, db: Session):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    orders = db.query(Order).filter(Order.created_at.between(start, end)).all()

    total_revenue = 0
    item_counts = {}
    for order in orders:
        items = json.loads(order.items)
        for item in items:
            total_revenue += item["price"] * item["quantity"]
            item_counts[item["name"]] = item_counts.get(item["name"], 0) + item["quantity"]

    most_popular_items = sorted(item_counts, key=item_counts.get, reverse=True)[:5]
    return {
        "total_revenue": total_revenue,
        "number_of_orders": len(orders),
        "most_popular_items": most_popular_items
    }
