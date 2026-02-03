import numpy as np
import time
import sys
import os
def qs_inplace(arr, l, r):
    if l >= r:
        return # Thoát hàm nếu l >= r
    mid = arr[(l+r)//2]
    i, j = l, r
    while i <= j:
        while arr[i] < mid: # Nếu arr[i] > mid thì sẽ dừng tại đây để xử lý nó 
            i += 1
        while arr[j] > mid: # Nếu mà arr[j] < mid thì sẽ dừng tại đây để xử lý nó
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i] # Hoán đổi hai vị trí đã tìm được ở trên (sau mỗi vòng lặp) cho nhau
            i += 1
            j -= 1 
    if l < j: qs_inplace(arr, l, j) # Đệ quy sử dụng hàm qs_inplace để tính tiếp từ [l,j]
    if i < r: qs_inplace(arr, i, r) # Đệ quy sử dụng hàm qs_inplace để tính tiếp từ [i,r]
    

DATA_DIR = "../dataset/data"
times = [] 

for i in range(1, 11):
    filename = f"d{i}.txt"
    filepath = os.path.join(DATA_DIR, filename)
    
    if os.path.exists(filepath):
        print(f"Đang chạy {filename}...", end="\r")
        data = np.loadtxt(filepath)
        n = len(data)
        start = time.time()
        qs_inplace(data, 0, n - 1)
        end = time.time()
        
        duration = end - start
        times.append(duration)
        print(f"Test {filename}: {duration:.5f}s")

if times:
    print("-" * 30)
    print(f"Thời gian trung bình: {sum(times) / len(times):.5f}s")

