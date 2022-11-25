#!/usr/bin/env pybricks-micropython

# Přečtěte si tento program, spusťte ho a potom nám vysvětlíte jak funguje :)
# Nebojte se experimentovat a upravovat ho, aby jste si vyzkoušeli, že to
# opravdu funguje tak, jak si myslíte.

from pybricks.ev3devices import Motor
from pybricks.parameters import Port


lavy_motor = Motor( Port.B )
pravy_motor = Motor( Port.C )

for i in range( 5 ):
    lavy_motor.run( 360 )
    pravy_motor.run( 360 )
    wait( i * 500 ) # `*` znamená násobenie
    lavy_motor.hold()
    pravy_motor.hold()
    wait( 100 )
