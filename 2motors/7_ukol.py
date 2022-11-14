#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# 7. Naprogramujte robota tak, aby se otočil doprava. (Tedy udělal 90° otocku)

lavy_motor = Motor( Port.B )
pravy_motor = Motor( Port.C )

lavy_motor.run( 360 )
pravy_motor.run( 360 )

wait( 2000 )

lavy_motor.stop()
pravy_motor.stop()
