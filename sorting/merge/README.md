# Blog Notes: Merge Sort

Merge Sort is a sorting algorithm in which the list of items
to be sorted is divided into smaller sub-lists. It does this
recursively, dividing them until the sub-lists have 0 or 1
elements in them. Once that has been accomplished, the sub-
lists are re-merged in order.

## Pseudocode

```pseudocode
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Trace (Step-Through)

Input: [8,4,23,42,16,15]

- Left: [8, 4, 23]
  - Left(Left): [8]; Left(Right): [4, 23]
  - Left(Left): [8]; Left(Right(Left)): [4]; Left(Right(Right)): [23]
  - Left(Left): [8]; Left(Right) [sorted]: [4, 23]
  - Left [sorted]: [4, 8, 23]
- Right: [42, 16, 15]
  - Right(Left): [42]; Right(Right): [16, 15]
  - Right(Left): [42]; Right(Right(Left)): [16]; Right(Right(Right)): [15]
  - Right(Left): [42]; Right(Right) [sorted]: [15, 16]
  - Right [sorted]: [15, 16, 42]
- List [sorted]: [4, 8, 15, 16, 23, 42]

Once a sub-list is sorted (a list with only 1 element is considered to be sorted)
the algorithm merges it with the other half of the sub-list. The first elements
of both halves are compared, and the smallest value is merged into the list.
The index is then incremented and the first value of the sublist A is compared
with the second element of sublist B. This process continues until one of the lists
is exhausted, at which point the remaining values in the other sub-list are brought
into the sorted list. This process is repeated recursively until the entire list
has been sorted.

## Code

```python
def mergesort(lst):
    n = len(lst)

    if n > 1:
        mid = n // 2
        left = lst[:mid]
        right = lst[mid:]

        mergesort(left)
        mergesort(right)

        merge(left, right, lst)

def merge(left, right, lst):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1
```

## Big O

### Time Efficiency

O(n log n), as you are dividing the list into halves, which requires O(log n),
plus you have to then iterate through all the items in the sub-lists, requiring
O(n), plus then merging all the sub-lists together O(n).

### Space Efficiency

Keeping the temporary sublists requires O(n) space, as they will contain as many
elements as the original list.
