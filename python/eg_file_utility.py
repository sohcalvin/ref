import os

def removeDuplicateFiles(dirPath) :
    files = os.listdir(dirPath)
    filesWithSize = [ [f, os.path.getsize(os.path.join(dirPath,f))]for f in files]
    filesWithSizeSorted = sorted(filesWithSize, key=lambda k: k[1])
    previousRec =  None
    previousContent=[]
    duplicateFiles = []
    for f,s in filesWithSizeSorted :
        if(previousRec is None) :
            previousRec = [f,s]
            previousContent.append(open(f,"rb").read())
            continue
        if(previousRec[1] == s) :

            currentContent = open(f,"rb").read()
            if(currentContent in previousContent) :
                print("File {0} has same size {1} as previous{2}".format( f,s,previousRec[0]))
            else :
                print("eeeeee")
        else :
            previousRec = [f,s]
            previousContent = []



    def makeReleaseDir(dirname) :
        release_dir = os.path.join( "release_files",  dirname)
        os.makedirs(release_dir)
        return release_dir











    print(filesWithSizeSorted)

removeDuplicateFiles("C:/tmp/datax-cv/resumes_and_jobs/business_developer_jobs/")
# os.path.getsize('C:\\Python27\\Lib\\genericpath.py')