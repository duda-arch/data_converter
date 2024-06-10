import struct
import binascii

class Conversions:
    
    @staticmethod
    def HEX_TWO_ASCII(valor):
        try:
            return str(bytes.fromhex(valor).decode('latin-1')).replace('\u0000', '')
        except Exception as err:
            return str(err)
        
    @staticmethod
    def FLOAT_BIG_ENDIAN_ABCD(valor):
        try:
            if len(valor) > 4:
                return struct.unpack('!f', bytes.fromhex(valor))[0]
            else:
                return struct.unpack('!f', bytes.fromhex(valor + "0000"))[0]
        except Exception as err:
            return str(err)
            
    @staticmethod
    def FLOAT_LITTLE_ENDIAN_DCBA(valor):
        try:
            if len(valor) > 4:
                return struct.unpack('<f', bytes.fromhex(valor))[0]
            else:
                return struct.unpack('<f', bytes.fromhex(valor + "0000"))[0]
        except Exception as err:
            return str(err)
            
    @staticmethod
    def INT16_BIG_ENDIAN_AB(valor):
        try:
            register = valor.replace(' ','') if len(valor) >= 2 and type(valor) == str else valor
            bits = 16
            val = int(register, bits)
            if val & (1 << (bits-1)):
                val -= 1 << bits
            return val
        except Exception as err:
            return str(err)
            
    @staticmethod
    def INT32_BIG_ENDIAN_ABCD(valor):
        try:
            return int("".join(str(valor).split(' ')), 16)
        except Exception as err:
            return str(err)
            
    @staticmethod
    def STRING_TWO_HEX(valor):
        try:
           return binascii.hexlify(valor.encode('utf-8')).decode('utf-8')
        except Exception as err:
            return str(err)
            
    @staticmethod
    def HEX_TWO_STRING(valor):
        try:
           return bytes.fromhex(valor).decode('utf-8')
        except Exception as err:
            return str(err)