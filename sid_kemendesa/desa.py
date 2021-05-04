import attr
import requests
from typing import Optional

from sid_kemendesa import DeskripsiDesa
from sid_kemendesa import IdmDesa
from sid_kemendesa.constants import BASE_URL


@attr.dataclass(slots=True)
class Desa:
    iddesa: str
    _deskripsi: Optional[DeskripsiDesa] = None
    _idm: Optional[IdmDesa] = None

    @property
    def deskripsi(self) -> DeskripsiDesa:
        if self._deskripsi:
            return self._deskripsi
        self._deskripsi = DeskripsiDesa.from_iddesa(self.iddesa)
        return self._deskripsi

    @property
    def idm(self) -> IdmDesa:
        if self._idm:
            return self._idm
        self._idm = IdmDesa.from_iddesa(self.iddesa)
        return self._idm
