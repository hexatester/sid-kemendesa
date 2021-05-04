import attr
from bs4 import BeautifulSoup
from typing import List


@attr.dataclass(slots=True)
class DeskripsiDesa:
    desa: str
    kecamatan: str
    kabupaten: str
    provinsi: str
    status_pemerintahan: str
    nama_kepala_desa: str
    jenis_kelamin_kepala_desa: str
    rpjm_yang_berlaku: str
    periode_rpjm_yang_berlaku: str
    keberadaan_kantor_kepala_desa: str
    status_kantor_kepala_desa: str
    kondisi_kantor_kepala_desa: str
    lokasi_kantor_kepala_desa: str
    peta_desa_ditetapkan_bupati_gubernur: str
    topografi_wilayah_desa: str
    keberadaan_permukiman_di_lereng_puncak: str
    wilayah_terletak_di: str
    wilayah_berbatasan_laut: str

    @classmethod
    def from_page(cls, page: str):
        soup = BeautifulSoup(page, "html.parser")
        area = soup.find("div", class_="notika-email-post-area")
        data: List[str] = list()
        for tr in area.find_all("tr"):
            data.append(tr.contents[-1].get_text())
        return cls(*data)
