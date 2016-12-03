from shutil import copytree, copy2
import re
from os.path import basename, isdir, dirname
import os

def copyDir(source_dir, dest_dir) :
    source_dir = re.sub(r'/$','',source_dir)
    if(not isdir(source_dir)) :
        raise Exception("Source dir '{0}' not a directory".format(source_dir))
    if (not isdir(dest_dir)):
        raise Exception("Destination dir '{0}' not a directory".format(dest_dir))
    bn = basename(source_dir);
    target= os.path.join(dest_dir, bn)
    copytree(source_dir, target)

copyTree2("c:/tmp/deletem/", "c:/tmp/xx/")




