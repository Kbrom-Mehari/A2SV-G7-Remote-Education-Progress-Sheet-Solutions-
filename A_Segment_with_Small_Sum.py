n, s = map(int, input().split())
nums = list(map(int, input().split()))

left = right = longest = running_sum = 0

for i in range(n):
    running_sum += nums[i]
    while running_sum > s:
        running_sum -= nums[left]
        left += 1
    longest = max(longest, i - left + 1)

    
print(longest)
