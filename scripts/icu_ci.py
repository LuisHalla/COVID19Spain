from libs import *
from globals import *

fig, ax1 = plt.subplots(figsize=(15, 5))
ax2 = ax1.twinx()

# Plots
line1, = ax1.plot(ci14[waves[1]:wave6_end], color='b', label='Cumulative incidence')
line2, = ax2.plot(icu_ocup[waves[1]:wave6_end], color='r', label='ICU occupation %')
line3 = ax1.axvline(x=vac80, color='g', linestyle='dashed', label='Full vaccination +80%')

ax1.axvspan(vac80, wave6_end, facecolor='g', alpha=0.2)

# Set title and yaxis labels
ax1.set_title("Cumulative Incidence and ICU occupation due to COVID", pad=14, fontdict={'fontsize': 20, 'color': 'black'})
ax1.set_ylabel("14-day Cumulative Incidence", labelpad = 14, fontdict={'fontsize': 14, 'color': 'black'})
ax2.set_ylabel("ICU occupation percentage", labelpad = 14, fontdict={'fontsize': 14, 'color': 'black'})

# Set axis lims
ax1.set_ylim([0, 2100])
ax2.set_ylim([0, 55])
ax1.set_xlim([waves[1], wave6_end])

# yticks
ax2.yaxis.set_major_formatter(lambda x, pos: f"{x:.0f}%")

# Legend and text
ax1.legend(handles=[line1, line2, line3], loc='upper left', fontsize='large')
ax2.text(vac80.replace(day=vac80.day+5), 26, 'Full vaccination +80%',
         fontdict={'fontsize': 12, 'color': 'k', 'rotation':'vertical'})
        
# Grid
ax1.yaxis.grid(color='b', linestyle='dashed', alpha=0.1)

# Save
plt.savefig('../plots/icu_ci.png', dpi=600)
