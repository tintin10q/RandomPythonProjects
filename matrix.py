def add_row(row1: list, row2: list, m1=-1, m2=1, l = True):
    new = []
    for r1, r2 in zip(row1, row2):
        n = r2 * m2 - r1 * m1
        new.append(n)
        if l:
            print(f'{r1}*{m1} - {r2}*{m2} = {r1 * m1} - {r2 * m2} = {n}')
    return new


def add_rows(row1: list, row2: list, t=0):
    new1 = []
    new2 = []
    m1 = row2[t]
    m2 = row1[t]
    for r1, r2 in zip(row1, row2):
        new1.append(r2 * m2)
        new2.append(r1 * m1)
    final = add_row(new1, new2, 1, 1, l=False)
    print(f'{row1} * {m1} = {new1}\n {row2} * {m2} = {new2}\n\n{new2} - {new1} = {final}')
    print(final)
    return new1, new2


def r(row1, row2, i=0):
    """Makes matrix row with first row[i] = 0"""
    assert len(row1) >= i and len(row2) >= i, "i is out of range."
    assert len(row1) == len(row2), "Rows are not the same lenght."
    result = add_rows(row1, row2, row2[i], row1[i])
    print(result)
    return result

#
# def triple_r(r1, r2, r3):
#     r2 = add_rows(r1, r2)[1:]
#     print('\n')
#     r3 = add_rows(r1, r3)[1:]
#     print('\n\n')
#     print('Next:\n')
#     l4 = add_rows(r2, r3)[1:]
#     print('\n\nFinal:')
#     result = l4[1] / l4[0]
#     print(f'{l4[1]}/{l4[0]} = {result}')
#     return result
#
#
# r1 = [2, 4, -1, 13]
# r2 = [5, 2, 42, 23]
# r3 = [-3, 8, -2, 5]
#
# triple_r(r1, r2, r3)

def row(m, r):
    return [i * m for i in r]


# add_rows([-9, -9, 15,15], [-7, 9, -3,5],1)
#
add_rows([-144,108,180],[-60,12,20])
# add_rows([2,2,2,2],[3,2,2,2],0)
