from .Mahasiswa import Mahasiswa
from .NilaiMataKuliah import NilaiMataKuliah

class KHS:
    def __init__(
            self,
            mahasiswa: Mahasiswa, # type hint mahasiswa bertype Mahasiswa
            list_nilai: list[NilaiMataKuliah] # type hint list_nilai bertype list of NilaiMataKuliah
        ):
        self.mahasiswa = mahasiswa
        self.list_nilai = list_nilai

    # -> type hint return value type
    def total_bobot_nilai(self) -> int:
        total = 0
        for mk in self.list_nilai:
            total = total + mk.bobot_nilai() # total += mk.bobot_nilai()

        return total

    def total_sks(self) -> int:
        total = 0
        for mk in self.list_nilai:
            total += mk.sks

        return total

    def index_prestasi(self) -> float:
        return self.total_bobot_nilai()/self.total_sks()