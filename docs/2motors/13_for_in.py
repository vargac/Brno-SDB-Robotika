#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port


lavy_motor = Motor( Port.B )
pravy_motor = Motor( Port.C )

# Často chceme aby robot něco zopakoval, například "třikrát blikni!". My zatím
# umíme jen hýbat motory, tak se zkusíme posunout třikrát dopředu.

lavy_motor.run( 360 )
pravy_motor.run( 360 )
wait( 500 )
lavy_motor.hold()
pravy_motor.hold()
wait( 100 )

lavy_motor.run( 360 )
pravy_motor.run( 360 )
wait( 500 )
lavy_motor.hold()
pravy_motor.hold()
wait( 100 )

lavy_motor.run( 360 )
pravy_motor.run( 360 )
wait( 500 )
lavy_motor.hold()
pravy_motor.hold()
wait( 100 )

# Nyní to uděláme jinak, místo toho abychom kopírovali stejný kód pod sebe,
# napíšeme ho jenom jednou a řekneme, aby ho provedl třikrát:

for i in range( 3 ):
    lavy_motor.run( 360 )
    pravy_motor.run( 360 )
    wait( 500 )
    lavy_motor.hold()
    pravy_motor.hold()
    wait( 100 )

# Všimněte si, že všechny řádky pod prvním řádkem (se slovem 'for') jsou
# posunuté o 4 mezery vpravo. Řádek takto posunete, když nastavíte kurzor na
# začátek řádku a potom stisknete tabulátor (na klávesnici je hned nad
# caps-lockem). Zkuste změnit program tak, aby šel dopředu až 5 krát.
