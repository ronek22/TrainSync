from glob import glob
import os

def delTcx():
    for tcx in glob('*.tcx'):
        os.remove(tcx)
    print "Pliki usuniete"

def countTcx():
    count=0
    for tcx in glob('*.tcx'):
        count+=1

    return count
