import attr
from bs4 import Tag
from typing import Any, List, Optional

from . import JenisIdm


@attr.dataclass(slots=True)
class IndikatorIdm:
    jenis: JenisIdm
    no: int
    indikator: str
    skor: int
    keterangan: str
    rekomendasi_kegiatan: Optional[str]
    nilai: float
    pelaksana_pusat: Optional[str]
    pelaksana_prov: Optional[str]
    pelaksana_kab: Optional[str]
    pelaksana_desa: Optional[str]
    pelaksana_csr: Optional[str]
    pelaksana_lainnya: Optional[str]

    def __attrs_post_init__(self) -> None:
        self.no = int(self.no)
        self.skor = int(self.skor)
        self.nilai = float(self.nilai)
        if self.rekomendasi_kegiatan == "-":
            self.rekomendasi_kegiatan = None

    @classmethod
    def from_tr(cls, tr: Tag, jenis: JenisIdm):
        data: List[Any] = list()
        data.append(jenis)
        for td in tr.find_all("td"):
            data.append(td.text)
        return cls(*data)
