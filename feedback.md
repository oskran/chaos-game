# Project 3: Passed
Her hadde det skjedd noe rart med "finished"-taggen deres, da den var helt tom. Jeg hentet prosjektet deres fra Github, men det er fint om dere passer på å sjekke at slikt blir riktig.

## Part A
#### a)
Bra.
#### b)
Bra, men dere ser ut til å mangle plottet som skal sjekke at 1000 genererte punkter er innenfor trekanten.
#### c)
Bra, men det er meningen å iterere 5 ganger _først_ slik at man får `n` punkter totalt for å plotte (så man skal altså egentlig iterere `n + 5` ganger totalt).
#### d)
Bra.
#### e)
Bra.
#### f)
Bra.

## Part B
#### a)
Bra.
#### b)
Bra, men dere mangler plot av alle polygoner med kanter fra 3 og til og med 8.
#### c)
Bra, men dere mangler plot av 1000 genererte startpunkter i en femkant.
#### d)
Bra.
#### e)
Bra.
#### f)
Bra.
#### g)
Bra.
#### h)
Fine tester, men når dere bruker `pytest.raises()` burde dere ha en egen `with`-blokk for hvert kall, så istedenfor:
~~~~python
with pytest.raises(Exception):
    game1 = ChaosGame(2, 1 / 2)
    game2 = ChaosGame(-5, 1 / 2)
~~~~
burde dere ha:
~~~~python
with pytest.raises(Exception):
    game1 = ChaosGame(2, 1 / 2)
with pytest.raises(Exception):
    game2 = ChaosGame(-5, 1 / 2)
~~~~
Dette er fordi i det første tilfellet vil testen passere så lenge _enten_ game1 eller game2 gir en feilmelding, men dere vil teste at _begge_ gir en feilmelding.

Fine plots!

## Part C
#### a)
Bra.
#### b)
Bra.
#### c)
Bra.
#### d)
Bra.
#### e)
Bra.

## Part D
#### a)
Bra.
#### b)
Bra.
#### c)
Fern-variasjonene deres ser litt rare ut. Dette er fordi dere skalerer ulikt langs x og y-aksene, slik at den originale bregnen blir "strukket". Dere burde heller finne ut den største verdien av enten x-verdiene eller y-verdiene og skalere både x og y med samme verdi.
#### d)
Bra.

## Miscellaneous
Generelt bra, noen småting her og der men ikke noe stort.

Hvis dere har spørsmål om oppgaven eller tilbakemeldingen kan dere gjerne sende meg en e-post: j.o.f.akerholm@fys.uio.no
