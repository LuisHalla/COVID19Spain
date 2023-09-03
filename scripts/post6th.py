from libs import *
from globals import *

fig, ax = plt.subplots(figsize=(12, 7))

# Plots
line1, = ax.plot(ci14[wave6_end:waves[6]], color='b', label='Cumulative incidence')
line2 = ax.axhline(y=250, color='g', linestyle='dashed')
line3 = ax.axhline(y=500, color='y', linestyle='dashed')

ax.axhspan(0, 250, facecolor='g', alpha=0.2)
ax.axhspan(250, 500, facecolor='y', alpha=0.2)
ax.axhspan(500, 1450, facecolor='tab:orange', alpha=0.2)

# Set title and yaxis labels
ax.set_title("Cumulative Incidence over the last year", pad=14, fontdict={'fontsize': 20, 'color': 'black'})
ax.set_ylabel("14-day Cumulative Incidence", labelpad = 14, fontdict={'fontsize': 14, 'color': 'black'})

# Set axis lims
ax.set_ylim([0, 1450])
ax.set_xlim([wave6_end, waves[6].replace(month=waves[6].month+1)])

# yticks
ax.yaxis.set_ticks([0, 250, 500, 750, 1000, 1250])

# Legend and text
green_patch = mpatches.Patch(fc='g', ec='k', alpha=0.5, label='None' )
yellow_patch = mpatches.Patch(fc='y', ec='k', alpha=0.5, label='Low' )
orange_patch = mpatches.Patch(fc='tab:orange', ec='k', alpha=0.5, label='Moderate' )

first_legend = ax.legend(handles=[line1], loc='lower left', fontsize='large')
ax.add_artist(first_legend)
ax.legend(handles=[orange_patch, yellow_patch, green_patch], loc='upper right', fontsize='large', title='Risk level')

ax.text(waves[6].replace(day=waves[6].day+5), ci14[waves[6]],  f"{ci14[waves[6]]:.2f}",
         fontdict={'fontsize': 12, 'color': 'b'})
        
# Grid
ax.yaxis.grid(color='b', linestyle='dashed', alpha=0.1)


# Save
plt.savefig('../plots/post6th.png', dpi=600)
