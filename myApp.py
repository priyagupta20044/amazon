from apify_client import ApifyClient 

# Initialize the Apify client with your API token
apify_client = ApifyClient('apify_api_uWrLct7OVyVtlgvtP7xjo8jwWQwtqw3Jnqf0')
dataset = apify_client.dataset('r9baUUubWSO4HRAbh')
dataset_items = dataset.list_items()

# Open a text file in write mode
with open("output/results.txt", "w", encoding="utf-8") as file:
    
    # Write captions to the file
    for item in dataset_items.items:
        file.write(f"Caption: {item.get('caption')}\n")
    
    # Write alt texts from childPosts to the file
    for item in dataset_items.items:
        if item.get('childPosts') and len(item['childPosts']) > 0:
            file.write(f"Image Content: {item['childPosts'][0].get('alt')}\n")
    
    # Write comments count to the file
    for item in dataset_items.items:
        file.write(f"Comments Count: {item.get('commentsCount')}\n")
    
    # Write the first comment to the file
    for item in dataset_items.items:
        file.write(f"First Comment: {item.get('firstComment')}\n")
    
    # Write latest comments (if any) to the file
    for item in dataset_items.items:
        if item.get('latestComments'):
            file.write("Latest Comments:\n")
            for comment in item['latestComments']:
                file.write(f"{comment.get('ownerUsername')}: {comment.get('text')}\n")
        file.write("\n" + "-"*50 + "\n\n")  # Separator between items
