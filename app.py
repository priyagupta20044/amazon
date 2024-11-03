from flask import Flask, render_template, request, jsonify
from apify_client import ApifyClient
import json

app = Flask(__name__)

# Initialize Apify client
APIFY_API_TOKEN = "apify_api_uWrLct7OVyVtlgvtP7xjo8jwWQwtqw3Jnqf0"
apify_client = ApifyClient(APIFY_API_TOKEN)

# Add a debug route to see if the app is working
@app.route('/debug')
def debug():
    return "Hello world! The Flask app is working!"

@app.route('/')
def home():
    # Add some debug information to the home page
    debug_info = {
        "status": "Application is running",
        "flask_version": Flask.__version__,
        "endpoints_available": [
            "/ (HOME)",
            "/debug (Debug info)",
            "/process_url (POST endpoint)"
        ]
    }
    return render_template('index.html', debug_info=debug_info)

@app.route('/process_url', methods=['POST'])
def process_url():
    try:
        # Log the incoming request
        print(f"Received request with data: {request.form}")
        
        url = request.form['url']
        
        # Configure the Apify actor input
        run_input = {
            "addParentData": False,
            "directUrls": [url],
            "enhanceUserSearchWithFacebookPage": False,
            "isUserReelFeedURL": False,
            "isUserTaggedFeedURL": False,
            "resultsLimit": 200,
            "resultsType": "posts",
            "searchLimit": 1,
            "searchType": "hashtag"
        }
        
        print("Starting Apify actor...")
        run = apify_client.actor("apify/instagram-scraper").call(run_input=run_input)
        
        print("Getting dataset items...")
        items = apify_client.dataset(run["defaultDatasetId"]).list_items().items
        
        if not items:
            return jsonify({"error": "No data found for this URL"}), 404
            
        post_data = items[0]
        
        processed_data = {
            "caption": post_data.get('caption', ''),
            "images": post_data.get('imageUrls', []),
            "timestamp": post_data.get('timestamp', ''),
            "likes": post_data.get('likesCount', 0),
            "comments": post_data.get('commentsCount', 0),
            "ownerUsername": post_data.get('ownerUsername', ''),
            "location": post_data.get('location', ''),
            "hashtags": post_data.get('hashtags', []),
            "mentions": post_data.get('mentions', [])
        }
        
        print("Processed data:", json.dumps(processed_data, indent=2))
        return jsonify({"success": True, "data": processed_data})
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True, port=5000)