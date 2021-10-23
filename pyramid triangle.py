def pyramid_triangle(n):
    k=n-1
    for z in range(0,n):
        for i in range(0,k):
            print(end=" ")
        k=k-1
    
        for j in range(0,z+1):
            print("*",end=" ")
        print("\r")
    g=n+1
    for u in range(0,n):
        for i in range(0,g):
            print(end=" ")
        g=g+1
n=int(input("Enter a value:"))
pyramid_triangle(n)
        

    
