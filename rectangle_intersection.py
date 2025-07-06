def rect_intersection(A, B):
    x1_A, y1_A, x2_A, y2_A = A
    x1_B, y1_B, x2_B, y2_B = B  

    # conditions for non-intersecting
    if x2_A < x1_B or x1_A > x2_B:
        return False     
    if y2_A < y1_B or y1_A > y2_B:
        return False

    #if they are not intersecting return true
    return True

print("Enter the coordinates of rectangle A")
A = list(map(int, input().split()))

print("Enter the coordinates of rectangle B")
B = list(map(int, input().split()))

print("Rectangles intersect:", rect_intersection(A, B))
