from math import floor

def bin16dec(bin_):
    num = bin_ & 0xFFFF
    if 0x8000 & num:
        num = -(0x010000 - num)
    return num
#' Decoder Version 4 '
# def decode_extended_v4(payload_hex):
def people_counter(payload_hex):
    bytes_ = bytearray.fromhex(payload_hex)
    decoded_payload = {'LTR': '', 'RTL': '', 'LTR_SUM': '', 'RTL_SUM': '', 'SBX_BATT': '', 'SBX_PV': '', 'DIFF': '',
                       'TEMP': ''}

    if len(bytes_) != 17:
        print('ERROR: Wrong payload length')
        return None

    if bytes_[0] == 0xbe and bytes_[1] == 0x01 and bytes_[2] == 0x04:

        decoded_payload['RTL'] = (bytes_[3] << 8 | bytes_[4])
        decoded_payload['LTR'] = (bytes_[5] << 8 | bytes_[6])
        decoded_payload['LTR_SUM'] = (bytes_[7] << 8 | bytes_[8])
        decoded_payload['RTL_SUM'] = (bytes_[9] << 8 | bytes_[10])
        decoded_payload['SBX_BATT'] = (bytes_[11] << 8 | bytes_[12])
        decoded_payload['SBX_PV'] = (bytes_[13] << 8 | bytes_[14])
        decoded_payload['DIFF'] = abs(decoded_payload['LTR_SUM'] - decoded_payload['RTL_SUM'])
        temp = (bytes_[15] << 8) | (bytes_[16])
        decoded_payload['TEMP'] = floor(bin16dec(temp) / 10)

    else:
        print('ERROR: PCR2 application payload should start with be0104..')

    return decoded_payload

# payload = 'be0104000000000000000100000000010c'
# print(decode_extended_v4(payload))