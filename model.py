#Simulation Loop
steps = 200
for t in range(steps):
    Cn = C.copy()
    
    #Difference term (central difference)
    diffusion = D*(
        (np.roll(Cn, -1, axis=0) - 2*Cn + np.roll(Cn, 1, axis=0)) / dx**2 + 
        (np.roll(Cn, -1, axis=1) -2*Cn + np.roll(Cn, 1, axis=1)) / dy**2 )
    
    #Advection term (upwind scheme)
    adv_x = -u * (Cn - np.roll(Cn, 1 , axis=0)) / dx
    adv_y = -v * (Cn -np.roll(Cn, 1, axis=1)) /dy
    
    #Update concentration
    C+=dt * (diffusion +adv_x + adv_y)