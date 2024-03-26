import redis

# Connect to Redis
redis_cli = redis.Redis(host="localhost", port=6379, charset="utf-8", decode_responses=True)

# Gets Redis db size
db_length = redis_cli.dbsize()

# Checks if db length is 0 if true return
if db_length == 0:
    print("No quotes found. Initiate Redis")
    exit()


# Loop will run until user inputs a valid username
while True:
    # Asks the user to input username
    username = input("Enter your name:").strip()
    # Resets loop if username is empty
    if not username:
        print("Username can't be empty, try again.")
    else:
        break

# Asks the user to input a quote
quote = input("Enter a quote:") + "\nAuthor: " + username
# variable for db key
db_name = "Quote:" + str(db_length + 1)

# Adds key value pair to Redis
redis_cli.set(db_name, quote)
print("New quote added to Redis")
