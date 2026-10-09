# 1086. El n-ésimo número primo

[Timus 1086](https://acm.timus.ru/problem.aspx?space=1&num=1086) · dificultad 106 · number_theory

Problema original del folclore, de la Tercera Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 4 de marzo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada uno de `k` números `n` (`1 ≤ n ≤ 15000`) imprime el `n`-ésimo
número primo. El 1 no es primo.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`k` y luego `k` líneas con `n`.

## Salida

El `n`-ésimo primo para cada `n`, uno por línea.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3
2
5
7
```

Salida:

```
5
3
11
17
```

## Solución

El primo número 15000 es 163 841, así que una criba de Eratóstenes hasta
ese número lista todos los primos que se pueden pedir, y cada consulta es
un índice en la lista. `O(L log log L)` para la criba con `L = 163 842`,
`O(1)` por consulta.

Detalles a tener en cuenta:

- el primer primo es 2, no 1;
- el límite de la criba debe cubrir el propio primo número 15000; se puede
  hallar una vez por cualquier método y escribirlo en el programa;
- el número de consultas no está limitado, así que los primos se calculan
  una sola vez y no en cada consulta.

Las respuestas se comprobaron con primos hallados uno a uno por división
de prueba.

## Notas por lenguaje

- Python tacha los múltiplos asignando cortes en un `bytearray`.
- C++, Go, Java y Rust empiezan a tachar en `p²`; C++ y Java lo calculan
  en 64 bits para no arriesgarse a un desbordamiento.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1086_number_theory.cpp](1086_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log log L) | AC | 0.031 s | 212 KB |
| [1086_number_theory.go](1086_number_theory.go) | Go 1.14 x64 | number_theory | O(L log log L) | AC | 0.001 s | 2308 KB |
| [1086_number_theory.java](1086_number_theory.java) | Java 1.8 | number_theory | O(L log log L) | AC | 0.093 s | 2132 KB |
| [1086_number_theory.py](1086_number_theory.py) | Python 3.12 x64 | number_theory | O(L log log L) | AC | 0.093 s | 2764 KB |
| [1086_number_theory.rs](1086_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log log L) | AC | 0.001 s | 1268 KB |
