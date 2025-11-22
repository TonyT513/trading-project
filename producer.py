import redis, json, time

r = redis.Redis(host="localhost", port=6379, db=0)

def publish_tick(symbol, bid, ask, ts_ns):
    r.xadd(
        "market_ticks",
        {"symbol": symbol, "bid": bid, "ask": ask, "ts": ts_ns},
        maxlen=100000,
        approximate=True
    )

if __name__ == "__main__":
    publish_tick("AAPL", 150.25, 150.30, int(time.time_ns()))
    print("Tick published to Redis stream")

