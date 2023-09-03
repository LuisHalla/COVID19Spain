from libs import *
from globals import *

fig, ax = plt.subplots(figsize=(15, 5))

# Plot
ax.plot(ci14, color='b')

# Fill curve
ax.fill_between(df.index.unique(), ci14, alpha=.5, zorder=2)

# Fill waves
colors = list(mcolors.CSS4_COLORS.values())

for i in range(len(waves)-1):
    ax.axvspan(waves[i], waves[i+1], facecolor=colors[i+25], alpha=0.2)

# Set title and yaxis label
ax.set_title("COVID waves in Spain", pad=14, fontdict={'fontsize': 20, 'color': 'black'})
ax.set_ylabel("14-day Cumulative Incidence", labelpad = 14, fontdict={'fontsize': 14, 'color': 'black'})

# Set axis lims
ax.set_ylim([0, 2100])
ax.set_xlim([waves[0], waves[-1]])

# xticks - Wave start and end dates
ax.set_xticks(waves)
ax.tick_params(axis='x', length=6)

xticks_names = ['Jan\n2020', 'Jun\n2020', 'Dec\n2020', 'Mar\n2021', 'Jun\n2021', 'Oct\n2021', 'May\n2023']
ax.set_xticklabels(xticks_names)

# Text - Middlepoint of waves
mid_waves_text = ['1st', '2nd', '3rd', '4th', '5th', '6th - present']

for i in range(len(waves)-1):
    mid_wave = waves[i] + (waves[i+1] - waves[i]) / 2
    ax.text(mid_wave, 1600, mid_waves_text[i], fontdict={'fontsize': 15, 'color': 'black', 'ha':'center'})

# Grid
ax.xaxis.grid(color='gray', linestyle='solid', alpha=0.5)

# Save
plt.savefig('../plots/waves.png', dpi=600)
