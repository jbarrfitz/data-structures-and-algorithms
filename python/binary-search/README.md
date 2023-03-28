# Binary Search

Binary search in a sorted 1D list

## Whiteboard Process

[Whiteboard](code_challenge_03_whiteboard.png)

## Approach & Efficiency

Since items in the list are sorted, begin with calculating
the middle element's index. If the item at the middle index
is equal to the search key, return that index. If the item
at the middle index is less than the search key, recalibrate
the search area so that the minimum index is one greater than
the middle index; if the item at the middle index is greater
than the search key, recalibrate the search area so that the
maximum index is one less than the middle index. Then
recalculate the middle index and repeat the process. Continue
until an index whose element matches the search key (and return
that index), or until the minimum index is greater than the
maximum index, at which point there are no more elements to
search, and return -1.

Time: O(log n), since the search area is halved with each operation
Space: O(1), as the size of the input has no bearing on the amount
of memory required.
