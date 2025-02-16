
import requests
from PIL import Image
from io import BytesIO


def get_cat_pic():
    url = "https://api.thecatapi.com/v1/images/search"  # API endpoint
    headers = {
        "x-api-key": "YOUR_OWN_API_KEY"  # Replace with your API key
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        image_url = data[0]["url"]  # Get the image URL
        print("Here's your cat picture URL: ", image_url)
        
        # Fetch the image content using the URL
        image_response = requests.get(image_url)
        
        if image_response.status_code == 200:
            # Open the image from the fetched content
            img = Image.open(BytesIO(image_response.content))
            img.show()  # Display the image
        else:
            print("Failed to download the image. Status code:", image_response.status_code)
    else:
        print("Failed to retrieve cat picture. Status code:", response.status_code)

# Call the function
get_cat_pic()
