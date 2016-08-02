import sys

class BitStream:
    length=0
    container=''

    """Binary string"""
    def __init__(self, value='0'):
        try:
            self.container=str(int(value, 2))
        except ValueError:
            print "[FATAL] "+value+" is not a binary value"
            sys.exit(2)

    def __repr__(self):
        return self.container

    def push_int(self, value):
        binstr="{0:b}".format(value)
        self.length+=len(binstr)
        self.container+=binstr

    def get_bit(self, indx):
        return int(self.container[indx])

    def padleft(self, to):
        while self.length<to:
            self.container='0'+self.container
            self.length+=1

    def padright(self, to):
        while self.length<to:
            self.container=self.container+'0'
            self.length+=1

    def trimzerosleft(self):
        while self.container[0]=='0':
            self.container=self.container[1:]
            self.length-=1

    def trimzerosright(self):
        while self.container[-1]=='0':
            self.container=self.container[:-1]
            self.length-=1

    def xor(self, value):
        if self.length>=value.length:
            str1=self.container
            str2=value.container
        else:
            str1=value.container
            str2=self.container
        diff=len(str1)-len(str2)

        res=BitStream()
        res.push_int(int(str1[:diff]))
        res.push_int(int(str2)^int(str1[diff:]))
