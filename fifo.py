"""
This script was created to perform memory paging table calculations for a 
page reference using the First-In First-Out (FIFO) page replacement algorithm
"""


def fifo(sequence: list, frames=3, show_pages=False):
    hits, misses = 0, 0
    occurences = {}

    numbers = []
    for i in range(len(sequence)):
        for num in numbers:
            if num in occurences.keys():
                occurences[num] += 1
            else:
                occurences[num] = 1

        if sequence[i] in numbers:
            hits += 1
            continue
        else:
            misses += 1
            if len(numbers) < frames:
                numbers.append(sequence[i])
            else:
                longest_in = max(occurences, key=occurences.get)
                occurences[longest_in] = 0
                idx = numbers.index(longest_in)
                numbers[idx] = sequence[i]

        if show_pages:
            print(f"Page {i+1} {numbers}")

    print(f"\nHits {hits}, Misses {misses}")
    print(f"Average misses {round((misses/len(sequence))*100,2)}%")


seq = [1, 3, 0, 3, 5, 6]
seq1 = [5, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 5, 0, 1]
seq2 = ['a', 'b', 'c', 'd', 'c', 'a', 'd', 'b', 'e', 'b', 'a', 'b', 'c', 'd']

fifo(seq, show_pages=True)
fifo(seq1, show_pages=True)
fifo(seq2, 4, True)
