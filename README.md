# Self Service Checkout (SSC)
A mcrl2 model of a self service checkout system for the course system validation (2IMF30)

## Converting files 
How to convert mcrl2 code to a lps (linear process) file: 
`mcrl22lps <file_name>.mcrl2 <file_name>.lps`

How to convert a lps file to a lts (labeled transition system) file: 
`lps2lts <file_name>.lps <file_name>.lts`

How to view a lts file as a graph: 
`ltsgraph <file_name>.lts`

## model checking with mu calculus formulas 
Check if a lps file holds against a mcf (model mu-calculus formula) file and convert it to a pbes (parameterised boolean equation system) file 

`lps2pbes <file_name>.lps -f <file_name>.mcf <file_name>.pbes`

To run the solver and check if the formula is satisfied: 
`pbes2bool <file_name>.pbes`
