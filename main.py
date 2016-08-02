from encoding import encode_data
from qrcode import QRCode, ERROR_CORRECTION_LEVELS
import getopt
import sys

DEFAULT_ERROR_CORRECTION_LEVEL='M'

def load_args(argv):
    try:
        opts, args=getopt.getopt(argv, "i:v:e:")
    except getopt.GetoptError:
        print 'main.py -i <inputfile> [-e <errorlevel=L|M|Q|H>]'
        sys.exit(2)
    for opt, arg in opts:
        if opt=='-i':
            with open(arg, 'r') as infile:
                QRCode.DATA=infile.read()
        elif opt=='-e':
            QRCode.ERROR_LEVEL=arg
    if QRCode.DATA is None:
        print "[FATAL] Input data not set"
        sys.exit(2)
    elif QRCode.DATA[-1]=='\n':
        QRCode.DATA=QRCode.DATA.rstrip()
    if QRCode.ERROR_LEVEL is None or QRCode.ERROR_LEVEL not in ERROR_CORRECTION_LEVELS:
        print "[WARNING] Error correction level missing or invalid, setting to "+DEFAULT_ERROR_CORRECTION_LEVEL
        QRCode.ERROR_LEVEL=DEFAULT_ERROR_CORRECTION_LEVEL

if __name__=="__main__":
    load_args(sys.argv[1:])
    encode_data()
