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
    qs_inplace(arr, l, j) # Đệ quy sử dụng hàm qs_inplace để tính tiếp từ [l,j]
    qs_inplace(arr, i, r) # Đệ quy sử dụng hàm qs_inplace để tính tiếp từ [i,r]



