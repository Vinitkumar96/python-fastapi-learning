def serial(record) -> dict:
    return {
        "id": str(record["_id"]),
        "title": record["title"],
        "amount": record["amount"],
        "type": record["type"],
        "category": record["category"],
        "date": record["date"]
    }
