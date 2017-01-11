# Example MITgcm setup for steady stratified flow over Gaussian Bump

  - `./code/` contains modified code
  - `./input/` contains the `data*` files and the python script to generate the data sets

  - './build' is where we build things.  To build you should run:
```
 /Users/jklymak/MITgcmc66b/MITgcm/tools/genmake2 \
  -optfile=../build_options/darwin_brewgfortranmpi -mods=../code/ \
   -rootdir=/Users/jklymak/MITgcmc66b/MITgcm
```
