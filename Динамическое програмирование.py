
word_a = 'hish'
word_b = 'fish'

a = len(word_a)
b = len(word_b)
cell = [[0] * b for _ in range(a)]
for i in range(a):           #строка
    for j in range(b):       #столбец
        if word_a[i] == word_b[j]:
            cell[i][j] = cell[i-1][j-1] + 1  #буквы совпадают
        else:
            cell[i][j] = max(cell[i-1][j], cell[i][j-1]) #буквы не совпадают
print('Количество совпадений ', cell[i][j])
print('В каких буквах было совпадение ', *cell[j])