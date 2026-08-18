# print('hello vscode')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.01)
y = np.sin(x)
plt.plot(x,y)
plt.title('y =sinx')
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.show()

print('新增了feature分支,同时对应增加这个语句以测试提交')

print('你好')
