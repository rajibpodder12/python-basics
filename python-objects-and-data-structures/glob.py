import glob

for filename in glob.glob('/Users/rpodder/Documents/pylearn/python-objects-and-data-structures/*.py',recursive=True):
    print(filename)