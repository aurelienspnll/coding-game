# Blunder

<p align="center">
    <img src="https://i.pinimg.com/originals/84/a8/e1/84a8e1847cef2a104174b1a8bca64dd9.png" alt="Blunder" width="10%" height="10%">
</p>

## The goal

Blunder is a depressed robot who heals his depression by partying and drinking alcohol. To save him from a life of debauchery, his creators have reprogrammed the control system with a more rudimentary intelligence. Unfortunately, he has lost his sense of humor and his former friends have now rejected him.

Blunder is now all alone and is wandering through the streets with the intention of ending it all in a suicide booth.

To intercept him and save him from almost certain death, the authorities have given you a mission: write a program that will make it possible to foresee the path that Blunder follows. To do so, you are given the logic for the new intelligence with which Blunder has been programmed as well as a map of the city.

## Rules

The 9 rules of the new Blunder system:

1. Blunder starts from the place indicated by the @ symbol on the map and heads SOUTH.
2. Blunder finishes his journey and dies when he reaches the suicide booth marked $.
3. Obstacles that Blunder may encounter are represented by # or X.
4. *When Blunder encounters an obstacle*, he changes direction using the following priorities: SOUTH, EAST, NORTH and WEST. So he first tries to go SOUTH, if he cannot, then he will go EAST, if he still cannot, then he will go NORTH, and finally if he still cannot, then he will go WEST.
5. Along the way, Blunder may come across path modifiers that will instantaneously make him change direction. The S modifier will make him turn SOUTH from then on, E, to the EAST, N to the NORTH and W to the WEST.
6. The circuit inverters (I on map) produce a magnetic field which will reverse the direction priorities that Blunder should choose when encountering an obstacle. Priorities will become WEST, NORTH, EAST, SOUTH. If Blunder returns to an inverter I, then priorities are reset to their original state (SOUTH, EAST, NORTH, WEST).
7. Blunder can also find a few beers along his path (B on the map) that will give him strength and put him in “Breaker” mode. Breaker mode allows Blunder to destroy and automatically pass through the obstacles represented by the character X (only the obstacles X). When an obstacle is destroyed, it remains so permanently and Blunder maintains his course of direction. If Blunder is in Breaker mode and passes over a beer again, then he immediately goes out of Breaker mode. The beers remain in place after Blunder has passed.
8. 2 teleporters T may be present in the city. If Blunder passes over a teleporter, then he is automatically teleported to the position of the other teleporter and he retains his direction and Breaker mode properties.
9. Finally, the space characters are blank areas on the map (no special behavior other than those specified above).

Your program must display the sequence of moves taken by Blunder according to the map provided as input.

The map is divided into lines (L) and columns (C). The contours of the map are always unbreakable # obstacles. The map always has a starting point @ and a suicide booth $.

If Blunder cannot reach the suicide booth because he is indefinitely looping, then your program must only display LOOP.

## Example

Let the map below:
```
######
#@E $#
# N  #
#X   #
######
```

In this example, Blunder will follow this sequence of moves:

- SOUTH (initial direction)
- EAST (because of the obstacle X)
- NORTH (change of direction caused by N)
- EAST (change of direction caused by E)
- EAST (current direction, until end point $)

## Usage 

```bash
python3 main.py "../files/blunder/world-1.txt"

# test
python -m unittest discover
```