import requests
from PIL import Image
from io import BytesIO

# Function to fetch and convert the image to a specified format
def fetch_and_convert_image(image_url, output_format='PNG'):
    try:
        # Fetch image from the URL
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful

        # Open the image and convert it
        img = Image.open(BytesIO(response.content))
        
        # Save the image in the desired format (PNG, JPG, or JPEG)
        output_filename = f"product_image.{output_format.lower()}"
        img.save(output_filename, format=output_format)
        
        print(f"Image saved as {output_filename}")
        return output_filename
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the image: {e}")
        return None
    except Exception as e:
        print(f"Error processing the image: {e}")
        return None

# Example usage
image_url = "https://media.croma.com/image/upload/v1694713300/Croma%20Assets/Communication/Wearable%20Devices/Images/300848_0_hyu5ar.png"  # Replace with the actual image URL
output_format = 'PNG'  # Desired output format (can be 'PNG', 'JPEG', or 'JPG')

# Fetch and convert the image
fetch_and_convert_image(image_url, output_format)
