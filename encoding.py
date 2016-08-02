from bitstream import BitStream
from qrcode import QRCode, ENC_NUM, ENC_ALPHANUM, ENC_BYTE, get_data_limit
import sys

NUM_CHARS="0123456789"
ALPHANUM_CHARS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"

def set_enc_type():
    string=QRCode.DATA
    enc=ENC_NUM
    for ch in string:
        if enc==ENC_NUM:
            if ch in NUM_CHARS:
                continue
            elif ch in ALPHANUM_CHARS:
                enc=ENC_ALPHANUM
            else:
                enc=ENC_BYTE
        if enc==ENC_ALPHANUM:
            if ch not in ALPHANUM_CHARS:
                enc=ENC_BYTE
    QRCode.ENCODING=enc

def enc_num(string):
    stream=BitStream()
    return stream

def enc_alphanum(string):
    stream=BitStream()
    return stream

def enc_byte(string):
    stream=BitStream()
    return stream

def get_best_version(data_length, encoding, error):
    for i in range(1, 41):
        if get_data_limit(version=i, error=error, encoding=encoding)>=data_length:
            return i
    print "[FATAL] Too much data to fit a QR code: "+str(data_length)+" chars"
    sys.exit(2)

def encode_data():
    set_enc_type()
    data=QRCode.DATA
    encoded=None
    if QRCode.ENCODING==ENC_NUM:
        encoded=enc_num(data)
    elif QRCode.ENCODING==ENC_ALPHANUM:
        encoded=enc_alphanum(data)
    elif QRCode.ENCODING==ENC_BYTE:
        encoded=enc_byte(data)
    else:
        print "[FATAL] Unrecognized encoding mode "+QRCode.ENCODING
        sys.exit(2)
    QRCode.ENC_DATA=encoded
    QRCode.VERSION=get_best_version(data_length=encoded.length, encoding=QRCode.ENCODING, error=QRCode.ERROR_LEVEL)
