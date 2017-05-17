
import re

def substituteInFile(file_path,pattern_replacement_list) :
   f = open(file_path, "r")
   contents = f.read()
   f.close();
   for pattern, replacement in pattern_replacement_list :
      contents = re.sub(pattern, replacement, contents, flags=re.MULTILINE)
   fo = open(file_path,"w")
   fo.writelines(contents)
   fo.close()


def commentOutFileLinesContaining(file_path, list_strings) :
   args = []
   for s in list_strings :
      args.append([r"(.*{}.*)".format(s), '#\\1'])
   substituteInFile(file_path, args)

commentOutFileLinesContaining("a.txt", ["CV-Common","cf-python-logging-support", "sapclea-mlpkit"])
