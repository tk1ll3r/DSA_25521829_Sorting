import numpy as np
import os
os.makedirs("data", exist_ok=True)
N = 1000000
dataset = []

d1 = np.sort(np.random.uniform(0, 1, N)) # dãy số thực tăng dần
np.savetxt("data/d1.txt", d1)
dataset.append(d1)

d2 = np.sort(np.random.uniform(0, 1, N))[::-1] # dãy số thực giảm dần
np.savetxt("data/d2.txt", d2)
dataset.append(d2)

for i in range(3, 6):  # 3 dãy số thực, ngẫu nhiên
    data = np.random.uniform(0, 1, N)
    np.savetxt(f"data/d{i}.txt", data)
    dataset.append(data)

for i in range(6, 11): # 5 dãy int, ngẫu nhiên
    data = np.random.randint(0, 10**9, N)
    np.savetxt(f"data/d{i}.txt", data, fmt='%d')
    dataset.append(data)