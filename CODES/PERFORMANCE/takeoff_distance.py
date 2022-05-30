""" 
THIS CODE HAS THE OBJECTIVE OF ESTIMATING THE TAKE-OFF DISTANCE OF AN AIRCRAFT.
ACORDING TO ROSKAM, THE TAKE-OFF SEGMENT CAN BE DIVIDED INTO 3 GROUND-ROLL, AIR DISTANCE
AND CLIMB-OUT, SO THIS CODE WILL FOLLOW THE SAME IDEIA USING THE APPROXIMATE ANALYTICAL METHOD
FOR PREDICTING THE TAKE-OFF DISTANCE AND THE TIME TO TAKE-OFF

"""

import math

def ground_roll (Tv_vo,Tv_vr, Vr, m, u_g, CL_g, CD_g, S, Vw=0, phy=0, p=1.225, g=9.81):
    """
    THIS FUNCTION ESTIMATES THE GROUND ROLL DISTANCE THROUGH ANALYTICAL METHOD.
    Tv_vo = ENGINE THRUST AT ZERO SPEED - [N]
    Tv_vr = ENGINE THRUST AT ROTATION SPEED - [N]
    Vr = ROTATION SPEED (APROX. 1.1*V_STALL) - [M/S]
    m = AIRCRAFT MASS - [KG]
    u_g = GROUND FRICTION COEFICIENT - []
    CL_g = LIFT COEFICIENT UNDER GROUND EFFECT - []
    CD_g = DRAG COEFICIENT UNDER GROUND EFFECT - []
    S = WING PLANFORM AREA - [M²]
    Vw = WIND VELOCITY (OPTIONAL, IF NOT SPECIFIED Vw = 0) - POSITIVE FOR TAIL WIND AND NEGATIVE FOR HEAD WIND) - [M/S]
    phy = RUNWAY GRADIENT (OPTIONAL, IF NOT SPECIFIED phy = 0 RADIANS)
    p = AIR DENSITY (OPTIONAL, IF NOT SPECIFIED p = 1.225 KG/M³) - [KG/M³]
    g = GRAVITY ACCELERATION (OPTIONAL, IF NOT SPECIFIED g = 9.81 M/S²) - [M/S²]

    """
    W = m*g
    A_grvr = g*((Tv_vr/W - u_g) - (CD_g - u_g*CL_g)*p*Vr**2/(2*W/S) - phy)
    A_grvo = g*((Tv_vo/W - u_g) - phy)
    kw = (1 - A_grvr/A_grvo)*(1-Vw**2/Vr**2)/math.log((A_grvo/A_grvr)*(1-Vw**2/Vr**2) + Vw**2/Vr**2)
    A_gw = A_grvo*kw
    Snrg = 0.5*(Vr + Vw)**2/A_gw
    return Snrg