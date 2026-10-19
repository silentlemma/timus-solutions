# 1874. Portería de fútbol

[Timus 1874](https://acm.timus.ru/problem.aspx?space=1&num=1874) · dificultad 199 · geometry

Problema original de Fedor Fominykh, del Concurso Regional de Programación por Equipos de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una portería se construye con un abedul vertical, el suelo y dos palos
de longitudes a y b: el abedul es un poste, y los palos forman el otro
poste y el larguero. La portería puede ser cualquier cuadrilátero. Hay
que hallar su mayor área. El abedul es más alto que a + b.

## Entrada

a y b (1 ≤ a, b ≤ 10 000).

## Salida

La mayor área, con al menos seis cifras tras el punto decimal.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2
```

Salida:

```
4.828427125
```

## Solución

El cuadrilátero tiene un ángulo recto donde el abedul toca el suelo. Su
diagonal c, del punto alto del abedul al extremo lejano en el suelo, lo
divide en dos. Una parte es un triángulo rectángulo de hipotenusa c,
cuya área es como mucho c²/4, alcanzada con catetos iguales. La otra es
el triángulo de los dos palos con ángulo t entre ellos. Entonces
c² = a² + b² − 2ab·cos t, y el total es
(a² + b² − 2ab·cos t)/4 + ab·sin t/2. Su derivada se anula cuando
sin t + cos t = 0, es decir t = 135°, y el área es
(a² + b² + 2√2·ab)/4. `O(1)`.

Para a = b = 2 da (4 + 4 + 8√2)/4 = 2 + 2√2 ≈ 4.828427125.

Trampas:

- la portería no tiene por qué ser un rectángulo; lo único fijo es el
  ángulo recto al pie del abedul;
- el ángulo entre los palos es 135°, no 90°: un ángulo recto solo da
  (a + b)²/4;
- el enunciado garantiza que el abedul es lo bastante alto, así que su
  altura nunca limita la respuesta.

La fórmula coincide con una búsqueda directa sobre el ángulo entre los
palos y con una implementación aceptada independiente en todas las
pruebas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1874_geometry.cpp](1874_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 152 KB |
| [1874_geometry.go](1874_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1136 KB |
| [1874_geometry.java](1874_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1832 KB |
| [1874_geometry.py](1874_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 452 KB |
| [1874_geometry.rs](1874_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 248 KB |
