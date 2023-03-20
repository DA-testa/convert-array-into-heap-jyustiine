# python3

def sift(a, i, swaps):
    n=len(a)
    min= i
    j=2*i+1

    if j<n and a[j]< a[min]:
        min=j
    b=2 * i + 2
    if b<n and a[b]< a[min]:
        min=b

    if i !=min:
        swaps.append((i,min))

        a[i], a[min]=a[min], a[i]
        sift(a, min, swaps)


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    n = len(data)

    for i in range(n // 2 - 1, -1, -1):

        sift(a, i, swaps)

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print(len(swaps))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
