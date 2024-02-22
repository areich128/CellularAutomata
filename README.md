# CellularAutomata

Experimenting with cellular automata using python with an intention to create a Lenia world and experiment with training steady state "beings" using neural networks

`ConvolutionImpl1.py` is step 1. As GoL is essentially a convolution, I wanted to get a simpler convolution algorithm started before complicating things.

`GameOfLifeImpl.py` is step 2. This was the basic GoL implementation in a binary, 2d world. Doing this was very useful to learn about how to create images etc. using `imshow()` in python.

`UserInputImpl.py` is step 3 -- allowing the user to create the starting conditions for their GoL simulation.

`LeniaImpl1.py` is step 4. This will be the non-discreet GoL, with a range of values each cell can become and a more complicated convolution kernel.

Sources: [Source 1](https://link.springer.com/article/10.1134/S1995423914040016) , [Source 2](https://arxiv.org/pdf/2005.03742.pdf)
