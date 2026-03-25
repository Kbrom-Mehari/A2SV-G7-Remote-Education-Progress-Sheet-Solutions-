n, t = map(int, input().split())
books = list(map(int, input().split()))

total_books = 0
left = 0
running_sum = 0

for right in range(n):
    running_sum += books[right]

    while running_sum > t:
        running_sum -= books[left]
        left += 1
    total_books = max(total_books, right - left + 1)

print(total_books)

