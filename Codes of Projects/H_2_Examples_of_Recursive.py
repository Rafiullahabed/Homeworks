
# def fibonacci(n,a=0,b=1):
#     print(a, end=" ")
#     a , b = b, a + b
#     if n > 1:
#         fibonacci(n-1, a, b)
# fibonacci(20)

# def tower_of_hanoi(n, source, target, auxiliary):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return
#     tower_of_hanoi(n-1, source, auxiliary, target)
#     print(f"Move disk {n} from {source} to {target}")
#     tower_of_hanoi(n-1, auxiliary, target, source)

# n = 3
# tower_of_hanoi(n,"A","C","B")