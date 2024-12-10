import matplotlib.pyplot as plt
import numpy as np

# Data
categories = [
    "Pronghorn", "Coyote", "Small Mammals", "Elk", "Woody Plants",
    "Stream Morphology", "Beaver", "Birds", "Berries", "Bear", 
    "Scavengers", "Wolf"
]
proportions_increase = [
    0.99, 0.01, 0.99, 0.14, 0.88, 0.88, 0.88, 0.88, 0.88, 0.74, 0.14, 1.0
]
proportions_decrease = [1 - p for p in proportions_increase]

# Bar width
bar_width = 0.5
y_positions = np.arange(len(categories))

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(y_positions, proportions_increase, color='orange', label="Increase")
ax.barh(y_positions, proportions_decrease, left=proportions_increase, color='blue', label="Decrease")

# Aesthetics
ax.set_yticks(y_positions)
ax.set_yticklabels(categories)
ax.set_xlabel("Proportion of Outcomes")
ax.set_title("Proportion of Models with Increased and Decreased Populations")
ax.legend(loc="lower right")
plt.gca().invert_yaxis()  # Reverse order to match typical visualization style

# Show plot
plt.tight_layout()
plt.show()