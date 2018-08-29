from pyWM import Key
from pyWM import Encrypt
from pyWM import Decrypt
from pyWM import HiddenSignature

Key.generate()  #Generate key
sig = Encrypt.getSignature("LYP")   #Private key signature
HiddenSignature.encodeDataInImage("1.jpg", sig.decode(), "encodeImage.png") #Signature stegans in the picture
get_sig = HiddenSignature.decodeImage("encodeImage.png")    #Extract hidden signatures from images
print(get_sig)
print(Decrypt.verify("LYP",get_sig))    #Use public key to verify signature