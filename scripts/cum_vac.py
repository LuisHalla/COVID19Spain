from libs import *
from globals import *

fig, axs = plt.subplots(2, figsize=(12, 10))

# Plots
axs[0].plot(df.groupby('date').positive.sum().cumsum(), color='b', label='Positive tests')
axs[0].set_title("Total COVID cases", pad=14, fontdict={'fontsize': 20, 'color': 'black'})

axs[0].axvspan(vac80, df.index[-1], facecolor='tab:blue', alpha=0.2)

axs[1].plot(df.groupby('date').hosp.sum().cumsum(), color='tab:orange', label='Hospitalized')
axs[1].plot(df.groupby('date').death.sum().cumsum(), color='r', label='Deceased')
axs[1].set_title("Total hospitalizations and deaths due to COVID", pad=14, fontdict={'fontsize': 20, 'color': 'black'})

axs[1].axvspan(vac80, df.index[-1], facecolor='tab:orange', alpha=0.2)

for ax in axs.flat:
    #Lines
    ax.axvline(x=vac80, color='g', linestyle='dashed', label='Full vaccination +80%')
    
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

# Text
axs[0].text(vac80.replace(day=vac80.day+10), 16e5, 'Full vaccination +80%',
         fontdict={'fontsize': 12, 'color': 'k', 'rotation':'vertical'})


positive_ratio = df[:vac80].groupby('date').positive.sum().sum() / df.groupby('date').positive.sum().sum()
hosp_ratio = df[:vac80].groupby('date').hosp.sum().sum() / df.groupby('date').hosp.sum().sum()
death_ratio = df[:vac80].groupby('date').death.sum().sum() / df.groupby('date').death.sum().sum()

axs[0].text(19300, 1.7e6,  f'{(1-positive_ratio)*100:.0f}% of\ntotal cases',
         fontdict={'fontsize': 20, 'color': 'k', 'ha': 'center'})

axs[1].text(19000, 39e4,  f'{(1-hosp_ratio)*100:.0f}% of total\nhospitalizations',
         fontdict={'fontsize': 20, 'color': 'k', 'ha': 'center'})

axs[1].text(19350, 15e4,  f'{(1-death_ratio)*100:.0f}% of\ntotal deaths',
         fontdict={'fontsize': 20, 'color': 'k', 'ha': 'center'})
    
fig.tight_layout(h_pad=4)

# Save
plt.savefig('../plots/cum_vac.png', dpi=600)
