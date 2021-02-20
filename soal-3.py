ujianteori = 50.0
ujianpraktek = 50.0

if ujianteori >= 70 and ujianpraktek >= 70 :
    print("Selamat, anda lulus!")
elif ujianteori >= 70 and ujianpraktek <=70:
    print("Anda harus mengulang ujian praktek.")
elif ujianteori <= 70 and ujianpraktek >=70:
    print("Anda harus mengulang ujian teori.")
else :
    print("Anda harus mengulang ujian teori dan praktek.")