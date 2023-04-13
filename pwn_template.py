#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template
from pwn import *
# Many built-in settings can be controlled on the command-line and show up
# in "args". For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
def start(argv=[], *a, **kw):
'''Start the exploit against the target.'''
if args.GDB: # Set GDBscript below
    return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
elif args.REMOTE: # ('server', 'port')
    return remote(sys.argv[1], sys.argv[2], *a, **kw)
else: # Run locally
    return process([exe] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

# Set up path
exe = './path/to/binary'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
rop = ROP(elf)
# Enable verbose logging so we can see exactly what is being sent (info/debug)
context.log_level = 'debug'

#===========================================================
# EXPLOIT GOES HERE
#===========================================================
io = start()
# shellcode = asm(shellcraft.sh())
# payload = fit({
# 32: 0xdeadbeef,
# 'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
# io.send(payload)
# flag = io.recv(...)
# log.success(flag)
io.interactive()
