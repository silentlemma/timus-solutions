# 2090. Paso de cebra o semáforo: dónde gana cada uno

[Timus 2090](https://acm.timus.ru/problem.aspx?space=1&num=2090) · dificultad 4817 · math, probability

Problema original de Egor Shchelkonogov, del Concurso Individual Abierto de la UrFU 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un peatón camina a velocidad v por la calle Marx hacia su cruce con la
calle Engels y debe llegar a la esquina opuesta. Puede cruzar Marx por
un paso de cebra (sin semáforo) a distancia d antes del cruce y luego
cruzar Engels en el semáforo, o cruzar las dos calles en el semáforo, en
cualquier orden. El semáforo da verde a quien cruza Engels durante t₁,
amarillo t₂, luego verde a quien cruza Marx durante t₃ y amarillo t₄, y
se repite; solo se entra en una calle con verde. La fase al empezar es
uniformemente aleatoria. Hallar la probabilidad de que el paso de cebra
sea estrictamente más rápido y la de que lo sea el semáforo. Los límites
son 1 segundo y 64 MB.

## Entrada

v, después d, w₁ (el ancho de Engels) y w₂ (el ancho de Marx) y después
t₁ … t₄; todos de 1 a 10⁶, con w₁ ≤ v t₂ y w₂ ≤ v t₄.

## Salida

Las dos probabilidades con error absoluto de a lo sumo 10⁻⁹.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
10 1 1
4 1 4 1
```

Salida:

```
0.4 0.1
```

## Solución

Los dos caminos recorren la misma distancia d por Marx; el del paso de
cebra además cruza Marx antes, así que llega a la esquina lejana w₂/v
más tarde que el otro a la cercana, y luego espera el verde de Engels.
Sea θ la fase cuando el camino del semáforo llega al cruce.

- θ en el verde de Engels [0, t₁): el camino del semáforo cruza Engels
  enseguida y luego espera el verde de Marx en t₁ + t₂. El del paso de
  cebra está en la esquina lejana en θ + w₂/v; si eso cae aún dentro del
  verde termina antes (cruzar Engels toma a lo sumo t₂), y si no espera
  un ciclo entero y pierde. Así que el paso de cebra gana en
  [0, t₁ − w₂/v) y el semáforo en los últimos w₂/v del verde.
- θ en el amarillo de Marx (duración t₄): el camino del semáforo no
  puede entrar en ninguna calle y debe esperar el verde de Engels y
  luego mucho el verde de Marx, mientras el del paso de cebra llega al
  siguiente verde de Engels no más tarde; gana el paso de cebra.
- θ en el amarillo de Engels o en el verde de Marx: los dos caminos
  cruzan Engels en el mismo verde, empate.

Así que las probabilidades son (v (t₁ + t₄) − w₂) / (v T) y w₂ / (v T),
con T = t₁ + t₂ + t₃ + t₄. Son racionales, así que se imprimen con una
división larga exacta en enteros, redondeada a 12 decimales y sin ceros
finales.

En el ejemplo v = 1, w₂ = 1 y T = 10: el paso de cebra gana con
probabilidad (4 + 1 − 1) / 10 = 0.4 y el semáforo con 1/10 = 0.1.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2090_math_probability.cpp](2090_math_probability.cpp) | G++ 13.2 x64 | math, probability | O(1) | AC | 0.015 s | 384 KB |
| [2090_math_probability.go](2090_math_probability.go) | Go 1.14 x64 | math, probability | O(1) | AC | 0.031 s | 1120 KB |
| [2090_math_probability.java](2090_math_probability.java) | Java 1.8 | math, probability | O(1) | AC | 0.093 s | 412 KB |
| [2090_math_probability.py](2090_math_probability.py) | Python 3.12 x64 | math, probability | O(1) | AC | 0.109 s | 488 KB |
| [2090_math_probability.rs](2090_math_probability.rs) | Rust 1.75 x64 | math, probability | O(1) | AC | 0.015 s | 244 KB |
