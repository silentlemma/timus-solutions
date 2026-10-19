# 1988. Encuentro sobre una esfera sin atravesarla

[Timus 1988](https://acm.timus.ru/problem.aspx?space=1&num=1988) · dificultad 1153 · geometry

Problema original de Mikhail Rubinchik, del Campeonato Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una esfera centrada en el origen tiene radio `R=|A|>0`. Un viajero
empieza en `A`, sobre la superficie, y se mueve por ella a velocidad
como máximo 1. Otro empieza en `S`, con `|S|>R`, y viaja fuera de la
esfera o sobre ella a velocidad como máximo `v`. Hallar el primer
instante en que pueden encontrarse. Ambos pueden esperar.

Las coordenadas de `A` y `S` son enteros de valor absoluto como máximo
100, `1≤v≤100` es entero y `0<|A|²<|S|²`. Límites: 0,5 segundos y 64 MB.

## Entrada

Tres líneas: las tres coordenadas de `A`, las tres de `S` y la velocidad `v`.

## Salida

Un número real: el tiempo mínimo de encuentro.

## Evaluación

Los números se comparan con error absoluto o relativo 10⁻⁶.

## Ejemplos

Entrada:

```
-1 1 -1
10 10 10
1
```

Salida:

```
15.588457
```

## Solución

Sean `D=|S|` y `θ` el ángulo entre `A` y `S`. Medir el ángulo `β` de un
punto superficial desde la dirección de `S`. Para un `β` fijo, la mínima
distancia superficial desde `A` es `R|θ−β|`, alcanzada en un círculo
máximo que pasa por ambas direcciones iniciales, por la desigualdad
triangular esférica. Los puntos con `β>θ` son peores que el punto
inicial superficial: no acortan el vuelo y requieren movimiento
superficial. Basta buscar `0≤β≤θ` sobre el arco corto hacia el punto
situado justo debajo de `S`.

### Vuelo mínimo alrededor del obstáculo

Sean `h=√(D²−R²)` y `α=atan2(h,R)`, el radio angular del casquete
visible. La distancia mínima legal hasta un destino de ángulo `β` es:

- `L(β)=√((D−R)²+4DR sin²(β/2))` si `β≤α`: segmento visible directo;
- `L(β)=h+R(β−α)` si `β>α`: segmento tangente y arco superficial.

La segunda expresión limita por abajo cualquier ruta exterior. Para
llegar a `β>α`, una ruta debe cruzar primero el cono de ángulo `α`. En
el cruce tiene radio `ρ≥R`; como `D cos α=R`, su distancia desde `S` es
al menos `√((ρ−R)²+D²−R²)≥h`. La parte restante mide al menos `R(β−α)`,
pues la proyección radial de una ruta exterior sobre la esfera no
aumenta su longitud. La tangente y el arco máximo alcanzan ambas cotas.
En el caso visible, el segmento directo alcanza la cota euclídea.

### Equilibrar las llegadas

El viajero superficial necesita tiempo `R(θ−β)` y el exterior `L(β)/v`.
Como pueden esperar, el tiempo de encuentro es el máximo, no la suma. La
primera función decrece con `β`; la segunda crece continuamente.

Si `Rθ≤(D−R)/v`, pueden encontrarse en `β=0` tras `(D−R)/v`; es óptimo
porque todo vuelo hasta la esfera mide al menos `D−R`. Si no, los
tiempos se igualan una única vez en `(0,θ)`. Hacer 80 pasos de bisección
angular: si tarda más el viajero superficial, aumentar el límite
inferior; en otro caso, reducir el superior. Evaluar el máximo de
tiempos en el punto medio final.

### Evaluación estable y corrección

Calcular productos escalares, vectoriales y `Δ=|S|²−|A|²` como enteros.
Usar `θ=atan2(|A×S|,A·S)` maneja inicios paralelos y antiparalelos sin
dividir entre el producto vectorial. El hueco radial se calcula como
`Δ/(D+R)`, evitando restar raíces próximas. El vuelo visible usa
`hypot(D−R,2√(DR) sin(β/2))`, sin restar cuadrados cercanos.

Como `v≥1`, ambas funciones temporales tienen constante de Lipschitz
como máximo `R`. Después de 80 pasos, el error matemático de búsqueda es
como máximo `Rπ/2⁸⁰<5·10⁻²²`. Doble precisión y diez cifras decimales
dejan margen frente a `10⁻⁶`; la evaluación flotante también se
comprueba con alta precisión independiente. Las normas al cuadrado no
superan 30 000 y su diferencia es un entero positivo: el hueco radial es
al menos `1/(2√30000)`, por lo que el tiempo mínimo es positivo incluso
a velocidad 100.

En el ejemplo `R=√3` y `D=10√3`. El viajero superficial llega debajo de
`S` antes del vuelo radial, por lo que el óptimo es `9√3≈15.5884572681`,
acorde con la salida dentro de la tolerancia.

Son 80 iteraciones de tamaño constante: tiempo `O(B)` con `B=80`, es
decir `O(1)` bajo las restricciones, y memoria `O(1)`.

Trampas:

- Una cuerda hacia un punto no visible atraviesa la esfera y está prohibida.
- El encuentro usa el máximo de las llegadas; ambos pueden esperar.
- Las distancias superficiales son arcos máximos, no cuerdas.
- Incluir el óptimo de frontera justo debajo del inicio exterior.
- Usar radianes y cálculo estable del ángulo con productos escalar y vectorial.
- Conservar `|S|²>|A|²>0` al generar pruebas.

## Notas por lenguaje

Los cinco programas usan la misma bisección angular de 80 pasos y
geometría de doble precisión. Los lenguajes compilados usan enteros
amplios para los productos; Python usa enteros exactos. Todos ofrecen
`atan2` e `hypot`. Java fija la configuración regional para imprimir el
punto decimal.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1988_geometry.cpp](1988_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 480 KB |
| [1988_geometry.go](1988_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1120 KB |
| [1988_geometry.java](1988_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1816 KB |
| [1988_geometry.py](1988_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 736 KB |
| [1988_geometry.rs](1988_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 264 KB |
