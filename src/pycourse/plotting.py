import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="white")

def plot_corr_heatmap(eeg_df, output_path):
    cols = [c for c in eeg_df.columns if c != "time"]
    data = eeg_df[cols]
    corr = data.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    fig.savefig(output_path)
