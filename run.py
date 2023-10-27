import os
from os import listdir
from os.path import isfile, join

# to lps 
os.system('mcrl22lps ssc.mcrl2 out/ssc.lps')
# to lts 
os.system('lps2lts out/ssc.lps out/ssc.lts')

# convert the lts branching bisimular to a version with internal transitions hidden
os.system('ltsconvert -ebranching-bisim out/ssc.lts out/ssc_red.lts')

# prove everything with evidence 
path = "prove/"
file_check = "out/ssc_red.lts"
files = [f for f in listdir(path) if isfile(join(path, f))]
mcf_files = [f for f in files if f.split('.')[1] == "mcf"]

for file in mcf_files: 
    name = file.split('.')[0]
    print(f'Checking {file}:')
    os.system(f'lts2pbes -v -c -f prove/{file} {file_check} prove/{name}.pbes')
    os.system(f'pbessolve -v --file={file_check} --evidence-file=prove/evidence/{name}.lts prove/{name}.pbes')
    # os.system(f'lps2lts prove/evidence/{name}.lps prove/evidence/{name}.lts')
