### WaterMark for Python

## pyWM

A lightweight python image watermark library that supports encrypted watermarks.

## Update Announcement

version|content
--------|--------
1.0.0|Package simply, and it must rely on PIL. We will improve following.
1.0.5|Add the rsa signature module.
1.0.8|Add steganography module, but not work well for JPG
1.1.0|Fix the problem about the length of UTF8, and add demo.

## the effect of the package
![pic1](https://github.com/lyp22/pyWM/raw/master/image/1.png)
![pic2](https://github.com/lyp22/pyWM/raw/master/image/2.png)
![pic3](https://github.com/lyp22/pyWM/raw/master/image/3.png)

## Install
1.Download the package, and input
```
python setup.py install
```
2.Move the the folder called pyWM which has the __init__.py to
```
/the path that you install python/Lib/site-packages
```

## How to use it
```
from pyWM import Key
from pyWM import Encrypt
from pyWM import Decrypt
from pyWM import HiddenSignature

Key.generate()  #Generate key
sig = Encrypt.getSignature("LYP")   #Use private key to generate signature
HiddenSignature.encodeDataInImage("1.jpg", sig.decode(), "encodeImage.png") #Signature stegans in the picture
get_sig = HiddenSignature.decodeImage("encodeImage.png")    #Extract hidden signatures from images
print(get_sig)
print(Decrypt.verify("LYP",get_sig))    #Use public key to verify signature
```


## The version 1.2.0 is on the way.
