from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# storage مؤقت للبيانات
traffic_data = []

@app.get("/")
def home():
    return {"message": "Traffic System Running 🚦"}

@app.post("/traffic")
def add_traffic(count: int):
    data = {
        "count": count,
        "time": str(datetime.now())
    }
    traffic_data.append(data)
    return {"status": "added", "data": data}

@app.get("/stats")
def stats():
    total = sum(item["count"] for item in traffic_data)
    return {
        "total_cars": total,
        "records": len(traffic_data)
    }
