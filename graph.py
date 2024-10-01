import matplotlib.pyplot as plt
import numpy as np

# Data
events = [
    "Molecule replication (4B years ago)",
    "First human consciousness (2.5M years ago)",
    "Rise of Cro-Magnons (50K years ago)",
    "Invention of civilization (10K years ago)",
    "Invention of printing press (500 years ago)",
    "Invention of computer (50 years ago)",
    "End of timeline (40 years in future)"
]
years = [-4_000_000_000, -2_500_000, -50_000, -10_000, -500, -50, 40]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(events, years, marker='o')

# Labels and title
plt.xlabel("Events")
plt.ylabel("Years (before present or future)")
plt.title("Timeline of Key Events")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right")

# Show the plot
plt.tight_layout()
plt.show()


# Data: time of events (in years before present)
years = [-4_000_000_000, -2_500_000, -50_000, -10_000, -500, -50, 40]

# Calculate time intervals between events
time_intervals = np.diff(years)

# Take the log of the absolute value of time intervals (since some are negative)
log_time_intervals = np.log10(np.abs(time_intervals))

# Data: labels for time intervals
interval_labels = [
    "Molecule replication → First human",
    "First human → Cro-Magnons",
    "Cro-Magnons → Civilization",
    "Civilization → Printing press",
    "Printing press → Computer",
    "Computer → End"
]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(interval_labels, log_time_intervals, marker='o')

# Labels and title
plt.xlabel("Event Transitions")
plt.ylabel("Log10 of Time Interval (years)")
plt.title("Logarithmic Time Intervals Between Key Events")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right")

# Show the plot
plt.tight_layout()
plt.show()

