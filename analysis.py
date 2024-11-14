import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Sample data (can be replaced by input from a file or database)
data = {
    'comments': [
        "Great product, really loved it!",
        "Not worth the price, poor quality",
        "Excellent value for money. Highly recommend!",
        "The product broke within a week, very disappointed"
    ],
    'likes': [100, 50, 200, 30],
    'engagement': [120, 60, 220, 35],
    'hashtags': ["#awesome", "#notworthit", "#valueformoney", "#disappointed"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Function to perform sentiment analysis
def analyze_sentiment(comment):
    analysis = TextBlob(comment)
    return analysis.sentiment.polarity

# Add sentiment score to DataFrame
df['sentiment'] = df['comments'].apply(analyze_sentiment)

# Analyze and display sentiment analysis results
positive_comments = df[df['sentiment'] > 0]
negative_comments = df[df['sentiment'] < 0]
neutral_comments = df[df['sentiment'] == 0]

# Scope of improvement
improvement_suggestions = {
    'positive_feedback': positive_comments['comments'].tolist(),
    'negative_feedback': negative_comments['comments'].tolist(),
    'neutral_feedback': neutral_comments['comments'].tolist()
}

# Print feedback summary
print("Positive Feedback:\n", improvement_suggestions['positive_feedback'])
print("\nNegative Feedback:\n", improvement_suggestions['negative_feedback'])
print("\nNeutral Feedback:\n", improvement_suggestions['neutral_feedback'])

# Plot likes vs. engagement
plt.figure(figsize=(8, 6))
plt.scatter(df['likes'], df['engagement'], c=df['sentiment'], cmap='coolwarm')
plt.title('Likes vs. Engagement with Sentiment Analysis')
plt.xlabel('Likes')
plt.ylabel('Engagement')
plt.colorbar(label='Sentiment Score')
plt.show()

# Output trendy hashtags
hashtag_counts = df['hashtags'].value_counts()
print("\nTrendy Hashtags:\n", hashtag_counts)

# Recommendations based on analysis
print("\nSuggestions for Improvement:")
if len(negative_comments) > 0:
    print("- Focus on addressing quality issues, as highlighted in negative feedback.")
if len(positive_comments) > 0:
    print("- Promote positive aspects and keep engaging with satisfied customers.")
if len(positive_comments) == 0:
    print("- Work on creating a better product to increase positive sentiment.")
