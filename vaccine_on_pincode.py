import pandas as pd
import matplotlib.pyplot as plt

# Sample data with continent and country information
data = {
    'Continent': ['Asia', 'Europe', 'Africa', 'Asia', 'Europe', 'Africa', 'North America'],
    'Country': ['China', 'France', 'Nigeria', 'India', 'Germany', 'Egypt', 'USA']
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Group the data by continent and count the number of countries in each continent
continent_counts = df['Continent'].value_counts().reset_index()
continent_counts.columns = ['Continent', 'Number of Countries']

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(continent_counts['Continent'], continent_counts['Number of Countries'], color='skyblue')
plt.title('Number of Countries per Continent')
plt.xlabel('Continent')
plt.ylabel('Number of Countries')
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
