
def _sort(alist, start, end):
    """
    Быстрая сортировка для массива данных
    alist: Изначльный список
    start: Начальная позиция
    end: Конечная позиция
    return: Отсортированный массив
    """
    i = start
    j = end
    arr = alist[(start + end) //2][1]
    while True:
        while alist[i][1] < arr:
            i += 1
        while alist[j][1] > arr:
            j -= 1
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
            i += 1
            j -= 1
        else:
            break
    if start < j:
        _sort(alist, start, j)
    if i < end:
        _sort(alist, i, end)

with open("devices.txt",encoding="UTF-8") as file:
    with open("coy.txt", 'w', encoding="UTF-8") as filend:
        endd=len(list(file))
        filend.write(_sort(list(file),0,endd-1))
        a=read(filend)
        for k in range(5):
            print(f"{a[0]}-{a[1]}-{a[8]}")