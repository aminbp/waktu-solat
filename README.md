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
[('Gombak,H.Selangor,Rawang, H.Langat,Sepang,Petaling,  S.Alam', '12-10-2017 13:58:55'), ('Imsak', '5:33'), ('Subuh', '5:43'), ('Syuruk', '6:57'), ('Zohor', '13:03'), ('Asar', '16:17'), ('Maghrib', '19:03'), ('Isyak', '20:12')]
```

The list of district code can be obtained from http://www2.e-solat.gov.my/zon-waktusolat.php
