def bubble_sort(lst):
    """
    버블 정렬 (Bubble Sort)

    Parameters:
        lst (list): 정렬할 리스트

    Returns:
        None: 리스트를 직접 수정하는 in-place 정렬입니다.
    """
    bubble_count = len(lst)
    bubble_limit = bubble_count - 1
    for i in range(bubble_count):  # i = target_bubble
        for j in range(bubble_limit - i):  # j = bubble_index
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    # return lst : in-place sorting, explicit return not needed