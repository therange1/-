#matplotlib默认不支持中文
from pylab import mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

import matplotlib.pyplot as plt
plt.figure()
plt.title('一个表格')
plt.xlabel('x轴名称')
plt.ylabel('y轴名称')

import numpy as np
x = np.linspace(0.1, 10, 400)
y = 1 / x

plt.plot(x, y)

plt.show()
