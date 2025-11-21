from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "OK"}

class TradeRequest(BaseModel):
    ticker: str
    action: str  # "buy" or "sell"
    quantity: int

@app.post("/trade")
def trade(request: TradeRequest):
    return {
        "message": "Trade endpoint placeholder",
        "ticker": request.ticker,
        "action": request.action,
        "quantity": request.quantity
    }

