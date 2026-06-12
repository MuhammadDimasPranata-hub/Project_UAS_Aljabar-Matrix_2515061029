def tampil_matriks(m):
    for baris in m:
        print(baris)


def penjumlahan_matriks(A, B):
    rows = len(A)
    cols = len(A[0])

    hasil = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            hasil[i][j] = A[i][j] + B[i][j]

    return hasil


def pengurangan_matriks(A, B):
    rows = len(A)
    cols = len(A[0])

    hasil = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            hasil[i][j] = A[i][j] - B[i][j]

    return hasil


def perkalian_matriks(A, B):
    rows_A = len(A)
    cols_A = len(A[0])

    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        return "Perkalian tidak dapat dilakukan"

    hasil = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                hasil[i][j] += A[i][k] * B[k][j]

    return hasil


def transpose_matriks(A):
    rows = len(A)
    cols = len(A[0])

    hasil = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            hasil[j][i] = A[i][j]

    return hasil


def determinan_2x2(A):
    if len(A) != 2 or len(A[0]) != 2:
        return "Matriks harus berordo 2x2"

    return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])


def invers_2x2(A):
    det = determinan_2x2(A)

    if det == 0:
        return "Matriks tidak memiliki invers"

    hasil = [
        [A[1][1] / det, -A[0][1] / det],
        [-A[1][0] / det, A[0][0] / det]
    ]

    return hasil