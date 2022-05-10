# dutch national flag

flag = [0, 1, 2, 0, 2, 1, 1]


def first_swap(pivot_index: int, a: list[int]) -> None:
    smaller = []
    equal = []
    greater = []

    for x in a:
        pivot = a[pivot_index]
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    print()


first_swap(4, flag)




