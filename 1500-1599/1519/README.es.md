# 1519. Fórmula 1

[Timus 1519](https://acm.timus.ru/problem.aspx?space=1&num=1519) · dificultad 466 · dp

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un terreno de N × M casillas (2 ≤ N, M ≤ 12) tiene algunas casillas
ocupadas por madrigueras. Un circuito es un único lazo cerrado que pasa
exactamente una vez por cada casilla libre, moviéndose entre casillas
con un lado común. Hay que contar los circuitos; su número cabe en 63
bits.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, y luego N filas de M caracteres: '.' libre, '*' madriguera. Hay
al menos cuatro casillas libres.

## Salida

El número de circuitos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
**..
....
....
....
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
4 4
....
....
....
....
```

Salida:

```
6
```

## Solución

Programación dinámica sobre un perfil quebrado, casilla a casilla por
filas, con la conectividad de los trozos que cruzan el perfil como
estado. El perfil tiene M + 1 conectores: los lados inferiores de las
casillas de la fila anterior o actual y el lado
izquierdo de la casilla actual. Cada conector está vacío o es un
extremo de un trozo de camino, y los dos extremos de cada trozo se
anidan como paréntesis, así que un conector es «(», «)» o nada: 2 bits,
y un estado cabe en 26 bits. En una casilla libre con conector
izquierdo L y superior U:

- sin conectores: se abre un trozo nuevo hacia la derecha y hacia abajo;
- un conector: se continúa a la derecha o hacia abajo;
- «(» y «(»: se unen los trozos, y el «)» pareja de U pasa a «(»;
- «)» y «)»: se unen, y el «(» pareja de L pasa a «)»;
- «)» y «(»: se unen dos trozos en uno;
- «(» y «)»: esto cierra un lazo, permitido solo en la última casilla
  libre y sin otros conectores, y entonces cuenta.

Una madriguera solo deja pasar estados con ambos conectores vacíos. Al
final de cada fila el perfil se desplaza un conector. En el terreno vacío
de 12 × 12 hay como mucho unos 14000 estados a la vez, y el trabajo es
`O(N·M²·S)` con S estados.

Detalles a tener en cuenta:

- el lazo solo puede cerrarse en la última casilla libre, cuando no
  queda nada abierto (prueba 09);
- un número impar de casillas libres, o una zona libre separada del
  resto, da 0 (pruebas 05, 06, 08);
- el terreno vacío de 12 × 12 tiene unos 1.08·10¹⁸ circuitos, así que
  los números necesitan 64 bits (prueba 03);
- las madrigueras sueltas casi nunca dejan circuitos, así que las
  pruebas generadas recortan sobre todo bloques enteros de 2 × 2 (gen1,
  gen2, gen3).

## Notas por lenguaje

- Python se ejecuta con PyPy: CPython excede el límite de 1 s en la
  prueba 18 del juez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1519_dp.cpp](1519_dp.cpp) | G++ 13.2 x64 | dp | O(N * M^2 * S) | AC | 0.203 s | 2076 KB |
| [1519_dp.go](1519_dp.go) | Go 1.14 x64 | dp | O(N * M^2 * S) | AC | 0.203 s | 10420 KB |
| [1519_dp.java](1519_dp.java) | Java 1.8 | dp | O(N * M^2 * S) | AC | 0.328 s | 18436 KB |
| [1519_dp.py](1519_dp.py) | PyPy 3.10 x64 | dp | O(N * M^2 * S) | AC | 0.609 s | 10768 KB |
| [1519_dp.rs](1519_dp.rs) | Rust 1.75 x64 | dp | O(N * M^2 * S) | AC | 0.062 s | 1600 KB |
