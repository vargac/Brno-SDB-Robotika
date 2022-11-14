#!/usr/bin/env pybricks-micropython

# Problém předchozí úlohy je v tom, že robot se né vždy otočí o stejný úsek.
# Například pokud budou méně nabité baterie nebo bude jiný povrch na zemi. Zde
# si ukážeme funkci 'run_angle', která funguje trochu jinak než 'run'.  Začneme
# tím, co už známe:

from pybricks.ev3devices import Motor
from pybricks.parameters import Port


lavy_motor = Motor( Port.B )
pravy_motor = Motor( Port.C )

# Nyní použijeme 'run_angle', která kromě rychlosti potřebuje vědět ještě úhel,
# o který se má motor otočit. Pozor! Motor, né kolo. Pokud jsou mezi motorem
# a kolem převody, tak se kolo nemusí otočit o stejně jako motor.

pravy_motor.run_angle( 360, 720 )
lavy_motor.run_angle( 360, 720 )

# Nejprve se pravý motor otočil rychlostí 360 o 720 stupňů. To jsou dvě celé
# rotace motoru, neboť kruh má 360 stupňů a 360 * 2 = 720. Zkuste to odpozorovat,
# když robota spustíte, jestli se opravdu otočí dvakrát.

# Vraťte se k předchozí úloze, ale použijte 'run_angle' místo 'run'.
