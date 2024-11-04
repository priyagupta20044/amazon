import flask
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
APIFY_TOKEN = 'apify_api_uWrLct7OVyVtlgvtP7xjo8jwWQwtqw3Jnqf0'  # Replace with your actual Apify token

@app.route('/')
def home():
    return render_template('index.html')  # Create a basic HTML form in index.html

@app.route('/scrape', methods=['POST'])
def scrape_instagram():
    url = request.form.get('url')
    
    if url:
        # Run the Instagram scraper Actor
        result = run_instagram_scraper(url)
        return jsonify(result)
    else:
        return jsonify({"error": "No URL provided"}), 400

def run_instagram_scraper(url):
    # Define the Apify API endpoint and input data for the Actor
    api_url = f"https://api.apify.com/v2/acts/apify~instagram-api-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "directUrls": [url],  # URL of the Instagram post to scrape
        "resultsType": "posts",
        "resultsLimit": 10
    }
    
    # Send POST request to run the Actor
    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        # Return the JSON response if the request was successful
        return response.json()
    else:
        return {"error": "Failed to fetch data from Apify API"}

if __name__=='__main__':
    app.run(debug=True)