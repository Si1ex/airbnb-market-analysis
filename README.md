# Airbnb Market Analysis

This repository contains a market analysis of Airbnb listings in Stockholm. The analysis includes data preparation, visualization, and correlation analysis to understand the distribution of room types, average room prices, availability, and correlations between different variables.

## Data

For this project, I used the public Airbnb dataset from https://public.opendatasoft.com/explore/dataset/air-bnb-listings/information/?disjunctive.neighbourhood&disjunctive.column_10&disjunctive.city&location=14,59.32467,18.06092&basemap=jawg.light

## Files

- `stockholm_airbnb_analysis.csv`: The cleaned and filtered Airbnb listings data for Stockholm.
- `room_type_distribution.png`: A bar plot showing the distribution of room types in Stockholm.
- `avg_price_neighborhood.png`: A bar plot showing the average room price by neighborhood in Stockholm.
- `avg_availability_neighborhood.png`: A bar plot showing the average availability by neighborhood in Stockholm.
- `correlation_matrix.png`: A heatmap showing the correlation between room price, number of reviews, and availability.

## Setup

To reproduce the analysis, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Si1ex/airbnb-market-analysis.git
    ```

2. Navigate to the repository directory:
    ```bash
    cd airbnb-market-analysis
    ```

3. Ensure you have the necessary Python packages installed:
    ```bash
    pip install pandas matplotlib seaborn
    ```

4. Run the analysis script (provided in the repository).

## Analysis Overview

- **Room Type Distribution**: Visualizes the number of different room types available in Stockholm.
- **Average Room Price by Neighborhood**: Displays the average room price across different neighborhoods.
- **Average Availability by Neighborhood**: Shows the average availability of listings in different neighborhoods.
- **Correlation Matrix**: Analyzes the relationship between room price, number of reviews, and availability.

## Author

- Daniel Kurhinen (and ChatGPT)
