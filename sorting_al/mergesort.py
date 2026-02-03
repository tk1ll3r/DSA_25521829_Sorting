# Sắp xếp trộn
import numpy as np
import time
import sys
import os

def merge_sort(arr,l,r): # Hàm chia nhỏ arr và thực thi đệ quy trộn và sắp xếp
    if l >= r:
        return
    mid = (l+r)//2
    merge_sort(arr,l,mid)
    merge_sort(arr,mid + 1,r)

    merge(arr,l,mid,r)
def merge(arr, l, mid, r): # Hàm trộn và sắp xếp 
    left = arr[l:mid+1].copy()
    right =  arr[mid+1:r+1].copy()
    i = j = 0 # Hạng tử đếm số lượng phần tử đã được ấy vào
    k = l # Để lấy index và sửa trực tiếp vào arr
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # So sánh để lấy phần tử nhỏ hơn và thực thi
            arr[k] = left[i] # Thực thi ngay trên mảng arr
            i += 1
            k +=1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
            
# Nếu 1 bên đã thêm hết, thì sẽ thực thi phần còn lại của bên còn lại vào mảng arr
    while i < len(left): 
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1

    
# Đọc dataset từ file 'data'   
DATA_DIR = "../dataset/data"
times = [] 

for i in range(1, 11):
    filename = f"d{i}.txt"
    filepath = os.path.join(DATA_DIR, filename)
    
    if os.path.exists(filepath):
        data = np.loadtxt(filepath)
        
        n = len(data)
        start = time.time()
        merge_sort(data, 0, n - 1)
        end = time.time()
        
        duration = end - start
        times.append(duration)
        print(f"Test {filename}: {duration:.5f}s")

if times:
    print("-" * 30)
    print(f"Thời gian trung bình: {sum(times) / len(times):.5f}s")
