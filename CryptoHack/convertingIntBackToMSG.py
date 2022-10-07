import codecs
import base64
from Crypto.Util.number import *

bytesStr = codecs.decode('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf' , 'hex_codec')

base = base64.b64encode(bytesStr)

print(base)