import json
import requests
import redis

# Connects to redis
redis_cli = redis.Redis(host="localhost", port=6379, charset="utf-8", decode_responses=True)

# If Redis db size is greater than 0 print text and exit
if redis_cli.dbsize() > 0:
    print("Redis already initiated.")
    exit()

# Fetch quotes from website
response = requests.get("https://dummyjson.com/quotes")
# Inputs data in json format
data = json.loads(response.text)
# Gets quotes from data
quotes = data["quotes"]

# Loops through quotes and adds key value pairs to Redis
for i in quotes:
    key = "Quote:" + str(i["id"])
    value = i["quote"] + "\nAuthor: " + i["author"]
    redis_cli.set(key, value)
print("Redis initialized")
