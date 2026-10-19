# 1868. Concurso de pronósticos

[Timus 1868](https://acm.timus.ru/problem.aspx?space=1&num=1868) · dificultad 158 · implementation

Problema original de Denis Dublennykh, del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En la final mundial los cuatro primeros equipos ganan oro, los cuatro
siguientes plata y los cuatro siguientes bronce. Varios veteranos
hicieron pronósticos del tipo "el equipo X gana una medalla de tipo Y",
y Vadik paga cinco dólares a cada veterano con más aciertos. Dados los
doce medallistas en el orden de sus puestos y todos los pronósticos,
¿cuánto paga Vadik?

## Entrada

Doce nombres de equipos del primer puesto al duodécimo, luego n
(1 ≤ n ≤ 100) y n pronósticos. Un pronóstico empieza con su número de
apuestas kᵢ, seguido de kᵢ líneas "equipo : medalla" con la medalla
"gold", "silver" o "bronze". Ningún pronóstico da dos medallas a un
equipo ni una misma medalla a más de cuatro equipos. Los nombres tienen
de 1 a 30 letras latinas, guiones bajos, puntos y comas.

## Salida

Lo que paga Vadik, en dólares.

## Ejemplos

### Ejemplo 1

Entrada:

```
Zhejiang_U
U_of_Michigan_at_Ann_Arbor
Tsinghua_U
St._Petersburg_SU
Nizhny_Novgorod_SU
Saratov_SU
Friedrich_Alexander_U
Donetsk_National_U
Jagiellonian_U_in_Krakow
Moscow_SU
Ural_SU
U_of_Waterloo
3
6
Moscow_SU : gold
St._Petersburg_SU_of_ITMO : gold
Warsaw_U : gold
Tsinghua_U : gold
Nizhny_Novgorod_SU : silver
Saratov_SU : silver
6
Warsaw_U : gold
Saratov_SU : gold
Tsinghua_U : gold
Donetsk_National_U : silver
St._Petersburg_SU_of_ITMO : silver
Ural_SU : bronze
6
Zhejiang_U : gold
Tsinghua_U : gold
Shanghai_Jiao_Tong_U : gold
Fudan_U : gold
Moscow_SU : silver
Nizhny_Novgorod_SU : silver
```

Salida:

```
15
```

## Solución

Los nombres no tienen espacios, así que la entrada es una secuencia de
palabras: doce nombres y, por cada apuesta, un nombre, dos puntos y una
medalla. Un diccionario de los doce nombres a sus medallas (puestos 1–4
oro, 5–8 plata, 9–12 bronce) dice si una apuesta acierta; un equipo que
no está en él no ganó nada. Se cuentan los aciertos de cada veterano y
se pagan cinco dólares a cada veterano con la cuenta más alta.
`O(n·k)` consultas al diccionario.

En el ejemplo cada veterano tiene tres aciertos, así que ganan los tres
y Vadik paga 15 dólares.

Trampas:

- la medalla sale del puesto: los nombres van en orden, así que los
  cuatro primeros son oro, y así sucesivamente;
- un pronóstico puede nombrar equipos que no ganaron ninguna medalla;
- los nombres distinguen mayúsculas y pueden constar solo de puntos y
  comas;
- si nadie acierta nada, todos los veteranos empatan con cero y cobran
  todos.

Las cantidades coinciden con una implementación aceptada independiente
en 150 concursos aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1868_implementation.cpp](1868_implementation.cpp) | G++ 13.2 x64 | implementation | O(n k) | AC | 0.015 s | 444 KB |
| [1868_implementation.go](1868_implementation.go) | Go 1.14 x64 | implementation | O(n k) | AC | 0.015 s | 1220 KB |
| [1868_implementation.java](1868_implementation.java) | Java 1.8 | implementation | O(n k) | AC | 0.093 s | 1196 KB |
| [1868_implementation.py](1868_implementation.py) | Python 3.12 x64 | implementation | O(n k) | AC | 0.078 s | 692 KB |
| [1868_implementation.rs](1868_implementation.rs) | Rust 1.75 x64 | implementation | O(n k) | AC | 0.015 s | 536 KB |
