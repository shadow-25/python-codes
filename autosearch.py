import time
import webbrowser
import random

# List of random search queries
search_queries = [
    "cute kittens",
    "recipe for chocolate cake",
    "interesting facts about space",
    "best hiking trails near me",
    "how to grow tomatoes",
    "funny cat videos",
    "popular tourist destinations",
    "healthy breakfast ideas",
    "world's tallest buildings",
    "famous historical events",
    # Add more search queries as desired
]

# Set the number of searches you want to perform
total_searches = 30

search_delay = random.randint(5, 15)  # Random delay between 3 and 12 seconds

def perform_random_search():
    # Choose a random search query
    random_query = random.choice(search_queries)

    # Construct the Bing search URL
    search_url = f"https://www.bing.com/search?q={random_query}"

    # Open the default browser with the search URL
    webbrowser.open(search_url)

if __name__ == "__main__":
    print(f"Performing {total_searches} random Bing searches...")
    for _ in range(total_searches):
        perform_random_search()
        time.sleep(search_delay)

    print("All searches completed. Enjoy exploring!")
