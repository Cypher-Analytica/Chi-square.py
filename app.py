# chi_square_streamlit.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Streamlit app title
st.title("Chi-Square Distribution Visualization")

# Sidebar input for degrees of freedom
st.sidebar.header("Chi-Square Parameters")
df = st.sidebar.slider("Degrees of Freedom (df)", min_value=1, max_value=30, value=5, step=1)

# Generate Chi-Square distribution data
x = np.linspace(0, 30, 1000)
y = chi2.pdf(x, df)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f'Chi-Square Distribution (df={df})', color='blue')
plt.fill_between(x, y, color='lightblue', alpha=0.5)
plt.title(f"Chi-Square Distribution with {df} Degrees of Freedom")
plt.xlabel("X")
plt.ylabel("Probability Density")
plt.grid(True)
plt.legend()

# Display the plot
st.pyplot(plt)

# Display additional information
st.write(f"The Chi-Square distribution with {df} degrees of freedom is often used in statistical tests, such as the Chi-Square test for independence.")
