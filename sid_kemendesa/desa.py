import attr
import requests
from typing import Optional

from sid_kemendesa import DeskripsiDesa
from sid_kemendesa.constants import BASE_URL


@attr.dataclass(slots=True)
class Desa:
    iddesa: str
    _deskripsi: Optional[DeskripsiDesa] = None

    @property
    def deskripsi(self) -> DeskripsiDesa:
        if self._deskripsi:
            return self._deskripsi
        res = requests.get(BASE_URL + f"/home/sdgs/{self.iddesa}")
        assert res.ok
        return DeskripsiDesa.from_page(res.text)
