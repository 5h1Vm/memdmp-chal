#!/usr/bin/env python3
import ctypes
import time
import os
import sys

PART1 = "CTF{v0latility_n3wbi3"
PART2_DOUBLE_ENCODED = b"WHpSdU5sOWphRFJzZlE9PQ=="
HEAP_MARKER = b"[!] Secret Credential Base:64 You are near Flag"

# Reduce Python's memory footprint
sys.dont_write_bytecode = True

def main():
    print(f"[*] PID: {os.getpid()}")
    print(f"[*] Job: {PART1}")
    print(f"[*] Encoding: Double Base64")
    
    kernel32 = ctypes.windll.kernel32
    kernel32.GetProcessHeap.restype = ctypes.c_void_p
    kernel32.HeapAlloc.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_size_t]
    kernel32.HeapAlloc.restype = ctypes.c_void_p
    
    h_heap = kernel32.GetProcessHeap()
    
    # Allocate MINIMAL heap (just 512 bytes)
    mem_ptr = kernel32.HeapAlloc(h_heap, 0, 512)
    
    if mem_ptr:
        # Everything packed tightly
        offset = 0
        
        # Write marker
        ctypes.memmove(mem_ptr + offset, HEAP_MARKER, len(HEAP_MARKER))
        offset += len(HEAP_MARKER) + 4  # Small gap
        
        # Write encoded data immediately after
        ctypes.memmove(mem_ptr + offset, PART2_DOUBLE_ENCODED, len(PART2_DOUBLE_ENCODED))
        
        print(f"[*] Heap address: {hex(mem_ptr)}")
        print(f"[*] Allocation: 512 bytes only")
        print(f"[*] Running...")
        
        # Keep minimal memory footprint
        while True:
            time.sleep(120)

if __name__ == "__main__":
    main()
