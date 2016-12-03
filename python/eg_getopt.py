import sys
import getopt

def usage() :
   print("How to use")




if __name__ == "__main__" :
   try:
      argv = sys.argv[1:]
      opts,args = getopt.getopt(argv,"i:o:h",["ifile=x","ofile=y"])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)

   print(opts)

