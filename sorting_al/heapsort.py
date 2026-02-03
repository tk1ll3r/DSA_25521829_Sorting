# Sắp xếp vun đống (Heap Sort)


def heapify(a, n, i): # Hàm heapify: sửa lại cây tại vị trí i để nó thỏa mãn Max-Heap
    largest = i            # Giả sử phần tử lớn nhất là cha
    left = 2*i + 1         # Con trái
    right = 2*i + 2        # Con phải
    if left < n and a[left] > a[largest]: # So sánh với con trái
        largest = left   
    if right < n and a[right] > a[largest]: # So sánh với con phải
        largest = right
    
    if largest != i: # Nếu cha không phải lớn nhất thì đổi chỗ
        a[i], a[largest] = a[largest], a[i]
        # Sau khi đổi chỗ thì tiếp tục sửa heap ở nhánh dưới
        heapify(a, n, largest)



def heapsort(a): # Hàm heap sort
    n = len(a)
    
    for i in range(n//2 - 1, -1, -1): # Duyệt từ các nút cha cuối cùng lên gốc
        heapify(a, n, i)  
    for i in range(n-1, 0, -1): # Đưa phần tử lớn nhất về cuối
        a[0], a[i] = a[i], a[0]

        # Sửa lại heap với kích thước giảm đi
        heapify(a, i, 0)
