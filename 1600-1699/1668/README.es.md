# 1668. Estrella de la Muerte 2

[Timus 1668](https://acm.timus.ru/problem.aspx?space=1&num=1668) · dificultad 5684 · math

Problema original de Alex Samsonov, del Ural SU Contest en el campus de invierno de Petrozavodsk, enero de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una estación en un espacio de N dimensiones tiene M motores fijos. Dar
X unidades de energía al motor i suma X · A_ij a la coordenada j del
empuje, y X puede ser negativo. Hay que elegir X₁ … X_M para que el
empuje total quede lo más cerca posible de un vector b y, entre esas
elecciones, la de menor suma de cuadrados de X.

## Entrada

N y M (1 ≤ N, M ≤ 100), luego M filas de N enteros A_ij y luego los N
enteros de b; todos de valor absoluto a lo sumo 100.

## Salida

X₁ … X_M con cinco cifras tras el punto decimal.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
2 3 -2 1
-1 2 1 3
4 2 3 -2
3 13 -9 13
```

Salida:

```
4.00000 2.00000 -1.00000
```

## Solución

El empuje es Σ Xᵢ aᵢ, donde aᵢ es la fila i de A. Es el problema de
mínimos cuadrados para la matriz de columnas aᵢ, y la más corta de sus
soluciones (la respuesta de la pseudoinversa) es única: es la solución
que está en el espacio generado por los vectores cⱼ = (A₁ⱼ, …, A_Mⱼ),
las columnas de A, porque cualquier parte ortogonal a ellos no cambia el
empuje y solo añade longitud.

1. Se elige un conjunto independiente maximal entre los cⱼ. En coma
   flotante haría falta un umbral de «casi dependientes»; en cambio la
   eliminación se hace módulo el primo 10⁹ + 7, de forma exacta. Un
   conjunto independiente módulo el primo lo es sobre los racionales; el
   rango módulo el primo solo podría salir menor si el primo dividiera
   todos los menores de orden r, lo que exige una matriz construida
   contra ese primo.
2. Los vectores elegidos se convierten en una base ortonormal q₁ … q_r
   con Gram–Schmidt, restando cada proyección dos veces: la segunda
   pasada recupera la ortogonalidad perdida por redondeo.
3. Con X = Σ w_k q_k, el empuje es K w con K_jk = cⱼ · q_k, y K tiene
   rango completo por columnas. Una segunda QR de K, también con
   Gram–Schmidt, da el w de mínimos cuadrados por sustitución hacia
   atrás, y de ahí X.

Ningún paso forma AᵀA, así que el número de condición nunca se eleva al
cuadrado. `O(N · M · min(N, M))`.

Detalles a tener en cuenta:

- con motores dependientes el mejor empuje se alcanza con muchos X, y
  solo el más corto es correcto (pruebas 03 y 05);
- un motor muerto recibe 0, y una matriz nula da todo ceros (prueba
  02);
- los resultados negativos diminutos se imprimen como `-0.00000`, así
  que los valores por debajo de 5 · 10⁻⁶ se ponen a cero.

Las respuestas coinciden con un cálculo exacto con fracciones en unas
300 entradas pequeñas y con una implementación aceptada independiente en
las grandes.

## Notas por lenguaje

- Python se ejecuta con PyPy: CPython tarda aquí 0,2–0,4 s con entradas
  de 100 × 100 frente a un límite de 0,5 s, demasiado justo para el
  juez, y PyPy unos 0,1 s. La versión de CPython igualmente guarda Q
  traspuesta para que cada proyección sea una pasada de sumas internas
  por fila.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1668_math.cpp](1668_math.cpp) | G++ 13.2 x64 | math | O(N M min(N, M)) | AC | 0.031 s | 632 KB |
| [1668_math.go](1668_math.go) | Go 1.14 x64 | math | O(N M min(N, M)) | AC | 0.046 s | 2060 KB |
| [1668_math.java](1668_math.java) | Java 1.8 | math | O(N M min(N, M)) | AC | 0.109 s | 1788 KB |
| [1668_math.py](1668_math.py) | PyPy 3.10 x64 | math | O(N M min(N, M)) | AC | 0.250 s | 6936 KB |
| [1668_math.rs](1668_math.rs) | Rust 1.75 x64 | math | O(N M min(N, M)) | AC | 0.031 s | 1000 KB |
