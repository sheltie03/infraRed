# irMagicianで赤外線のキャプチャとリプレイ

##　irMagicianの認識

```
$ ls -la /dev/ttyACM0 
crw-rw---- 1 root dialout 166, 0  4月 15 22:25 /dev/ttyACM0
```

## リモコンのコマンドをJSONファイルとしてダンプ

```
$ sudo python irMagician.py -c -f on.json
$ sudo python irMagician.py -c -f off.json
```

## リモコンのコマンドをリプレイする

```
$ sudo python irMagician.py -p -f on.json
$ sudo python irMagician.py -p -f off.json
```

## コマンドをリプレイし続ける

```
from irMagician import playIR
import time

while True:
    playIR('./on.json')
    time.sleep(1.0)
    playIR('./off.json')
    time.sleep(1.0)
```