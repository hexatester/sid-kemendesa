import attr
import requests
from bs4 import BeautifulSoup, Tag
from typing import Any, List

from sid_kemendesa.constants import BASE_URL
from . import JenisIdm
from . import StatusIdm
from . import IndikatorIdm


@attr.dataclass(slots=True)
class IdmDesa:
    desa: str
    kecamatan: str
    kabupaten: str
    provinsi: str
    skor_idm: float
    status_idm: StatusIdm
    target_status: StatusIdm
    skor_idm_minimal: float
    penambahan_yang_dibutuhkan: float
    indikator: List[IndikatorIdm]
    iks_2020: float
    ike_2020: float
    ikl_2020: float
    idm_2020: float
    status_idm_2020: str

    def __attrs_post_init__(self) -> None:
        self.skor_idm = float(self.skor_idm)
        if isinstance(self.status_idm, str):
            self.status_idm = StatusIdm(self.status_idm)
        if isinstance(self.target_status, str):
            self.target_status = StatusIdm(self.target_status)
        self.skor_idm_minimal = float(self.skor_idm_minimal)
        self.penambahan_yang_dibutuhkan = float(self.penambahan_yang_dibutuhkan)
        self.iks_2020 = float(self.iks_2020)
        self.ike_2020 = float(self.ike_2020)
        self.ikl_2020 = float(self.ikl_2020)
        self.idm_2020 = float(self.idm_2020)

    @classmethod
    def from_page(cls, page: str) -> "IdmDesa":
        soup = BeautifulSoup(page, "html.parser")
        content: Tag = soup.find("div", class_="widget-tabs-int")
        trs: List[Tag] = content.find_all("tr")
        data: List[Any] = list()
        for metadata in trs[0:9]:
            data.append(metadata.contents[5].text)
        indikator: List[IndikatorIdm] = list()
        for iks_tr in trs[11:46]:
            indikator.append(IndikatorIdm.from_tr(iks_tr, JenisIdm.IKS))
        for ike_tr in trs[47:59]:
            indikator.append(IndikatorIdm.from_tr(iks_tr, JenisIdm.IKE))
        for ikl_tr in trs[60:63]:
            indikator.append(IndikatorIdm.from_tr(iks_tr, JenisIdm.IKL))
        data.append(indikator)
        data.append(trs[46].contents[5].text)
        data.append(trs[59].contents[5].text)
        data.append(trs[63].contents[5].text)
        data.append(trs[64].contents[5].text)
        data.append(trs[65].contents[5].text.strip())
        return cls(*data)

    @classmethod
    def from_iddesa(cls, iddesa: str) -> "IdmDesa":
        res = requests.get(BASE_URL + f"/home/idm/{iddesa}")
        assert res.ok
        return cls.from_page(res.text)
