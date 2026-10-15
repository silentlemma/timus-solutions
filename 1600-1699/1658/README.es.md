# 1658. Suma de cifras

[Timus 1658](https://acm.timus.ru/problem.aspx?space=1&num=1658) · dificultad 202 · dp

Problema original de Vladimir Yakovlev (idea de Stanislav Vasilyev), del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada una de t consultas, dada la suma s₁ de las cifras de un entero
positivo y la suma s₂ de sus cuadrados, hay que imprimir el menor entero
así, o `No solution` si no hay ninguno de a lo sumo 100 cifras.

## Entrada

t (a lo sumo 10000) y luego t pares s₁ s₂ (1 ≤ s₁, s₂ ≤ 10000).

## Salida

El menor número de cada consulta, o `No solution`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
9 81
12 9
6 10
7 9
```

Salida:

```
9
No solution
1122
111112
```

## Solución

El menor número tiene la menor cantidad de cifras y, entre esos, es la
menor cadena. Nunca contiene un cero: un cero añade una cifra sin cambiar
ninguna suma, así que no sería el más corto. Con a lo sumo 100 cifras las
sumas no pasan de 900 y 8100, así que las consultas mayores no tienen
respuesta.

Una tabla con la menor cantidad de cifras no nulas para cada par
(s₁, s₂) hasta 900 × 8100 se llena en una pasada: cada casilla es una más
que la mejor casilla a la que se llega quitando una cifra d y d². La
respuesta se construye de forma voraz: la primera cifra es la menor d
tras la cual al resto le falta exactamente una cifra menos, y así
sucesivamente. Las cifras salen ordenadas, así que cada búsqueda puede
empezar en la cifra anterior. `O(S₁ · S₂ · 9)` para la tabla y `O(100)`
por consulta.

Detalles a tener en cuenta:

- la tabla tiene 7,3 millones de casillas, así que se guarda en bytes;
- una suma de cuadrados menor que la de cifras, o mayor que nueve veces
  ella, es imposible; la tabla lo recoge sin casos especiales;
- s₁ = 900 con s₂ = 8100 son cien nueves, una cifra más ya es demasiado
  larga (prueba 02).

Las respuestas coinciden con una implementación aceptada independiente
en 80 000 consultas.

## Notas por lenguaje

- Python no puede llenar una tabla de 7,3 millones de casillas a tiempo,
  así que guarda, para cada número de cifras k, un entero grande por suma
  de cifras cuyos bits marcan las sumas de cuadrados alcanzables; una capa
  nueva es un «o» de la anterior desplazada d² para cada cifra d. Ocupa
  unos 16 MB y una fracción de segundo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1658_dp.cpp](1658_dp.cpp) | G++ 13.2 x64 | dp | O(S₁ · S₂ · 9) | AC | 0.140 s | 9592 KB |
| [1658_dp.go](1658_dp.go) | Go 1.14 x64 | dp | O(S₁ · S₂ · 9) | AC | 0.203 s | 12960 KB |
| [1658_dp.java](1658_dp.java) | Java 1.8 | dp | O(S₁ · S₂ · 9) | AC | 0.265 s | 14264 KB |
| [1658_dp.py](1658_dp.py) | Python 3.12 x64 | dp | O(S₁ · S₂ · 9) | AC | 1.578 s | 23432 KB |
| [1658_dp.rs](1658_dp.rs) | Rust 1.75 x64 | dp | O(S₁ · S₂ · 9) | AC | 0.140 s | 9596 KB |
