

# Prodigy Infotech Data Science Internship Task 01

## Introduction
This repository contains a Python script that visualizes the distribution of ages and genders in a population using histograms and bar charts. The script utilizes the `matplotlib` and `numpy` libraries to generate random data and create informative plots.

## Requirements
- Python 3.x
- NumPy
- Matplotlib

## Usage
1. Clone the repository: `git clone https://github.com/your_username/PRODIGY_DS_01.git`
2. Navigate to the project directory: `cd PRODIGY_DS_01`
3. Open the Jupyter Notebook or run the Python script.

The script will generate two plots:
1. A histogram displaying the distribution of ages in the population.
2. A bar chart showing the distribution of genders in the population.

## Code Explanation

### Importing Libraries
```python
import matplotlib.pyplot as plt
import numpy as np
```
The script imports the required libraries: `matplotlib.pyplot` for plotting and `numpy` for numerical operations.

### Generating Age Data
```python
ages = np.random.normal(loc=35, scale=10, size=10000).astype(int)
```
This line generates a random sample of 10,000 ages from a normal distribution with a mean of 35 and a standard deviation of 10. The ages are then converted to integers.

### Plotting Age Distribution
```python
plt.figure(figsize=(8,6))
plt.hist(ages, bins=range(0,100,5), edgecolor='black', linewidth=1)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Ages')
plt.tight_layout()
plt.show()
```
These lines create a histogram to visualize the distribution of ages. The `plt.hist` function is used to plot the histogram, with the `bins` parameter specifying the age ranges. The plot is customized with labels, a title, and a tight layout. Finally, `plt.show()` displays the plot.

### Generating Gender Data
```python
genders = np.random.choice(['Male', 'Female'], size=10000)
```
This line generates a random sample of 10,000 genders, with each value being either 'Male' or 'Female'.

### Plotting Gender Distribution
```python
gender_counts = [len(genders[genders=='Male']), len(genders[genders=='Female'])]

plt.figure(figsize=(6,4))
plt.bar(['Male', 'Female'], gender_counts, edgecolor='black', linewidth=1)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Genders')
plt.show()
```
These lines create a bar chart to visualize the distribution of genders. The `gender_counts` list stores the counts of 'Male' and 'Female' genders. The `plt.bar` function is used to plot the bar chart, with the gender labels and corresponding counts as input. The plot is customized with labels, a title, and displayed using `plt.show()`.

Note: The provided code generates random data for demonstration purposes. To visualize real-world data, replace the `ages` and `genders` variables with your actual data.

## Contributions
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments
- [Yash Raj](https://github.com/KING-OF-FLAME) - Creator and Maintainer
- Special thanks to the Prodigy Infotech team for providing this internship opportunity.

