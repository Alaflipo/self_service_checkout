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

mcf_files.sort()
mcf_files = mcf_files[14:] + mcf_files[1:14]

results = {}
for file in mcf_files: 
    if (file == "ssc13a.mcf" or file=="ssc14a.mcf" ):
        continue
    name = file.split('.')[0]
    print(f'\nChecking {file}:\n')
    os.system(f'lts2pbes -v -c -f prove/{file} {file_check} prove/pbes/{name}.pbes')
    result = os.popen(f'pbessolve -v --file={file_check} --evidence-file=prove/evidence/{name}.lts prove/pbes/{name}.pbes').read()
    print(result)
    results[name] = result.strip()

print(results)
