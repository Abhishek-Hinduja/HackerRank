def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0

    if y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 <= d2):
        fine = 0
    elif y1 == y2 and m1 == m2:
        fine = 15 * (d1 - d2)
    elif y1 == y2 and m1 > m2:
        fine = 500 * (m1 - m2)
    else:
        fine = 10000

    return max(fine, 0)

print(libraryFine(9,6,2015,6,6,2015))