import pwn

# see exactly what bytes are received and sent
pwn.context.log_level = 'debug'
pwn.context.terminal = ['tmux', 'splitw', '-h']

p = pwn.remote('localhost', 1337)
# p = process('./example')

# attach gdb to the process
# specify gdb commands to run
pwn.gdb.attach(p, '''
    b *0x4006b6
    b *main+0x2d
    b *win
    c
''')


# Sending data
p.send(b'hello world\n')
p.sendline(b'A' * 77)
p.sendlineafter(b'> ', b'give shell\n')

offset = 77
win = 0xdeadbeef

pwn.p64(win)
pwn.p64(win, endian='big')
# pack in little endian
pwn.p64(win, endian='little')

payload = [
    b'A' * offset,
    pwn.p32(win),
]
p.sendline(b''.join(payload))


# Receiving data
p.recvline()
p.recvuntil('?')
p.recvall()
p.recvall(timeout=1)
p.recvall(timeout=0.1)


# other useful functions
p.interactive()


# assembly
# https://docs.pwntools.com/en/stable/asm.html
pwn.asm('''
    mov rax, 0x3b
    mov rdi, 0x1337
    syscall
''')

pwn.disasm(b'\x48\xc7\xc0\x3b\x00\x00\x00\x48\xc7\xc7\x37\x13\x00\x00\x0f\x05')
