import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

# Display the first few rows of the dataset
print(iris_df.head())

# Check for missing values
print(iris_df.isnull().sum())

# Check data types
print(iris_df.dtypes)

# Summary statistics
print(iris_df.describe())

# Visualize relationships between variables
# Scatter plot of sepal length vs sepal width
plt.figure(figsize=(8, 6))
colors = {'setosa': 'r', 'versicolor': 'g', 'virginica': 'b'}
for species, color in colors.items():
    species_subset = iris_df[iris_df['species'] == species]
    plt.scatter(species_subset['sepal_length'], species_subset['sepal_width'], color=color, label=species)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Length vs Sepal Width')
plt.legend()
plt.show()

# Boxplot to visualize distribution of each variable by species
plt.figure(figsize=(10, 6))
iris_df.boxplot(column=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], by='species', grid=False)
plt.title("Distribution of Variables by Species")
plt.suptitle("")
plt.show()
