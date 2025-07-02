import plotly.express as px
import pandas as pd

# Get the data from the sentiment analysis table
df = q.cells("Sentiment_Analysis_Data")

# Create a bar chart
fig = px.bar(df, x='Sentiment', y='Count', 
             title='Distribution of Customer Reviews by Sentiment',
             color='Sentiment',
             color_discrete_map={'Positive': '#1f77b4', 'Negative': '#d62728', 'Neutral': '#ff7f0e'},
             labels={'Sentiment': 'Sentiment Category', 'Count': 'Number of Reviews'})

# Update the layout for a more professional look
fig.update_layout(
    xaxis_title='Sentiment Category',
    yaxis_title='Number of Reviews',
    title_x=0.5,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(
        family="Arial, sans-serif",
        size=12,
        color="#7f7f7f"
    )
)

# Show the chart
fig.show()
