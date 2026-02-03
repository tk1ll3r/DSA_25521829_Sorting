import numpy as np

N = 1000000
dataset = []

d1 = np.sort(np.random.uniform(0, 1, N)) # dãy số thực tăng dần
dataset.append(d1)


d2 = np.sort(np.random.uniform(0, 1, N))[::-1] # dãy số thực giảm dần
dataset.append(d2)


for _ in range(3): # 3 dãy số thực, ngẫu nhiên
    dataset.append(np.random.uniform(0, 1, N))


for _ in range(5): # 5 dãy int, ngẫu nhiên
    dataset.append(np.random.randint(0, 10**9, N))
