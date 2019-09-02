from matplotlib import pyplot as pl
import numpy as np

tinv = [
        1.35,
        1.3,
        1.25,
        1.22,
        1.2,
        1.1,
        1.05,
        1.0,
        0.95,
        0.9,
        0.875,
        0.825,
        0.8,
        0.775,
        0.7
        ]

mu = [
      6e0,
      2e0,
      4e-1,
      1.5e-1,
      1e-1,
      5e-2,
      3e-2,
      2e-2,
      1.5e-2,
      1.25e-2,
      1.1e-2,
      9e-3,
      8e-3,
      7e-3,
      5e-3
      ]

fig, ax = pl.subplots()

ax.plot(tinv, mu, marker='.', linestyle='none', label='GK: Paper')

ax.legend()
ax.grid()

ax.set_yscale('log')

ax.set_ylabel(r'$\eta$ $[Pa \cdot s]$')
ax.set_xlabel(r'$1000/T$ $[K^{-1}]$')

pl.show()

