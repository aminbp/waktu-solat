# solat

```solat``` is a python API for malaysia prayer times. This API is using JAKIM prayer times as source of references

### Installation
```
pip install solat
```

### Usage
```
import solat

district = 'sgr01'
print(solat.prayer(district))
```
It will return:
```
[('Kota Setar, Kubang Pasu, Pokok Sena', '12-10-2017 13:57:41'), ('Imsak', '5:38'), ('Subuh', '5:48'), ('Syuruk', '7:03'), ('Zohor', '13:07'), ('Asar', '16:24'), ('Maghrib', '19:06'), ('Isyak', '20:16')]
```

The list of district code can be obtained from http://www2.e-solat.gov.my/zon-waktusolat.php
