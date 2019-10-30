# Zen Solver
solve zen game
# Install
  1. python3
  2. pip3 install -r reqirements.txt
# Run
python3 zen.py \<your board input\> \<your shape input\>

e.g.:
  python3 zen.py board.dat shapes.dat
# Showcase
Example of board.dat:

<img width="176" alt="Screen Shot 2019-09-19 at 10 00 58 PM" src="https://user-images.githubusercontent.com/55373469/65300664-2278e080-db29-11e9-91f3-3032e51b7068.png">



Example of shapes.dat:

<img width="118" alt="Screen Shot 2019-09-19 at 10 01 25 PM" src="https://user-images.githubusercontent.com/55373469/65300707-53591580-db29-11e9-9b4c-ccc173591f88.png">



Example of solver results:

<img width="365" alt="Screen Shot 2019-09-19 at 10 01 40 PM" src="https://user-images.githubusercontent.com/55373469/65300758-7a174c00-db29-11e9-9f72-e38d158a4a04.png">

# Known Issues
1. 45 degree shapes are currently not supported (Should be easy to add this feature)
2. Runtime is not optimized yet!
3. Some abut pieces may have same color due limitation of terminal color choice
