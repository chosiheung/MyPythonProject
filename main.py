import pandas as pd 
print("hello, python + VS Code!")
print("판다스 버전:", pd.__version__)

import numpy as np
import matplotlib.pyplot as plt

print("NumPy 버전:", np.__version__)
print("Matplotlib 테스트!")

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave Test")
plt.xlabel("x-axis")
plt.ylabel("y = sin(x)")
plt.grid()
plt.show()
print("테스트 수정 중이에요!")
