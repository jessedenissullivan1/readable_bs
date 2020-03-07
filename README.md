# Readable bytestring class for python

main.py defines readable_bs class that takes a byte string and optional word-size (ws) in bytes, row size (rs) in words, and codec (codec) arguments (current supports codecs support by builtin python codecs module).  When the object of this class is printed, it is printed as an addressed row of rs words where each word is ws bytes.  Example:

```
0x6e929f8b8 53c94b d5750a 014edb af8b2c 7344f0 f95d6e c127ad 8432f1  
0x6e929f8d0 65bba2 29ebec fe11e2 1886e7 7c5b99 f6fa1d 735aba c205f1  
0x6e929f8e8 959b31 08e938 7127a9 f32e0e 196e95 618b58 0c4831 75a5ca  
0x6e929f900 af99  
```

The class also takes an optional offset to start the address at.  Otherwise addresses start at 0 and increment by number of bytes in the row.

Run main.py as a script to see example results.