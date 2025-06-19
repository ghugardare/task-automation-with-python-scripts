import os
import shutil
import re
import requests

def move_jpg_files():
    source_folder = input("Enter source folder path: ").strip()
    destination_folder = input("Enter destination folder path: ").strip()

    if not os.path.exists(source_folder):
        print("❌ Source folder does not exist.")
        return

    os.makedirs(destination_folder, exist_ok=True)

    count = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, dest_path)
            print(f"Moved: {filename}")
            count += 1

    print(f"✅ Total .jpg files moved: {count}")


def extract_emails():
    input_file = input("Enter the path to the .txt file: ").strip()
    output_file = "emails_found.txt"

    if not os.path.exists(input_file):
        print("❌ Input file not found.")
        return

    with open(input_file, "r") as file:
        text = file.read()

    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

    with open(output_file, "w") as file:
        for email in emails:
            file.write(email + "\n")

    print(f"✅ Extracted {len(emails)} emails to '{output_file}'")


def scrape_web_title():
    url = input("Enter a URL (e.g., https://example.com): ").strip()
    try:
        response = requests.get(url, timeout=10)
        title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)

        if title_match:
            title = title_match.group(1)
            with open("page_title.txt", "w") as file:
                file.write(title)
            print(f"✅ Page title saved: '{title}'")
        else:
            print("❌ No title found on the page.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching page: {e}")


def main():
    while True:
        print("\n🔧 Python Automation Toolkit")
        print("1. Move all .jpg files to another folder")
        print("2. Extract emails from a .txt file")
        print("3. Scrape title from a webpage")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_web_title()
        elif choice == "4":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
