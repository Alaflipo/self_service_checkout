import os

# to lps 
os.system('mcrl22lps ssc.mcrl2 out/ssc.lps')
# to lts 
os.system('lps2lts out/ssc.lps out/ssc.lts')
