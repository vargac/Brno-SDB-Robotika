#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# 6. Rozšiřte program dále, aby robot nejprve šel jednu sekundu dopředu, poté
# jednu sekundu dozadu.
# Nyní chceme, aby mezitím ještě 1 vteřinu stál na místě.

lavy_motor = Motor( Port.B )
pravy_motor = Motor( Port.C )

lavy_motor.run( 360 )
pravy_motor.run( 360 )

wait( 2000 )

lavy_motor.stop()
pravy_motor.stop()
