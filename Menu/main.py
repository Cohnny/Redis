import json
import requests
import redis


def main():
    # Connects to redis
    redis_cli = redis.Redis(host="localhost", port=6379, charset="utf-8", decode_responses=True)

    while True:
        db_length = redis_cli.dbsize()
        print()
        print("Database length:", db_length)
        print("\nMenu")
        print("1. Initiate Redis")
        print("2. Get random quote")
        print("3. Add quote")
        print("0. Exit")

        choice = input("Enter choice: ")
        if choice == "0":
            print()
            print("Exiting...")
            break
        elif choice == "1":
            init_db(redis_cli)
        elif choice == "2":
            get_quote(redis_cli)
        elif choice == "3":
            add_quote(redis_cli)
        else:
            print("Invalid input, try again.")


def init_db(redis_cli):
    # If Redis db size is greater than 0 print text and exit
    if redis_cli.dbsize() > 0:
        print("Redis already initiated.")
        return

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


def get_quote(redis_cli):
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


def add_quote(redis_cli):
    # Gets Redis db size
    db_length = redis_cli.dbsize()

    # Checks if db length is 0 if true return
    if db_length == 0:
        print("No quotes found. Initiate Redis")
        return

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


if __name__ == "__main__":
    main()
