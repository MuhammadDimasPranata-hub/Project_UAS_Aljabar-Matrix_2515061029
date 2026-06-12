import dimas029

A = [[1, 2],[3, 4]]

B = [[5, 6],[7, 8]]

print("Matriks A")
dimas029.tampil_matriks(A)

print("\nMatriks B")
dimas029.tampil_matriks(B)

print("\nPenjumlahan Matriks")
hasil = dimas029.penjumlahan_matriks(A, B)
dimas029.tampil_matriks(hasil)

print("\nPengurangan Matriks")
hasil = dimas029.pengurangan_matriks(A, B)
dimas029.tampil_matriks(hasil)

print("\nPerkalian Matriks")
hasil = dimas029.perkalian_matriks(A, B)
dimas029.tampil_matriks(hasil)

print("\nTranspose Matriks A")
hasil = dimas029.transpose_matriks(A)
dimas029.tampil_matriks(hasil)

print("\nDeterminan Matriks A")
print(dimas029.determinan_2x2(A))

print("\nInvers Matriks A")
hasil = dimas029.invers_2x2(A)
dimas029.tampil_matriks(hasil)