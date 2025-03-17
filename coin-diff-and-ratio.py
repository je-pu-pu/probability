
"""
差と比をの推移をプロットする
"""

import random
import matplotlib.pyplot as plt

plt.rcParams[ "font.family" ] = "MS Gothic"

N = 5000 # 試行回数

face = 0 # コインの表が出た回数
back = 0 # コインの裏が出た回数

x = range(1, N + 1 )
y = []
z = []

for n in range(0, N):
    if random.randint(0, 1) == 1:
        face += 1
    else:
        back += 1
    
    y.append( abs( face - back ) )
    z.append( face / ( n + 1 ) )

fig, ax = plt.subplots()
# ax.set_ylim( 0, 1 )
ax.plot( x, y, label='表が出た回数と裏が出た回数の差', color='red' )
h1, l1 = ax.get_legend_handles_labels()

ax2 = ax.twinx()
ax2.set_ylim( 0, 1 )
ax2.plot( x, z, label='コインを投げた回数に対する表が出た回数の比', color='blue' )
h2, l2 = ax2.get_legend_handles_labels()

ax.set_title( 'コインを' + str( N ) + '回投げて差と比の推移をプロット' )
ax.legend( h1 + h2, l1 + l2, loc='upper right' )

plt.show()