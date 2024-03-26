import redis

# Connects to redis
redis_cli = redis.Redis(host="localhost", port=6379, charset="utf-8", decode_responses=True)

# Gets random key from Redis
random_key = redis_cli.randomkey()

# If random_key is None prints text
if random_key is None:
    print("No quotes found. Initiate Redis")
else:
    # Gets value for key
    random_value = redis_cli.get(random_key)

    # Prints the value
    print()
    print("Quote:", random_value)
