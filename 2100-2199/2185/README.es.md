# 2185. Pasar muchos valores iniciales por sumar si es negativo y restar si no

[Timus 2185](https://acm.timus.ru/problem.aspx?space=1&num=2185) · dificultad 2080 · math

Problema original de Artyom Stepanov y Artyom Abaturov, del Concurso Escolar de Programación de los Urales 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arreglo a₁ … a_n se aplica a un número x elemento a elemento: si
x < 0 se suma el elemento, y si no se resta. Dar el valor final para
cada uno de q valores iniciales. Los límites son 1.5 segundos y 512 MB.

## Entrada

n y q, 1 ≤ n, q ≤ 10⁶, luego el arreglo con |aᵢ| ≤ 10⁶ y q valores
iniciales con |xᵢ| ≤ 10⁶.

## Salida

El valor final para cada inicio.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2
3 1 2
4
-3
```

Salida:

```
-2
1
```

### Ejemplo 2

Entrada:

```
3 4
2 1 4
10
-5
2
6
```

Salida:

```
3
2
3
-1
```

## Solución

Sea ~x = −x − 1. Un paso conmuta con esta operación: si x ≥ 0 entonces
~x < 0, y ~x + a = −(x − a) − 1 = ~(x − a). Así todo el recorrido cumple
f(~x) = ~f(x), y un inicio negativo se responde desde el inicio no
negativo ~x. Queda procesar a la vez todos los inicios 0 … V, con
V ≤ 10⁶.

Se mantiene un intervalo [L, R] de inicios cuyos valores actuales están
todos del mismo lado del cero, así que todos valen inicio + offset y un
paso solo mueve offset. Cuando un paso hace que el intervalo cruce el
cero en el inicio c = −offset, los inicios menores que c tienen valores
negativos y los desde c no negativos. Un inicio s menor que c vale
s + offset = ~((2c − 1 − s) + offset), el complemento de su espejo
2c − 1 − s del otro lado. Por eso se corta el lado menor con la nota de
copiar el complemento de su espejo, que está en el lado mayor que se
queda, y como la regla de conmutación vale en cada paso posterior, la
relación se mantiene hasta el final.

Al final el intervalo que queda recibe inicio + offset, y los trozos
cortados se rellenan en orden inverso al corte, cada uno desde espejos
ya conocidos. Cada inicio se corta a lo sumo una vez.

En el primer ejemplo 4 pasa por 1, 0 y −2, y −3 = ~2, donde 2 pasa por
−1, 0 y −2, así que −3 termina en ~(−2) = 1.

El recorrido cuesta O(n), el relleno O(V) y las consultas O(q).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2185_math.cpp](2185_math.cpp) | G++ 13.2 x64 | math | O(n + q + V) | AC | 0.218 s | 28892 KB |
| [2185_math.go](2185_math.go) | Go 1.14 x64 | math | O(n + q + V) | AC | 0.218 s | 99692 KB |
| [2185_math.java](2185_math.java) | Java 1.8 | math | O(n + q + V) | AC | 0.703 s | 48808 KB |
| [2185_math.py](2185_math.py) | PyPy 3.10 x64 | math | O(n + q + V) | AC | 1.000 s | 229996 KB |
| [2185_math.rs](2185_math.rs) | Rust 1.75 x64 | math | O(n + q + V) | AC | 0.156 s | 62972 KB |
