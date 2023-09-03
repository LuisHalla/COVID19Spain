from libs import *
from globals import *

fig, axs = plt.subplots(2, figsize=(12, 10))

# Plots
axs[0].plot(df.groupby('date').positive.sum().cumsum(), color='b', label='Positive tests')
axs[0].set_title("Total COVID cases", pad=14, fontdict={'fontsize': 20, 'color': 'black'})


axs[1].plot(df.groupby('date').hosp.sum().cumsum(), color='tab:orange', label='Hospitalized')
axs[1].plot(df.groupby('date').death.sum().cumsum(), color='r', label='Deceased')
axs[1].set_title("Total hospitalizations and deaths due to COVID", pad=14, fontdict={'fontsize': 20, 'color': 'black'})

for ax in axs.flat:
    
    # Grid
    ax.yaxis.grid(color='b', linestyle='dashed', alpha=0.1)
    
# Labels
axs[0].set_ylabel("Total cases", labelpad = 14, fontdict={'fontsize': 14, 'color': 'black'})
axs[1].set_ylabel("Total hospitalizations and deaths", labelpad = 14, fontdict={'fontsize': 14, 'color': 'black'})

# yticks
axs[0].yaxis.set_major_formatter(lambda x, pos: f"{x/1e6:.1f}M")
axs[1].yaxis.set_major_formatter(lambda x, pos: f"{x/1e3:.0f}K")

# lims
axs[0].set_xlim([df.index[0], df.index[-1]])
axs[1].set_xlim([df.index[0], df.index[-1]])

axs[0].set_ylim([0, 35e5])
axs[1].set_ylim([0, 50e4])

# Legend and text
axs[0].legend(loc='upper left', fontsize='large')
axs[1].legend(loc='upper left', fontsize='large')

fig.tight_layout(h_pad=4)

# Save
plt.savefig('../plots/cum_no_vac.png', dpi=600)
