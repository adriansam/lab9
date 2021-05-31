import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data

# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# t = np.linspace(0, 2*np.pi, 100)
# z = t
# x = np.sin(t) * np.cos(t)
# y = np.tan(t)
# ax.plot(x, y, z, label='przyklad 1')
# ax.legend()
# plt.show()

# np.random.seed(19680801)
#
# def randrange(n, vmin, vmax):
#     return  (vmax - vmin) * np.random.rand(n) + vmin
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# n = 100
#
# # x[23, 32], y=[0,100] z=[zlow, zhigh]
# for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)
#
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# plt.show()

# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()

# fig = plt.figure(figsize=(8,3))
# ax1 = fig.add_subplot(121, projection='3d')
# ax2 = fig.add_subplot(122, projection='3d')
#
# _x = np.arange(4)
# _y = np.arange(5)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y = _xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = depth =1
# ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
# ax1.set_title("Wykres zacieniony")
# ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
# ax2.set_title("Wykres nie zacieniony")
# plt.show()

# fig = plt.figure(figsize=plt.figaspect(0.5))
#
# ax = fig.add_subplot(121, projection='3d')
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#
# ax.set_zlim(-1.01, 1.01)
#
# ax = fig.add_subplot(122, projection='3d')
# X, Y, Z = get_test_data()
# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
# plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.linspace(0, 1, 100
y = np.sin(x**2*np.pi)/2+0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x,y)')
colors = ['r', 'g', 'b', 'k']
np.random.seed(19680801)
x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list = []
for c in colors:
    c_list.extend([c] * 20)

ax.scatter(x, y, zs=0, zdir='y', label='points in (x,z)')

ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(elev=20, azim=-35)
plt.show()

#prc.domowa
#zad1

