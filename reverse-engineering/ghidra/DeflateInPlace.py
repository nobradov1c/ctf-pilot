#HTB inflate indefinite
#@author Matthieu Walter
#@category matth.ctf.htb
#@keybinding
#@menupath Tools.misc.DeflateInPlace
#@toolbar
import zlib
import jarray
import binascii
def decompress(addr):
    initial_addr = addr
    instr = getShort(addr)
    if instr != 0xb0f:
        raise Exception, "lol"
    addr = addr.add(2)
    comp_size = getShort(addr)
    print("comp size = %d"%comp_size)
    addr = addr.add(2)
    dec_size = getShort(addr)
    print("dec size = %d"%dec_size)
    addr = addr.add(4)
    data_buffer = jarray.zeros(comp_size,"b")
    currentProgram.getMemory().getBytes(addr,data_buffer)
    data_buffer = bytes(bytearray(data_buffer))
    uncompressed_data = zlib.decompress(data_buffer)
    addr = initial_addr
    for x in uncompressed_data:
        removeDataAt(addr)
        removeInstructionAt(addr)
        setByte(addr, ord(x))
        addr = addr.add(1)
addr = currentAddress
decompress(addr)
