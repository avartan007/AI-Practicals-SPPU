def selection_sort_greedy(numbers):
    n = len(numbers)
    print("\nList before Sorting:", numbers, "\n")
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        if min_index != i:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        print(f"Pass {i+1}: {numbers}")
    return numbers

n = int(input("Length of List: "))
numbers = [int(input("Enter Element: ")) for _ in range(n)]
print("\nSorted List:", selection_sort_greedy(numbers))
