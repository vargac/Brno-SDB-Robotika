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
# 
# 
# 1. Nyní se naučíme jak program nahrát do robota. Otevřete si stránku
# https://xlcteam.github.io/RLLR/04/ a přibližně v polovině stránky najdeme
# postup na více kroků. Začneme od kroku 7: "Teraz zapneme EV3-kocku..."
# a skončíme krokem 12.
# 
# 2. Motory jsme spustili rychlostí jedna otočka za sekundu, a šli 2 sekundy.
# Takže by se měly otočit o dvě celé otáčky. Spusťte robota a zkontrolujte,
# zda se kolo opravdu otočilo 2 krát.
# 
# 3. Co kdybychom spustili motory 2krát rychleji? Nebo ještě víc? Jak
# nejrychleji je umíte spustit?
# 
# 4. Nyní bychom chtěli našeho robota pustit do druhé strany, aby šel dozadu.
# Jak byste to udělali?
# 
# 5. Vyzkoušejte spustit jen jeden motor, druhým se vůbec nepohne. Jaký pohyb robot
# udělá?
# 
# 6. Napište program, kde se robot bude točit na místě.
# 
# 7. A jak byste poslali robota do kruhu? Přemýšlejte nad tím, vyzkoušejte
# si s programem pohrát, co Vás napadne.
# 
# 8. Rozšiřte program dále, aby robot nejprve šel jednu sekundu dopředu, poté
# jednu sekundu dozadu.
# 
# 9. Nyní chceme, aby mezitím ještě 1 vteřinu stál na místě.
# 
# 10. Naprogramujte robota tak, aby šel do čtverce.
# 
# BONUS: Vyberte si jednu písničku a zkuste vymyslet jednoduchou choreografii
# pro vašeho robota. Znáte už všechny možné pohyby, které robot zvládne.
