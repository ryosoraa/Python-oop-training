class Kelas:
    # PRIVATE CLASS VARIABLE
    __member = 0

    def __init__(self, name, kelas, absen):
        self.__name = name
        self.__kelas = kelas
        self.__absen = absen
        Kelas.__member += 1

    # HANYA BERLAKU UNTUK OBJECT
    def get_member(self):
        return Kelas.__member

    # HANYA BERLAKU UNTUK CLASS
    def get_member():
        return Kelas.__member

    #  BISA DI PANGGIL DENGAN CLASS MAUPUN OBEJECT NYA
    @staticmethod
    def get_member1():
        return Kelas.__member
    # HAMPIR SAMA DENGAN STATIC METHOD TAPI LEBIH BETTER JIKA NAMA CLASS NYA AKAN DI RUBAH

    @classmethod
    def get_member2(cls):
        return cls.__member


elda = Kelas('Elda', 12, 17)
desy = Kelas('Desy', 12, 12)
ryo = Kelas('Ryo', 12, 31)

print(Kelas.get_member1())
print(Kelas.get_member2())
print(elda.get_member2())
print(elda.get_member1())
