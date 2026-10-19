# 2069. La mejor ruta con a lo sumo dos giros

[Timus 2069](https://acm.timus.ru/problem.aspx?space=1&num=2069) · dificultad 226 · greedy

Problema original de Oleg Merkurev, preparado por Alexander Borzunov, del Concurso Regional Escolar de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad es una cuadrícula de n calles verticales y m horizontales, y
cada calle tiene su propia popularidad. Una ruta va por las calles desde
la esquina superior izquierda hasta la inferior derecha, y su genialidad
es la menor popularidad entre las calles en las que recorre una
distancia no nula. Hallar la mayor genialidad posible. Los límites son
1 segundo y 64 MB.

## Entrada

n y m, 2 ≤ n, m ≤ 10⁵, después las n popularidades de las calles
verticales de izquierda a derecha y las m de las horizontales de arriba
abajo, una por línea, cada una de 1 a 10⁹.

## Salida

La mayor genialidad.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
4
8
2
7
3
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
4 3
12
4
12
3
21
5
16
```

Salida:

```
12
```

## Solución

Sean v₁ … vₙ las calles verticales y h₁ … hₘ las horizontales; la ruta
empieza donde se cruzan v₁ y h₁ y termina donde se cruzan vₙ y hₘ. Su
primer paso va por v₁ o por h₁, y el último por vₙ o por hₘ, así que hay
cuatro casos.

- Empieza en v₁ y termina en hₘ. La genialidad es como mucho
  min(v₁, hₘ), y bajar por v₁ y luego ir a la derecha por hₘ la alcanza.
- Empieza en h₁ y termina en vₙ: como mucho min(h₁, vₙ), que se alcanza
  yendo a la derecha y luego hacia abajo.
- Empieza en h₁ y termina en hₘ. Para cambiar de fila la ruta debe
  recorrer alguna calle vertical, así que la genialidad es como mucho
  min(h₁, max v, hₘ). Ir a la derecha por h₁ hasta la mejor calle
  vertical, bajar por ella e ir a la derecha por hₘ alcanza esa cota.
- Empieza en v₁ y termina en vₙ: de forma simétrica min(v₁, max h, vₙ).

Toda ruta cae en uno de los casos y cada cota se alcanza, así que la
respuesta es el mayor de los cuatro valores, en O(n + m).

En el primer ejemplo los dos primeros casos dan min(4, 3) = 3 y
min(2, 8) = 2, mientras que el último baja por v₁ = 4, va a la derecha
por h₂ = 7 y baja por v₂ = 8, con genialidad 4.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2069_greedy.cpp](2069_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.140 s | 988 KB |
| [2069_greedy.go](2069_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.062 s | 5704 KB |
| [2069_greedy.java](2069_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.140 s | 1344 KB |
| [2069_greedy.py](2069_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.109 s | 21716 KB |
| [2069_greedy.rs](2069_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.031 s | 6328 KB |
