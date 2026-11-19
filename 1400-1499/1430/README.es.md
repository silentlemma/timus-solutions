# 1430. Crimen y castigo

[Timus 1430](https://acm.timus.ru/problem.aspx?space=1&num=1430) · dificultad 461 · number_theory

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los artículos cuestan A o B cada uno, se puede comprar cualquier
cantidad de cada uno y hay N para gastar (1 ≤ A, B, N ≤ 2·10⁹). Hay que
hallar cantidades x e y con x·A + y·B ≤ N lo mayor posible; vale
cualquier par óptimo.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

A, B y N.

## Salida

x e y.

## Evaluación

El repositorio usa un comprobador semántico y acepta cualquier salida que satisfaga estas condiciones. Emite dos cantidades no negativas en el orden original de precios. El coste no debe superar N y debe igualar el máximo gasto posible; cualquier par óptimo empatado es válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
8 5 22
```

Salida:

```
2 1
```

## Solución

Sea A ≥ B (si no, se intercambian y luego se intercambia la respuesta).
Si x ≥ B, entonces B artículos de precio A pueden cambiarse por A de
precio B con el mismo total, así que alguna respuesta óptima tiene
x < B; y x·A ≤ N da x ≤ N / A. Así que x va de 0 a min(N / A, B − 1), y
para cada x el resto compra y = (N − x·A) / B artículos de precio B.
Como A ≥ B, o bien B ≤ √N o bien N / A < √N, así que hay como mucho unos
44 722 valores de x; además el bucle para en cuanto se gasta justo N.
`O(√N)`.

Detalles a tener en cuenta:

- productos como x·A caben en 32 bits con signo (pruebas 03, 06);
- si ambos precios superan N, no se compra nada (prueba 12);
- la respuesta no es única, así que las pruebas usan un verificador
  (prueba 02).

## Soluciones optimizadas

Las nuevas versiones C++, Go y Rust mantienen la enumeración acotada. Con A≥B y g=gcd(A,B), B/g artículos de precio A se cambian por A/g de precio B sin alterar el coste; basta 0≤x≤min(floor(N/A),B/g−1). El sobrante r=(N−xA) mod B parte de N mod B y se actualiza restando A mod B, sumando B al hacerse negativo: no hay división dentro del bucle. Se conserva el menor sobrante y se recupera y al final. Todo coste es múltiplo de g: N mod g es una cota inferior demostrada que permite salir pronto. El peor caso sigue O(√N), más Euclides; mejoran aritmética y constantes. La E/S acotada de Go y el C runtime de Rust reducen almacenamiento. Se conservan las bases; Java/Python reutilizan las ya admitidas.

Las implementaciones base aceptadas [1430_number_theory.java](1430_number_theory.java), [1430_number_theory.py](1430_number_theory.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

`1430_number_theory_optimized.java`. Java conserva el algoritmo y las estructuras descritas para la versión sencilla. Un búfer fijo de bytes y FastInput sustituyen Scanner y su maquinaria de expresiones regulares y configuración regional. Los enteros se analizan directamente; las cadenas siguen decodificándose como UTF-8 cuando se solicitan y los decimales mantienen conversión numérica explícita. La anticipación guarda un token solo cuando hace falta. El algoritmo de salida no cambia. Se elimina el coste del análisis general; la tabla describe el trabajo algorítmico, con lectura lineal en bytes y un búfer acotado.

Frente a `1430_number_theory.java`: tiempo 0.109 s → 0.109 s; memoria 1684 KB → 492 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1430_number_theory.cpp](1430_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt N) | AC | 0.031 s | 128 KB | 11286201 |
| [1430_number_theory.go](1430_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt N) | AC | 0.031 s | 1068 KB | 11286202 |
| [1430_number_theory.java](1430_number_theory.java) \* | Java 1.8 | number_theory | O(sqrt N) | AC | 0.109 s | 1684 KB | 11286204 |
| [1430_number_theory.py](1430_number_theory.py) \* | Python 3.12 x64 | number_theory | O(sqrt N) | AC | 0.109 s | 468 KB | 11286203 |
| [1430_number_theory.rs](1430_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt N) | AC | 0.062 s | 220 KB | 11286205 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1430_number_theory_optimized.cpp](1430_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(sqrt N + log min(A,B)) | AC | 0.015 s | 108 KB | 11315180 |
| [1430_number_theory_optimized.go](1430_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(sqrt N + log min(A,B)) | AC | 0.031 s | 292 KB | 11315184 |
| [1430_number_theory_optimized.rs](1430_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(sqrt N + log min(A,B)) | AC | 0.046 s | 56 KB | 11315187 |
| [1430_number_theory_optimized.java](1430_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(sqrt N) | AC | 0.109 s | 492 KB | 11324975 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
