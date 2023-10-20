from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# Replace 'username' and 'password' with your MySQL username and password
engine = create_engine('mysql://root:csc19454@localhost/sakila')
query = """
SELECT DISTINCT c.first_name, c.last_name
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
WHERE fc.category_id = 8;
"""

import pandas as pd
import matplotlib.pyplot as plt

# Assuming you've executed the modified SQL query and stored the results in rental_data

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a bar chart
plt.bar(rental_data['first_name'] + ' ' + rental_data['last_name'], rental_data['rental_count'])

# Customize the chart
plt.title('Number of Movies Rented by Each Customer from Category 8')
plt.xlabel('Customer Name')
plt.ylabel('Number of Movies Rented')
plt.xticks(rotation=45)  # Rotate customer names for readability

# Display the chart
plt.tight_layout()
plt.show()


query = """
SELECT DATE(rental_date) AS rental_day, COUNT(rental_id) AS rental_count
FROM rental
GROUP BY rental_day;
"""

# Execute the SQL query and load the results into a pandas DataFrame
rental_data = pd.read_sql(query, engine)

# Set the figure size
plt.figure(figsize=(12, 6))

# Create a time-series line chart
plt.plot(rental_data['rental_day'], rental_data['rental_count'], marker='o', linestyle='-')

# Customize the chart
plt.title('Rental Count Over Time')
plt.xlabel('Rental Day')
plt.ylabel('Rental Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability

# Display the chart
plt.tight_layout()
plt.show()