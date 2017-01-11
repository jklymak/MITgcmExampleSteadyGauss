# Example MITgcm setup for steady stratified flow over Gaussian Bump

  - `./code/` contains modified code
  - `./input/` contains the `data*` files and the python script to generate the data sets

## Setting up

### Compiling

'./build' is where we compile the gcm.  To compile you should run:
```
 /Users/jklymak/MITgcmc66b/MITgcm/tools/genmake2 \
  -optfile=../build_options/darwin_brewgfortranmpi -mods=../code/ \
   -rootdir=/Users/jklymak/MITgcmc66b/MITgcm
```
then `make depend` followed by `make`

### Changing domain size

  1. Change `code/SIZE.h` and recompile.
  2. Change `input/gendata.py` and rerun `python gendata.py`.  It would be good practice to make a new name for the run at this point.
  3. If using open boundaries change `input/data.obcs` i.e. `OB_Jnorth=80*0,` where in this case `ny=80`

### Changing other parameters

  1. Edit  `gendata.py`.  For new runs it is best to change the value of `outdir` right away.

### Running

In `./input`, run `python gendata.py`.  
