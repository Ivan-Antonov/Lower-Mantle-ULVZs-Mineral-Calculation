# Lower-Mantle-ULVZs-Mineral-Calculation
Code that can be used to calculate physical properties (density, Vs &amp; Vp) of different minerals at Lower Mantle Conditions (Uses Lars Stixrude and Carolina Lithgow-Bertelloni data)


Call the class properties from module ultimate. (Lars Stixrude and Carolina Lithgow-Bertelloni data required)

There are 4 objects:

-graph

-matrix

-calculate

-colourmap

 

For the graph object you need to define:

p-pressure

s-the text file form which the physical properties are taken from e.g. pyrolite.56

g- which graphs to draw, d, vp, ,vs and all

 

For the matrix object you need to define:
p- pressure

s- the text file form which the physical properties are taken from

v- matrix or read file or both

o- the order of the matrix, 2,5,7

 

For the calculate object you need to define:

P- pressure

s- the text file form which the physical properties are taken from

phys- the property (D, Vp, Vs)

spin- the spin (AFM, FM, NS)

M- melt percentage

Fe- iron percentage

Sys- the system (Iso, Adi)

T- The temperature

 

For the colourmap object you need to define:

P- pressure

s- the text file form which the physical properties are taken from

phys- the property (D, Vp, Vs)

spin- the spin (AFM, FM, NS)

Sys- the system (Iso, Adi)

T- The temperature 
