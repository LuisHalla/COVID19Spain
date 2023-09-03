from libs import *
from globals import *

fig, ax = plt.subplots(figsize=(12, 7))

# Plots
line1, = ax.plot(vac_percent[:vac_stable], color='b', label='2nd dose vaccination %')

ax.axhspan(vac_percent[vac80], 100,
           facecolor='g', alpha=0.2)
ax.axhspan(vac_percent[vac20], vac_percent[vac80], 0, (vac80 - vac.index[0])/(vac_stable - vac.index[0]),
           facecolor='y', alpha=0.2)

ax.axvspan(vac80, vac_stable,
           facecolor='g', alpha=0.2)
ax.axvspan(vac20, vac80, 0, vac_percent[vac80]/100,
           facecolor='y', alpha=0.2)
ax.axvspan(vac.index[0], vac20, 0, vac_percent[vac20]/100,
           facecolor='tab:orange', alpha=0.4)


# Set title and yaxis labels
ax.set_title("Evolution of fully vaccinated population in 2021 ", pad=14, fontdict={'fontsize': 20, 'color': 'black'})
ax.set_ylabel("Full vaccination %", labelpad = 14, fontdict={'fontsize': 14, 'color': 'black'})

# Set axis lims
ax.set_ylim([0, 100])
ax.set_xlim([vac.index[0], vac_stable])

# yticks
ax.yaxis.set_major_formatter(lambda x, pos: f"{x:.0f}%")

# Legend and text
green_patch = mpatches.Patch(fc='g', ec='k', alpha=0.5, label='None' )
yellow_patch = mpatches.Patch(fc='y', ec='k', alpha=0.5, label='Low' )
orange_patch = mpatches.Patch(fc='tab:orange', ec='k', alpha=0.5, label='Moderate' )

first_legend = ax.legend(handles=[line1], loc='upper left', fontsize='large')
ax.add_artist(first_legend)
ax.legend(handles=[orange_patch, yellow_patch, green_patch], loc='lower right', fontsize='large', title='Risk level')

# left
ax.arrow(18774, 8,
          35.5, 0,
          width=0.7, ec='k', fc='k')
# right
ax.arrow(18774, 8,
          -35, 0,
          width=0.7, ec='k', fc='k')

ax.text(vac20 + (vac80 - vac20)/2, 10,  "11 weeks", ha='center',
        fontdict={'fontsize': 14, 'color': 'k'}) 

# Save
plt.savefig('../plots/vacs.png', dpi=600)
