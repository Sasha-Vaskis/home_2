screw_diameter = int(input('Какой диаметр самореза?'))
screw_length = int(input('Какая длина самореза?'))
numbe_of_screws = int(input('Сколько саморезов вам понадобится?'))
my_table = {2: {16: 1, 25: 1.4},
            3: {16: 1.6, 25: 2, 32: 3.2},
            4: {16: 1.8, 25: 2.3, 32: 3.5, 35: 3.8},
            5: {16: 2, 25: 2.5, 32: 3.8, 35: 4, 40: 5}
            }
print('Взвесьте', my_table[screw_diameter][screw_length]*numbe_of_screws, 'грамм саморезов')