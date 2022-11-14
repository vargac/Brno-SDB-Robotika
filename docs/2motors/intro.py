#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

lavy_motor = Motor( Port.B )
pravy_motor = Motor( Port.C )

lavy_motor.run( 360 )
pravy_motor.run( 360 )

wait( 2000 )

lavy_motor.stop()
pravy_motor.stop()


# Všechny řádky, které začínají mřížkou '#', jsou tzv. "komentáře".
# To znamená, že jsou to poznámky programátora, např. aby něco nezapomněl.
# Robot tyto řádky ignoruje, jako by tam nebyly. My toho využijeme, abychom si
# vysvětlili novou látku.
# 
# Tento kód je podobný tomu z minulé hodiny. Prvních 5 řádků je magických,
# zatím to berme tak, že je prostě třeba je napsat.
# 
# Následuje `left_motor = Motor( Port.B )`. Tím řekneme robotovi, že má
# na portu "B" připojený motor. To je pravá strana `Motor( Port.B )`, vytvoří
# se tak v paměti robota něco jako motor. Není to takový motor, jaký ho vidíme
# v realitě, není to fyzický, hmotný motor. Podobně jako nám se do paměti
# nedostane moucha, když se učíme na písemku z biologie. Máme v hlavě něco,
# co připomíná mouchu, pamatujeme si jak vypadá, jak se chová. Stejně tak robot
# nemá v paměti motor ale ví jak vypadá a jak ho má ovládat, i to, že je
# připojen na portu "B". Nyní ještě potřebujeme tento motor pojmenovat.
# To se udělá tak, že na levou stranu od rovnítka "=" napíšeme název. Jakoby
# si robot nalepil na motor poznámku "lavy_motor". On tomu nerozumí, stejně
# tak bychom ho mohli nazvat „vsvrbsbd“. Ale pro nás programátory je to snazší,
# když nazýváme proměnné správně. "Proměnné" - to je nové slovo, myslíme jím
# hodnotu (např. motor v paměti nebo číslo) svázanou s názvem.
# 
# Stejně vytvoříme "pravy_motor". Ten je připojen na portu "C".
# 
# `lavy_motor.run( 360 )` -- "lavy_motor" robot už má v paměti, najde si ho
# a roztočí. Tečku "." píšeme za názvem proměnné, pak následuje "metoda,
# kterou zavoláme". Co je to "zavolat metodu"? "metoda" je nějaký jiný program,
# podprogram. Napsal ho někdo jiný, stejně jako my teď píšeme hlavní
# program. Když se metoda "zavolá", znamená to, že se tento podprogram spustí.
# Nyní se spustí podprogram `run( 360 )` -- Motor se roztočí rychlostí 360
# stupňů za sekundu. Víme, že kruh má 360 stupňů. Takže za jednu vteřinu
# se kolo připojené na motor otočí o celou jednu otočku. Stejně spustíme i
# druhý motor "pravy_motor", nyní se oba točí, dokud je nevypneme.
# 
# `wait( 2000 )` jednoduše způsobí, že robot bude 2000ms (= 2s) čekat. Ale
# pozor, motory jsou již spuštěny, to znamená, že se po celé tyto dvě sekundy
# točí. "wait" je také podprogram. Tentokrát ale nepíšeme žádkou tečku a
# něco před ní. "lavy_motor.run" byla metoda, je tam i tečka. Bez tečky
# se to nazývá "funkce". "run" samo o sobě neví, který motor má spustit.
# Proto je tam i ta tečka "lavy_motor.run". Ale "wait" je jen jedno, pro
# jednoho robota, nedá se, aby např. jen motor čekal. Celý robot čeká.
# 
# Na konci oba motory vypneme, pomocí metody "stop".
