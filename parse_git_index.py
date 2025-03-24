import sys
import os
import struct

def sha1_to_hex(sha1):
    return ''.join("{:02x}".format(byte) for byte in sha1)

def calc_padding(n):
    floor = (n - 2) // 8
    target = (floor + 1) * 8 + 2
    return target - n

def parse_git_index(index_file):
    try:
        with open(index_file, "rb") as f:
            index_data = f.read()
    except FileNotFoundError:
        print(f"unable to open file '{index_file}'", file=sys.stderr)
        sys.exit(1)

    try:
        header_format = "!4sII"
        header_size = struct.calcsize(header_format)
        dirc, version, entries = struct.unpack(header_format, index_data[:header_size])

        if dirc != b"DIRC":
            raise ValueError("Invalid index file signature")

        print("==== header ===")
        print(f"signature = {dirc.decode()}")
        print(f"version = {version}")
        print(f"entries = {entries}")

        offset = header_size
        for _ in range(entries):
            entry_format = "!LLLLLLLLLL20sh" 
            entry_size = struct.calcsize(entry_format)
            try:
                ce_ctime_sec, ce_ctime_nsec, ce_mtime_sec, ce_mtime_nsec, \
                ce_dev, ce_ino, ce_mode, ce_uid, ce_gid, ce_size, \
                sha1, namelen = struct.unpack(entry_format, index_data[offset:offset + entry_size])
            except struct.error:
                print("Error unpacking entry data.  Index file may be corrupt.", file=sys.stderr)
                sys.exit(1)

            name = index_data[offset + entry_size : offset + entry_size + namelen].decode().rstrip('\x00') 
            padding = calc_padding(namelen)

            print(f"{ce_mode:o} {sha1_to_hex(sha1)} 0\t{name}")

            offset += entry_size + namelen + padding
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python prog .git/index", file=sys.stderr)
        sys.exit(1)

    index_file = sys.argv[1]
    parse_git_index(index_file)
