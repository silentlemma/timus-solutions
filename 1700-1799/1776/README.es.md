# 1776. Fuegos artificiales del aniversario

[Timus 1776](https://acm.timus.ru/problem.aspx?space=1&num=1776) · dificultad 465 · dp

Problema original de Alex Samsonov, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n cohetes están en fila. La primera salva lanza los dos cohetes de los
extremos. Antes de cada salva siguiente, en cada tramo no vacío de
cohetes entre dos vecinos ya lanzados se elige un cohete al azar, con
igual probabilidad, y todos los elegidos salen en esa salva. Las salvas
van cada diez segundos, y el espectáculo acaba con la salva que lanza
el último cohete. Hallar la duración esperada del espectáculo en
segundos.

## Entrada

n (3 ≤ n ≤ 400).

## Salida

La duración esperada con un error absoluto o relativo de a lo sumo
10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
```

Salida:

```
26.66666666666
```

## Solución

Tras la primera salva los m = n − 2 cohetes interiores forman un tramo,
y un tramo de i cohetes se parte en su cohete elegido en tramos de l e
i − 1 − l cohetes, para cada l con probabilidad 1/i, que siguen después
de forma independiente. Sea done(i, j) la probabilidad de que un tramo
de i cohetes termine en a lo sumo j salvas más: done(0, j) = 1,
done(i, j) = 1 si i ≤ j, y si no

done(i, j) = (1/i) · Σ done(l, j − 1) · done(i − 1 − l, j − 1).

El número esperado de salvas posteriores es Σ (1 − done(m, j)) sobre
j ≥ 0, y la respuesta es diez veces eso. El número de salvas se comporta
como la altura de un árbol de búsqueda aleatorio, unas 4,3 ln m, y su
cola cae muy deprisa, así que la suma se detiene en cuanto
1 − done(m, j) baja de 10⁻¹⁵: unas pocas decenas de rondas de `O(m²)`
en vez de `O(m³)`.

Con cinco cohetes los tres interiores se parten en el del medio con
probabilidad 1/3, y quedan dos salvas más, y si no hacen falta tres:
10 × (2/3 · 3 + 1/3 · 2) = 26,67 segundos.

Trampas:

- la primera salva empieza el espectáculo y no suma tiempo;
- los tramos se parten de forma independiente, así que la probabilidad
  de un tramo es el producto de las de sus dos partes;
- sumar las m rondas también funciona pero cuesta `O(m³)`, demasiado
  lento en algunos lenguajes.

Las respuestas coinciden con una implementación aceptada independiente,
que suma todas las rondas, para muchos valores de n hasta 400, con
10⁻⁹.

## Soluciones optimizadas

Go y Rust reutilizan dos filas de probabilidades de finalización done(i, j) de la recurrencia anterior. Emparejan términos simétricos l e i − 1 − l y añaden el cuadrado central cuando i es impar. Suman desde j = 0 hasta m − 1, con m = n − 2. Cada salva adicional lanza al menos un cohete restante, así que desde j = m la probabilidad de continuar es cero. El tiempo es O(m³), con una constante menor por simetría, y el espacio es O(m) memoria sin asignaciones por ronda. Puede calcular más rondas que la base. Nueve decimales limitan el redondeo de formato a 0,5·10⁻⁹, bajo la tolerancia. Go usa descriptores estándar y Rust la entrada y salida estándar de C. Las bases de C++, Java y Python también cubren las versiones rápidas.

El envío aceptado en Rust 1.75 x64 tarda 0.046 s frente a 0.015 s de la base y usa 52 KB frente a 240 KB.

Las implementaciones base aceptadas [1776_dp.cpp](1776_dp.cpp), [1776_dp.java](1776_dp.java), [1776_dp.py](1776_dp.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1776_dp.cpp](1776_dp.cpp) | G++ 13.2 x64 | dp | O(m^2) per volley, a few dozen volleys | AC | 0.015 s | 216 KB | 11289720 |
| [1776_dp.go](1776_dp.go) | Go 1.14 x64 | dp | O(m^2) per volley, a few dozen volleys | AC | 0.031 s | 1228 KB | 11289721 |
| [1776_dp.java](1776_dp.java) | Java 1.8 | dp | O(m^2) per volley, a few dozen volleys | AC | 0.125 s | 1932 KB | 11289725 |
| [1776_dp.py](1776_dp.py) \* | Python 3.12 x64 | dp | O(m^2) per volley, a few dozen volleys | AC | 0.250 s | 1328 KB | 11289724 |
| [1776_dp.rs](1776_dp.rs) | Rust 1.75 x64 | dp | O(m^2) per volley, a few dozen volleys | AC | 0.015 s | 240 KB | 11289726 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1776_dp_optimized.go](1776_dp_optimized.go) \* | Go 1.14 x64 | dp | O(m³) | AC | 0.015 s | 308 KB | 11315269 |
| [1776_dp_optimized.rs](1776_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(m³) | AC | 0.046 s | 52 KB | 11315900 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
