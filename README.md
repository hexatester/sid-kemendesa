# sid-kemendesa

[![sid-kemendesa - PyPi](https://img.shields.io/pypi/v/sid-kemendesa)](https://pypi.org/project/sid-kemendesa/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/sid-kemendesa)](https://pypi.org/project/sid-kemendesa/)
[![LISENSI](https://img.shields.io/github/license/hexatester/sid-kemendesa)](https://github.com/hexatester/sid-kemendesa/blob/main/LISENSI)

Module python untuk mencari dan melihat data desa dari sid kemendesa.

## Install

Pastikan [python 3.7+](https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe) terinstall, kemudian jalankan perintah di bawah dalam Command Prompt atau Powershell (di Windows + X):

```bash
pip install --upgrade sid-kemendesa
```

## Penggunaan

Contoh penggunaan

```python
from sid_kemendesa import search

nama_desa = "desaku"
hasil_pencarian = search(nama_desa)
for desa in hasil_pencarian:
    print(desa)
```

## Legal / Hukum

Kode ini sama sekali tidak berafiliasi dengan, diizinkan, dipelihara, disponsori atau didukung oleh [Kemendesa](https://kemendesa.go.id/) atau afiliasi atau anak organisasinya. Ini adalah perangkat lunak yang independen dan tidak resmi. _Gunakan dengan risiko Anda sendiri._
