import os

def create_file(filename):
    with open(filename, "w") as file:
        while True:
            word = input().strip()
            if word.upper() == "STOP":
                break
            file.write(word + "\n")

def read_file_to_list(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def is_sorted(words):
    return words == sorted(words)

def linear_search(words, target):
    for index, word in enumerate(words):
        if word == target:
            return index
    return -1

def merge_sort(words):
    if len(words) <= 1:
        return words
    mid = len(words) // 2
    left_half = merge_sort(words[:mid])
    right_half = merge_sort(words[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def save_list_to_file(filename, words):
    with open(filename, "w") as file:
        for word in words:
            file.write(word + "\n")

def binary_search(words, target):
    left, right = 0, len(words) - 1
    while left <= right:
        mid = (left + right) // 2
        if words[mid] == target:
            return mid
        elif words[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

filename = "words.txt"

create_file(filename)
words_list = read_file_to_list(filename)

if is_sorted(words_list):
    print("The list is already sorted.")
else:
    print("The list is NOT sorted.")

word_to_search = input().strip()
position = linear_search(words_list, word_to_search)
if position != -1:
    print(position)
else:
    print("-1")

sorted_list = merge_sort(words_list)
save_list_to_file(filename, sorted_list)

word_to_search = input().strip()
position = binary_search(sorted_list, word_to_search)
if position != -1:
    print(position)
else:
    print("-1")

print("O(n)")
print("O(log n)")
