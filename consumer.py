import redis

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Read the latest tick from the stream
msgs = r.xread({"market_ticks": "0"}, count=10)

for stream, entries in msgs:
    for msg_id, fields in entries:
        tick = {k.decode(): v.decode() for k, v in fields.items()}
        print(f"Received tick {msg_id}: {tick}")

