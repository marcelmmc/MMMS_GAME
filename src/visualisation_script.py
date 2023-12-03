import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from kbhmap import Heatmap

# Load statistics data
statistics = pd.read_csv('statistics.csv')

# Extract mistyped keys data
mistyped = statistics.loc[statistics['type'] == 'mistyped']['value'].values[0].strip("][").split(', ')
mistyped = [w.replace("'", '') for w in mistyped]

# Create Heatmap object
HMQ = Heatmap('qwerty')
chars = mistyped
unique, count = np.unique([char for char in chars], return_counts=True)
char_dict = dict(zip(unique, count))


# Plot WPM comparison
plt.subplot(2, 2, 2)
your_wpm = float(statistics.loc[statistics['type'] == 'wpm']['value'].values[0])
counts_wpm = [15, 25, your_wpm, 35]
indices_wpm = np.argsort(counts_wpm)
levels_wpm = ['beginner', 'intermediate', 'YOU', 'expert']
bar_colors_wpm = ['tab:green', 'tab:orange', 'tab:blue', 'tab:red']
plt.bar([levels_wpm[i] for i in indices_wpm], [counts_wpm[i] for i in indices_wpm], label=[levels_wpm[i] for i in indices_wpm], color=[bar_colors_wpm[i] for i in indices_wpm])
plt.ylabel('WPM (words per minute)')
plt.title('WPM comparison')

# Plot Accuracy comparison
plt.subplot(2, 2, 3)
your_accuracy = float(statistics.loc[statistics['type'] == 'accuracy']['value'].values[0])
counts_accuracy = [80, 85, your_accuracy, 90]
indices_accuracy = np.argsort(counts_accuracy)
levels_accuracy = ['beginner', 'intermediate', 'YOU', 'expert']
bar_colors_accuracy = ['tab:green', 'tab:orange', 'tab:blue', 'tab:red']
plt.bar([levels_accuracy[i] for i in indices_accuracy], [counts_accuracy[i] for i in indices_accuracy], label=[levels_accuracy[i] for i in indices_accuracy], color=[bar_colors_accuracy[i] for i in indices_accuracy])
plt.ylabel('Accuracy')
plt.title('Accuracy comparison')

# Load saving data
saving = pd.read_csv('saving.csv')
saving['Time_Difference'] = saving['Time_Difference'].abs()

# Plot Latency per hand
plt.subplot(2, 2, 4)
grouped = saving.groupby('side_to_side')['Time_Difference'].mean()
counts_latency = list(grouped.values)
indices_latency = np.argsort(counts_latency)
levels_latency = list(grouped.index)
bar_colors_latency = ['tab:green', 'tab:orange', 'tab:blue', 'tab:red']
plt.bar([levels_latency[i] for i in indices_latency], [counts_latency[i] for i in indices_latency], label=[levels_latency[i] for i in indices_latency], color=[bar_colors_latency[i] for i in indices_latency])
plt.ylabel('Average latency')
plt.title('Latency per hand')

# Adjust layout
plt.tight_layout()

# Show the combined plot
HMQ = Heatmap('qwerty')
chars = mistyped
unique,count = np.unique([char for char in chars],return_counts=True)
char_dict = dict(zip(unique,count))

HMQ.make_heatmap(char_dict,layout='qwerty',cmap='YlGnBu',sigmas=0.1)
plt.title('Mistyped keys');

plt.show()

