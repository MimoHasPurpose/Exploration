import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set an interactive backend
plt.switch_backend('TkAgg')  # Alternatives: 'Qt5Agg', 'wxAgg'

# Sample data
l = np.random.randn(100)

# Create the plot
sns.histplot(l, kde=True)

# Display the plot
plt.show()
