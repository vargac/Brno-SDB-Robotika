#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# 2. Nyní bychom chtěli našeho robota pustit do druhé strany, aby šel dozadu.
# Jak byste to udělali?

lavy_motor = Motor( Port.B )
pravy_motor = Motor( Port.C )

lavy_motor.run( 360 )
pravy_motor.run( 360 )

wait( 2000 )

lavy_motor.stop()
pravy_motor.stop()
