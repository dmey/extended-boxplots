# Extended BoxPlots

Extended box plots are a type of box plots that draws multiple boxes at different percentile pairs.
There is no concept of whiskers or outliers. See page 31 of [Principles of Graph Construction](http://biostat.mc.vanderbilt.edu/wiki/pub/Main/StatGraphCourse/graphscourse.pdf) by Frank E Harrell Jr for more info.


## Usage

```py
import numpy as np
import matplotlib.pyplot as plt

from extended_boxplots import compute_extended_boxplot_stats, plot_extended_boxplot

# Create sample normal distribution
dist_norm = np.random.normal(100, 30, 100000)

# Compute extended box plot statistics
boxplot_stats = compute_extended_boxplot_stats(dist_norm)

# Plot the extended box plot
fig, ax = plt.subplots()
plot_extended_boxplot(ax, [boxplot_stats])
fig.savefig('extended_boxplot.svg', dpi=200)
```

![Example extended box plot](images/extended_boxplot.svg)

## Versioning

This project uses [semantic versioning](https://semver.org/).


## Copyright and licence

Copyright 2018 D. Meyer. Licensed under [MIT](LICENSE.txt).