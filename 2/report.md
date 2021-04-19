Here, we calculate the value of pi using the fact that the probability of a pebble landing in the circle is 
```math
(Area of circle)/(Area of square)
= pi/4
```
So, we run a simulation, where we generate landing coordinates for pebbles and use these to determine whether they are in the circle or not. We count the number of pebbles that land in the circle, and divide by the total number of pebbles, and use this value to calculate pi.

Orange is actual value of pi, while blue is estimate

![pi graph](./images/pi.png)

As you can see, as we take more pebbles, and use their landing to estimate pi, our estimate gets closer to pi.