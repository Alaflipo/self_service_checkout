
# results = {}
# for file in mcf_files: 
#     if (file == "ssc13a.mcf" or file=="ssc14a.mcf" or file=="ssc3a_live.mcf" or file=="ssc3a_safe.mcf"):
#         continue
#     name = file.split('.')[0]
#     print(f'\nChecking {file}:\n')
#     os.system(f'lts2pbes -v -c -f prove/{file} {file_check} prove/pbes/{name}.pbes')
#     result = os.popen(f'pbessolve -v --file={file_check} --evidence-file=prove/evidence/{name}.lts prove/pbes/{name}.pbes').read()
#     print(result)
#     results[name] = result.strip()

# print(results)
