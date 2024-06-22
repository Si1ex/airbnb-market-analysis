import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Load dataset
df = pd.read_csv('{"PATH_TO_TO_DATA"}', encoding="ISO-8859-1", delimiter=';', low_memory=False)

# Display first few rows and data info
df.head()
df.info()

# Filter data for Stockholm
stockholm_listings = df.query("City == 'Stockholm'")
stockholm_listings.info()

# Handle missing values (example: drop rows with missing prices)
stockholm_listings = stockholm_listings.dropna(subset=['Room Price'])

# Convert data types if necessary (example: convert Room Price to float)
stockholm_listings['Room Price'] = stockholm_listings['Room Price'].astype(float)

# Room type distribution
room_type_counts = stockholm_listings['Room type'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=room_type_counts.index, y=room_type_counts.values, palette='viridis')
plt.title('Distribution of Room Types in Stockholm')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.savefig('/content/airbnb-market-analysis/room_type_distribution.png')
plt.show()

# Average room price by neighborhood
avg_price_neighborhood = stockholm_listings.groupby('Neighbourhood')['Room Price'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
avg_price_neighborhood.plot(kind='bar', color='skyblue')
plt.title('Average Room Price by Neighborhood in Stockholm')
plt.xlabel('Neighborhood')
plt.ylabel('Average Room Price')
plt.xticks(rotation=90)
plt.savefig('/content/airbnb-market-analysis/avg_price_neighborhood.png')
plt.show()

# Average availability by neighborhood
avg_availability_neighborhood = stockholm_listings.groupby('Neighbourhood')['Availibility'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
avg_availability_neighborhood.plot(kind='bar', color='orange')
plt.title('Average Availability by Neighborhood in Stockholm')
plt.xlabel('Neighborhood')
plt.ylabel('Average Availability')
plt.xticks(rotation=90)
plt.savefig('/content/airbnb-market-analysis/avg_availability_neighborhood.png')
plt.show()

# Correlation matrix
corr_matrix = stockholm_listings[['Room Price', 'Number of reviews', 'Availibility']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.savefig('/content/airbnb-market-analysis/correlation_matrix.png')
plt.show()

# Save dataframe to CSV
stockholm_listings.to_csv('/content/airbnb-market-analysis/stockholm_airbnb_analysis.csv', index=False)