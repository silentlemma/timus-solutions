# 1876. La mañana del ciempiés

[Timus 1876](https://acm.timus.ru/problem.aspx?space=1&num=1876) · dificultad 55 · math

Problema original de Mikhail Rubinchik, del Concurso Regional de Programación por Equipos de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un ciempiés tiene 40 patas izquierdas y 40 derechas, y bajo la cama hay
a zapatillas izquierdas y b derechas. Primero calza las patas
izquierdas: sacar una zapatilla cuesta un segundo. Una zapatilla
izquierda va a la siguiente pata izquierda. Una derecha cuesta un
segundo más, para ponerla en una pata derecha descalza o, si todas las
derechas están calzadas, para tirarla. Luego se calzan las patas
derechas de la misma forma. ¿Cuántos segundos tarda en el peor caso?

## Entrada

a y b (40 ≤ a, b ≤ 100).

## Salida

El número de segundos en el peor caso.

## Ejemplos

### Ejemplo 1

Entrada:

```
40 40
```

Salida:

```
120
```

## Solución

Supongamos que salen k zapatillas derechas mientras se calzan las patas
izquierdas; la fase izquierda cuesta 40 + 2k segundos. Si k ≥ 40, todas
las patas derechas ya están calzadas y la fase derecha queda vacía. El
peor caso así saca primero las b derechas: 2b + 40 segundos. Si k < 40,
la fase derecha puede sacar primero las a − 40 izquierdas sobrantes, a
dos segundos cada una, y después las 40 − k derechas que faltan. El
total es 2a + k, máximo con k = 39: 2a + 39. La respuesta es
max(2b + 40, 2a + 39). `O(1)`.

Con 40 zapatillas de cada tipo ambos caminos dan como mucho 120
segundos.

Trampas:

- las zapatillas izquierdas sobrantes solo pueden salir en la fase
  derecha, así que la fase izquierda no debe calzar todas las patas
  derechas: lo peor es 39;
- cuando todas las patas derechas están calzadas, tras la fase
  izquierda no pasa nada más;
- con a = 41 y b = 40 ya gana el segundo caso: 121 frente a 120.

La fórmula coincide con una búsqueda sobre todos los órdenes de sacar
zapatillas para todas las entradas, y con una implementación aceptada
independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1876_math.cpp](1876_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1876_math.go](1876_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1076 KB |
| [1876_math.java](1876_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1600 KB |
| [1876_math.py](1876_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 376 KB |
| [1876_math.rs](1876_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 236 KB |
