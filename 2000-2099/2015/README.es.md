# 2015. Elegir Vivienda y Convivencia Dentro del Presupuesto

[Timus 2015](https://acm.timus.ru/problem.aspx?space=1&num=2015) · dificultad 300 · bruteforce

Problema original de Eugene Kurpilyansky, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elige un apartamento para vivir sin compañía o compartir con una persona
de la lista. Sin compañía se admite una o dos habitaciones; compartir
exige dos. En solitario se paga toda la renta; al compartir, cada
persona paga exactamente la mitad y debe respetar su propio presupuesto.
La puntuación suma el beneficio del apartamento y el beneficio de vivir
sin compañía para ese número de habitaciones, o el de la amistad
elegida. Busca cualquier opción asequible de puntuación máxima. Si no
existe ninguna, informa de que no se puede alquilar.

## Entrada

Primero el presupuesto propio y los beneficios de vivir sin compañía con
una y dos habitaciones. Después `n`, `0 ≤ n ≤ 256`, y `n` pares de
presupuesto y beneficio de cada amistad. Luego `m`, `1 ≤ m ≤ 256`, y `m`
ternas: habitaciones (1 o 2), renta completa y beneficio. Presupuestos y
rentas son enteros de 1 a 100 000; beneficios de 0 a 100 000. Los
identificadores empiezan en 1 y siguen el orden de entrada. Tiempo
límite 1 segundo, memoria 64 MB.

## Salida

Para alquilar `i` sin compañía escribe `You should rent the apartment #i
alone.`. Con la amistad `j`, `You should rent the apartment #i with the
friend #j.`. Sin opciones asequibles, `Forget about apartments. Live in
the dormitory.`. Sustituye `i,j` por los identificadores y conserva
palabras, espacios, signos `#` y punto final.

## Evaluación

Un comprobador verifica la frase, los números, las habitaciones y ambos
presupuestos y compara la puntuación con el óptimo; se acepta cualquier
elección óptima, y la negativa solo si nada es asequible.

## Ejemplos

```
10000 50 70
1
10000 100
2
1 10000 200
2 30000 500
```

```
You should rent the apartment #1 alone.
```

```
30000 0 1
1
10000 1001
3
1 20000 2000
2 30000 2000
2 10000 1001
```

```
You should rent the apartment #3 with the friend #1.
```

```
1000 0 0
0
1
1 10000 1000
```

```
Forget about apartments. Live in the dormitory.
```

En el primero solo se puede pagar el apartamento 1, con `50+200=250`; ni
la mitad del segundo cabe. En el segundo la mejor opción individual suma
2001, pero compartir el apartamento 3 con la amistad 1 suma
`1001+1001=2002`. En el tercero la única vivienda es demasiado cara.

## Solución

Recorre los apartamentos en orden. Si la renta completa cabe en el
presupuesto propio, considera
`beneficio_apartamento+beneficio_individual[habitaciones−1]`. Para dos
habitaciones prueba además cada amistad. Compartir es factible
exactamente si `renta≤2·presupuesto_propio` y
`renta≤2·presupuesto_amigo`, con puntuación
`beneficio_apartamento+beneficio_amigo`. Las comparaciones duplicadas
son exactas incluso con renta impar, sin división ni coma flotante.

Guarda la mejor puntuación y los dos identificadores. Inicializa a −1,
menor que cualquier puntuación factible. Actualiza solo ante mejora
estricta: así los empates son deterministas, aunque el juez no lo exige.
Internamente, identificador de amistad cero indica vivir sin compañía.
Si nunca se actualiza, escribe que no se puede alquilar.

Toda opción legal es un apartamento en solitario o uno de dos
habitaciones con exactamente una amistad. Los bucles las consideran
todas y descartan exactamente los pagos que exceden un presupuesto. La
puntuación suma precisamente los dos beneficios relevantes. Por
inducción, la opción guardada es máxima entre las factibles ya vistas;
al terminar es óptima global o no existe ninguna. La inicialización
negativa distingue un óptimo factible de cero puntos de la
imposibilidad.

Hay como máximo `m(n+1) ≤ 65 792` candidatos: tiempo `O(m(n+1))`,
también para `n=0`. La entrada ocupa espacio `O(n+m)` y seleccionar
requiere `O(1)` adicional. Puntuaciones y presupuestos duplicados no
superan 200 000; bastan enteros ordinarios con signo. Otra opción es
ordenar amistades por presupuesto y consultar el mejor beneficio
asequible, pero aquí ya basta enumerar.

## Notas por lenguaje

Una habitación no se comparte. Comprueba ambos presupuestos: nadie puede
pagar más de la mitad para ayudar a la otra persona. No trunques una
mitad impar ni añadas beneficio individual al compartido. Los beneficios
individuales dependen de las habitaciones. Cero amistades y beneficios
nulos son válidos. Los cinco programas usan comparaciones enteras
exactas y el mismo orden de enumeración; la ausencia de opción se
distingue de vivir sin compañía. Python usa CPython y la búsqueda
acotada no necesita optimización.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2015_bruteforce.cpp](2015_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(m (n + 1)) | AC | 0.015 s | 404 KB |
| [2015_bruteforce.go](2015_bruteforce.go) | Go 1.14 x64 | bruteforce | O(m (n + 1)) | AC | 0.015 s | 1136 KB |
| [2015_bruteforce.java](2015_bruteforce.java) | Java 1.8 | bruteforce | O(m (n + 1)) | AC | 0.125 s | 424 KB |
| [2015_bruteforce.py](2015_bruteforce.py) | Python 3.12 x64 | bruteforce | O(m (n + 1)) | AC | 0.078 s | 584 KB |
| [2015_bruteforce.rs](2015_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(m (n + 1)) | AC | 0.031 s | 240 KB |
