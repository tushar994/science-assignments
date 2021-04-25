# Predator pery model

Here we solve the predator prey model and draw graphs using Euler time stepping method. The values we take are

```
gamma = 0.6
c = 0.4
alpha = 0.2
beta = 0.1
K = 50
R0, F0 = 4, 6
```

The plots are

`for duration t=30`
![](./images/30.png)

`for duration t=100`
![](./images/100.png)

`for duration t=1000`
![](./images/1000.png)


## For differnet alphas

For an alpha of valuue 0.8, the prey dies very quickly

![](./images/double_alpha.png)

For an alpha of valuue 0.2, the predators's final population increases

![](./images/half_alpha.png)