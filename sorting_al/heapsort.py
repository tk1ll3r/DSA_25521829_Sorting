# Sắp xếp vun đống (Heap Sort)
import numpy as np
import time
import sys
import os

def heapify(a, n, i):
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and a[left] > a[largest]:
            largest = left
        if right < n and a[right] > a[largest]:
            largest = right
            
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            i = largest  # Tiếp tục kiểm tra nút con vừa đổi chỗ
        else:
            break

def heapsort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

# Đọc dataset từ file 'data'   
DATA_DIR = "../dataset/data"
times = [] 

for i in range(1, 11):
    filename = f"d{i}.txt"
    filepath = os.path.join(DATA_DIR, filename)
    
    if os.path.exists(filepath):
        print(f"Đang chạy {filename}...", end="\r")
        data = np.loadtxt(filepath)
        
        start = time.time()
        heapsort(data)
        end = time.time()
        
        duration = end - start
        times.append(duration)
        print(f"Test {filename}: {duration:.5f}s")

if times:
    print("-" * 30)
    print(f"Thời gian trung bình: {sum(times) / len(times):.5f}s")






