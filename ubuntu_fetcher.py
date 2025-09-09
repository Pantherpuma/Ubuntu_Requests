import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # Prompt user for image URL
    url = input("Enter the image URL: ").strip()

    # Create directory for images
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Fetch image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If filename is empty, generate one
        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join(folder, filename)

        # Save image in binary mode
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"✅ Image successfully saved as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL. Please include http:// or https://")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")

    except requests.exceptions.RequestException as err:
        print(f"❌ Connection error: {err}")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
