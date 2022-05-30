import takeoff_distance

vw = [-10:1:10]

Snrg = takeoff_distance.ground_roll(Tv_vo=5826.88,Tv_vr=4176.67, Vr=36.24, m=1541.61, u_g=0.04, CL_g=0.59, CD_g=0.0414, S=13.46)
print(Snrg)