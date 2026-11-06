import json
import os
import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    print("\n--- Scraping Quotes from Sandbox Site ---")
    url = "http://quotes.toscrape.com/"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes_data = []

    # Extract quotes, authors, and tags
    quote_elements = soup.find_all('div', class_='quote')
    
    for element in quote_elements:
        text = element.find('span', class_='text').get_text(strip=True)
        author = element.find('small', class_='author').get_text(strip=True)
        tag_elements = element.find_all('a', class_='tag')
        tags = [tag.get_text(strip=True) for tag in tag_elements]
        
        quotes_data.append({
            "quote": text,
            "author": author,
            "tags": tags
        })

    print(f"Successfully scraped {len(quotes_data)} quotes!")
    return quotes_data

def save_to_json(data, filename="scraped_quotes.json"):
    if not data:
        print("No data to save.")
        return
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to JSON file: {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    while True:
        print("\n--- Project 04: Web Scraper for Headlines & Quotes ---")
        print("1. Scrape Quotes and Save to JSON")
        print("2. View Scraped JSON File Content")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            data = scrape_quotes()
            if data:
                save_to_json(data)
                # Print preview of first 3 items
                print("\nPreview of Scraped Data:")
                for i, item in enumerate(data[:3], 1):
                    print(f"{i}. \"{item['quote']}\" — *{item['author']}*")
        elif choice == '2':
            filename = "scraped_quotes.json"
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                print(f"\nLoaded {len(content)} items from {filename}:")
                for i, item in enumerate(content[:3], 1):
                    print(f"{i}. {item['author']}: {item['quote'][:60]}...")
            else:
                print(f"File '{filename}' not found. Run the scraper first.")
        elif choice == '3':
            print("Exiting Web Scraper. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
