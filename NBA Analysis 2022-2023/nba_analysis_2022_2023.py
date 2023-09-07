
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the NBA data
nba_data = pd.read_csv('path/to/your/NBA Team Stats.csv')

# Filter data for the 2022-2023 season
season_filter = '2022-2023'
top_10_3pt_2022_2023 = nba_data[nba_data['Season'] == season_filter].nlargest(10, '3P%')
top_10_fg_2022_2023 = nba_data[nba_data['Season'] == season_filter].nlargest(10, 'FG%')

# Function to save dataframe as an image (for creating tables)
def save_df_as_image(df, title, filename):
    from pandas.plotting import table
    fig, ax = plt.subplots(figsize=(8, 2)) 
    ax.set_frame_on(False) 
    ax.xaxis.set_visible(False) 
    ax.yaxis.set_visible(False) 
    tab = table(ax, df, loc='center', colWidths=[0.2]*len(df.columns))
    tab.auto_set_font_size(False)
    tab.set_fontsize(12)
    tab.scale(1.8, 1.8)
    plt.title(title, fontsize=14, weight='bold')
    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close()

# Create and save heatmaps as images (for the blog post)
def create_and_save_heatmaps(top_10_3pt, top_10_fg, paths):
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
    sns.heatmap(top_10_3pt.set_index('TEAM')[['3P%']], annot=True, fmt=".1f", cmap='YlGnBu', cbar=True, ax=ax[0])
    ax[0].set_title('Top 10 Teams in 3-Point Percentage (2022-2023)')
    ax[0].set_xlabel('3-Point Percentage')
    ax[0].set_ylabel('Team')
    sns.heatmap(top_10_fg.set_index('TEAM')[['FG%']], annot=True, fmt=".1f", cmap='YlGnBu', cbar=True, ax=ax[1])
    ax[1].set_title('Top 10 Teams in Field Goal Percentage (2022-2023)')
    ax[1].set_xlabel('Field Goal Percentage')
    ax[1].set_ylabel('Team')
    plt.tight_layout()
    plt.savefig(paths[0])
    plt.savefig(paths[1])
    plt.close()

# Specify paths to save the heatmaps
heatmap_paths = ['path/to/save/3pt_heatmap.png', 'path/to/save/fg_heatmap.png']

# Create and save the heatmaps
create_and_save_heatmaps(top_10_3pt_2022_2023, top_10_fg_2022_2023, heatmap_paths)
