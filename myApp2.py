from apify_client import ApifyClient

apify_client = ApifyClient('apify_api_uWrLct7OVyVtlgvtP7xjo8jwWQwtqw3Jnqf0')

# Start an Actor and wait for it to finish
actor_call = apify_client.actor('RB9HEZitC8hIUXAha').call()

# Fetch results from the Actor run's default dataset
dataset_items = apify_client.dataset(actor_call['defaultDatasetId']).list_items().items
for item in apify_client.dataset(actor_call["defaultDatasetId"]).iterate_items():
    print(item)