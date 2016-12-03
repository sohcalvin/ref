# Method 1
fh = open("eg_read_decode_sample.txt", "rb")
content = fh.readlines()
print("Method 1 output :", content)

# Method 2
fh = open("eg_read_decode_sample.txt", "rb")
bytes = fh.read()
# content = bytes.decode(encoding="utf-8", errors="surrogateescape")
# content = bytes.decode(encoding="utf-8", errors="ignore")
content = bytes.decode(encoding="utf-8", errors="ignore")

print("Method 2 output :", content)
