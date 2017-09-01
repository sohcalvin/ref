import tempfile
from memory_profiler import profile
from array import array

class FileCache():
    def __init__(self):
        self.fp_data = tempfile.NamedTemporaryFile(mode="w+", dir="/tmp")
        print(self.fp_data.name)
        # self.line_pos = [0]
        self.line_pos = array('I',[0])
        self.current_pos = 0


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp_data.close()

    def writeLine(self, line):
        c = line # + "\n"
        self.current_pos += len(c)
        self.line_pos.append(self.current_pos)
        self.fp_data.write(c)

    def readLine(self, line_index):
        self.fp_data.seek(self.line_pos[line_index])
        ss = self.fp_data.read(self.line_pos[line_index + 1] - self.line_pos[line_index])
        return ss




def genDummyFile(num,fname) :
    print("genDummyFile - Begin")
    with open(fname, "w") as fo:
        for i in range(num):
            fo.write(str(i) + "\n")
    print("genDummyFile - Done")

# @profile
def writeToCache(fc, fname) :
    with open(fname, "r") as fi:
        for d in fi:
            fc.writeLine(d.strip())



if __name__ == '__main__':

    fc = FileCache()
    fname = "test_file100mil.txt"

    # genDummyFile(100000000, fname)
    import time
    t1 = time.time()
    writeToCache(fc, fname)

    t2 = time.time()
    for i in range(10) :
        print(fc.readLine(100000))
        print(fc.readLine(0))


    t3= time.time()

    print("Writing to cache {} secs".format(t2-t1))

    print("Seek read 1 line {} secs".format(t3-t2))

    # import array
    # eff_array = array.array('I',[])
    # eff_array.append(5)
    # print(eff_array[0])