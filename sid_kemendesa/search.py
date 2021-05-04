import attr
import cattr
from bs4 import BeautifulSoup, Tag
from requests import Session
from typing import Dict, List, Optional

from .constants import BASE_URL

KAB_NONE = "<option value='0'>- Pilih Kabupaten -</option>"
KEC_NONE = "<option value='0'>- Pilih Kecamatan -</option>"
DESA_NONE = "<option value='0'>- Pilih Desa -</option>"


def select_to_choices(select: str) -> Dict[str, str]:
    select = select.strip(KAB_NONE)
    select = select.strip(KEC_NONE)
    select = select.strip(DESA_NONE)
    soup = BeautifulSoup(select, "html.markup")
    options: List[Tag] = soup.find_all("option")
    results: Dict[str, str] = dict()
    if not options:
        return results
    for option in options:
        results[option["value"]] = option.get_text()
    return results


@attr.dataclass
class ListResponse:
    list_kab: Optional[str] = None
    list_kec: Optional[str] = None
    list_desa: Optional[str] = None

    def __attrs_post_init__(self) -> None:
        if self.list_kec == KEC_NONE:
            self.list_kec = None
        if self.list_desa == DESA_NONE:
            self.list_desa = None


@attr.dataclass
class HasilDesa:
    label: str
    iddesa: str
    _provinsi: str = ""
    _kabupaten: str = ""
    _kecamatan: str = ""
    _desa: str = ""

    def __str__(self) -> str:
        return self.label

    def __attrs_post_init__(self) -> None:
        labels = [s.strip() for s in self.label.split("-")]
        (
            self._desa,
            self._kecamatan,
            self._kabupaten,
            self._provinsi,
            _,
        ) = labels

    @property
    def provinsi(self):
        return self._provinsi

    @property
    def kabupaten(self):
        return self._kabupaten

    @property
    def kecamatan(self):
        return self._kecamatan

    @property
    def desa(self):
        return self._desa


def listKab(id_provinsi: str) -> Dict[str, str]:
    session = Session()
    res = session.get(BASE_URL)
    assert res.ok
    res = session.post(
        url=BASE_URL + "/home/listKab",
        data={"id_provinsi": id_provinsi},
    )
    assert res.ok
    list_response = cattr.structure(res.json(), ListResponse)
    assert list_response.list_kab
    return select_to_choices(list_response.list_kab)


def listKec(id_kab: str) -> Dict[str, str]:
    session = Session()
    res = session.get(BASE_URL)
    assert res.ok
    res = session.post(
        url=BASE_URL + "/home/listKec",
        data={"id_kab": id_kab},
    )
    assert res.ok
    list_response = cattr.structure(res.json(), ListResponse)
    assert list_response.list_kec
    return select_to_choices(list_response.list_kec)


def listDesa(id_kec: str) -> Dict[str, str]:
    session = Session()
    res = session.get(BASE_URL)
    assert res.ok
    res = session.post(
        url=BASE_URL + "/home/listDesa",
        data={"id_kec": id_kec},
    )
    assert res.ok
    list_response = cattr.structure(res.json(), ListResponse)
    assert list_response.list_desa
    return select_to_choices(list_response.list_desa)


def search(term: str) -> List[HasilDesa]:
    session = Session()
    res = session.get(BASE_URL)
    assert res.ok
    res = session.get(
        url=BASE_URL + "/home/cari",
        params={"term": term},
    )
    assert res.ok
    results: List[HasilDesa] = list()
    try:
        results = cattr.structure(res.json(), List[HasilDesa])
    except Exception:
        pass
    return results
