#%%

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=[0,1,2,3,4]
y=[0,2,4,6,8]

plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='black')

plt.title('Our First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([0,1,2,3,4]) #define escala do eixo
plt.yticks([0,2,4,6,7,7.5,8])

plt.legend()

plt.show

# %%
x=[0,1,2,3,4]
y=[0,2,4,6,8]

#shorthand notation
#fmt = '[color][marker][line]'
plt.plot(x,y, 'b.--', label='2x')

plt.title('Our Second Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([0,1,2,3,4]) #define escala do eixo
plt.yticks([0,2,4,6,7,7.5,8])

plt.legend()

plt.show

# %%
x=[0,1,2,3,4]
y=[0,2,4,6,8]

#shorthand notation
#fmt = '[color][marker][line]'
plt.plot(x,y, 'b.--', label='2x')

x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:6], x2[:6]**2, 'r', label='x^2')
plt.plot(x2[5:], x2[5:]**2, 'r--')

plt.title('Our Third Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([0,1,2,3,4]) #define escala do eixo
#plt.yticks([0,2,4,6,7,7.5,8])

plt.legend()

plt.show

# %%
x=[0,1,2,3,4]
y=[0,2,4,6,8]

#resize your graph
plt.figure(figsize=(5,3), dpi=200)

#shorthand notation
#fmt = '[color][marker][line]'
plt.plot(x,y, 'b.--', label='2x')

x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:6], x2[:6]**2, 'r', label='x^2')
plt.plot(x2[5:], x2[5:]**2, 'r--')

plt.title('Our Fourth Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([0,1,2,3,4]) #define escala do eixo
#plt.yticks([0,2,4,6,7,7.5,8])

plt.legend()

plt.savefig('mygraph.png', dpi=300)

plt.show
# %%
