# Extended BoxPlots (https://github.com/dmey/extended-boxplots)
# Copyright 2018 D. Meyer. Licensed under MIT.

from pathlib import Path

import pytest

import numpy as np
import matplotlib.pyplot as plt

from extended_boxplots import compute_extended_boxplot_stats, plot_extended_boxplot

def test_extended_boxplot():
    dist_norm = np.random.normal(100, 30, 100000)

    boxplot_stats = compute_extended_boxplot_stats(dist_norm)
    fig, ax = plt.subplots()
    plot_extended_boxplot(ax, [boxplot_stats])

    path_to_outdir = Path.cwd() / 'temp'
    path_to_outdir.mkdir(exist_ok=True)
    fig.savefig(path_to_outdir / 'extended_boxplot_test.png', dpi=200)