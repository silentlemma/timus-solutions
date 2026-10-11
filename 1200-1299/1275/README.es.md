# 1275. Los caballeros de la Mesa Redonda

[Timus 1275](https://acm.timus.ru/problem.aspx?space=1&num=1275) · dificultad 2249 · math

Problema original de Sergey Volchenkov, Vladimir Pinaev y Michael Kopachev, del cuarto de final de la región central de Rusia del ACM ICPC 2003–2004, Rybinsk, 15–16 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N caballeros (2 ≤ N ≤ 1000) se sientan a una mesa redonda, cada uno con
algunas copas. En cada visita, un sirviente lleva una copa a cada uno de
dos caballeros sentados a K puestos de distancia, o se lleva una de cada
uno. Al final cada caballero debe tener F copas, y no se puede llevar
una copa que no está. Hay que dar un plan con el menor número de visitas,
o imprimir −1 si no existe. Las cantidades iniciales y F están entre
0 y 1000 y un plan óptimo tiene como mucho 30 000 visitas.

Límite de tiempo: 0,1 segundos. Límite de memoria: 0,5 MB. El enunciado
admite C, C++ y Pascal; el formulario de envío ofrece además Rust.

## Entrada

N, K y F, y luego las N cantidades de copas.

## Salida

El número de visitas M y las visitas como `i j +` o `i j -`, o −1.

## Evaluación

Puede haber muchos planes óptimos, así que el evaluador acepta
cualquiera: el número de visitas debe ser el menor posible, cada visita
debe servir a dos caballeros a K puestos, las cantidades deben mantenerse
no negativas y todos deben acabar con F.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 1 4
1 2 3
```

Salida:

```
3
1 2 +
1 2 +
3 1 +
```

## Solución

Sea x_i el número de visitas con signo al par (i, i + K): positivo si se
traen copas, negativo si se llevan. Mezclar ambas cosas en un par solo
desperdicia visitas. El caballero i está en los pares (i, i + K) e
(i − K, i), así que x_(i−K) + x_i debe valer F menos sus copas.

Los caballeros se dividen en gcd(N, K) ciclos i, i + K, i + 2K, …, cada
uno de longitud L = N / gcd(N, K), y cada ciclo se resuelve aparte.
Tomando la primera incógnita como t, cada regla fija la siguiente, y
queda x_j = ±t + c_j con signos alternos. La última regla cierra el
ciclo:

- si L es impar, da 2t = r: hay exactamente una solución, y ninguna si
  r es impar;
- si L es par, t se cancela: no hay solución salvo que r = 0, y entonces
  vale cualquier t. El número de visitas Σ |t − p_j| sobre los puntos
  p_j = ∓c_j es mínimo cuando t es una mediana de ellos.

Primero se imprimen todas las visitas que traen copas y después las que
se las llevan. Así cada caballero primero solo gana copas y luego solo
las pierde, de modo que las cantidades se mantienen no negativas y
acaban en F ≥ 0.

Detalles a tener en cuenta:

- en un ciclo par, dejar el primer par sin visitas puede ser subóptimo;
  la mediana elige la mejor cantidad (prueba gen3);
- imprimir un `-` antes del `+` del que depende puede llevarse una copa
  que aún no está;
- con N = 2K los pares (i, i + K) e (i + K, i) son el mismo, y ambos
  caballeros deben necesitar el mismo cambio (prueba 07);
- el límite de memoria no permite nada pesado: solo los flujos de C++ ya
  ocupan demasiado, así que el programa usa `scanf` y `printf`.

El menor número de visitas se comparó con una búsqueda exhaustiva sobre
todos los planes en 400 mesas aleatorias de hasta cinco caballeros.

## Notas por lenguaje

- El enunciado solo admite C, C++ y Pascal, pero el formulario de envío
  de Timus ofrece además Rust 1.75, así que hay soluciones en C++ y Rust;
  Go, Python y Java no se pueden enviar.
- C++ guarda los cambios de copas y las visitas con signo como `int`, y
  usa `long long` para t y el total; Rust usa `i64` para esos cambios,
  visitas y t, y `u64` para el total. Rust también implementa la entrada y
  la salida con buffers fijos de 4096 bytes en lugar de `scanf` y `printf`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1275_math.cpp](1275_math.cpp) | G++ 13.2 x64 | math | O(N + M) (on average) | AC | 0.015 s | 152 KB |
| [1275_math.rs](1275_math.rs) | Rust 1.75 x64 | math | O(N + M) | AC | 0.031 s | 244 KB |
