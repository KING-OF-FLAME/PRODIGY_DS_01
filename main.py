# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Load age data (replace with actual data)
ages = np.random.normal(loc=35, scale=10, size=10000).astype(int)

# Create histogram
plt.figure(figsize=(8,6))
plt.hist(ages, bins=range(0,100,5), edgecolor='black', linewidth=1)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Ages')
plt.tight_layout()
plt.show()

# Load gender data (replace with actual data)
genders = np.random.choice(['Male', 'Female'], size=10000)

# Create bar chart for gender counts
gender_counts = [len(genders[genders=='Male']), len(genders[genders=='Female'])]

plt.figure(figsize=(6,4))
plt.bar(['Male', 'Female'], gender_counts, edgecolor='black', linewidth=1)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Genders')
plt.show()
