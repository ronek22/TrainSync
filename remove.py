from glob import glob
import os

def delTcx():
    for tcx in glob('*.tcx'):
        os.remove(tcx)
    print "Pliki usuniete"
