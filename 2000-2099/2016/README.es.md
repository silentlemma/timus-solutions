# 2016. Tramos Rápidos de Tres Arcos Circulares Espaciales

[Timus 2016](https://acm.timus.ru/problem.aspx?space=1&num=2016) · dificultad 6173 · geometry

Problema original de Denis Dublennykh, preparado por Eugene Kurpilyansky, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un punto parte del origen en reposo. Actúan una aceleración constante
`(0,0,a)` hacia arriba y una fuerza de restricción perpendicular al
movimiento, que no realiza trabajo. Primero sube por un círculo de
centro `C1`. Al alcanzar por primera vez el punto de ese círculo más
cercano a `C2`, cambia al centro `C2`, conservando la velocidad
tangente. Se repite el cambio hacia `C3` y finalmente se completa una
vuelta entera alrededor de `C3`. Calcula la longitud total recorrida con
rapidez al menos `v`.

Cada nuevo círculo pasa por el punto de cambio y tiene la velocidad
entrante como tangente. Los dos puntos más cercanos son únicos,
distintos del inicio de su arco, y se alcanzan antes de una vuelta
completa. Ningún cambio coincide con el nuevo centro. La rapidez no
vuelve a cero tras el instante inicial. Se garantiza así una trayectoria
dirigida válida, que puede incluir círculos horizontales.

## Entrada

Primero `t`, `1 ≤ t ≤ 1000`. Cada experimento da enteros `v a`, `1 ≤ v ≤
50 000`, `1 ≤ a ≤ 1000`, seguidos por los tres vectores de centro. Cada
coordenada es un entero en `[-10^6,10^6]` y `C1.x²+C1.y²>0`. No hay un
arco horizontal recorrido con rapidez exactamente `v`. Tiempo límite 1
segundo, memoria 64 MB.

## Salida

Una longitud por experimento, en orden. Se permite error absoluto o
relativo de hasta `10^-6`; las pruebas usan `float:1e-6`. Los puntos
aislados de igualdad con el umbral no aportan longitud.

## Evaluación

Los números se comparan con error absoluto o relativo 10⁻⁶.

## Ejemplos

```
1
10 100
4 0 -3
4 16 2
21 16 2
```

```
35.3929206868
```

El primer arco tiene radio 5 y ángulo `asin(0.8)`, hasta `(4,0,2)`. El
siguiente es un cuarto de círculo horizontal de radio 16, hasta
`(20,16,2)`. El último es un círculo horizontal completo de radio 1. La
rapidez umbral corresponde a altura `0.5`; la parte válida del primer
arco más los dos arcos horizontales completos produce la salida.

## Solución

### De rapidez a altura

La fuerza de restricción es perpendicular a la velocidad y no hace
trabajo. Por unidad de masa, el trabajo de la aceleración ascendente es
`a·Δz`. Con altura y rapidez iniciales nulas, `rapidez²=2az`. Por tanto
basta medir donde `z≥h`, con `h=v²/(2a)`. No se integra el tiempo ni se
simula la aceleración sobre el arco. La rapidez positiva garantiza que
el sentido de marcha no se invierte.

### Representar un círculo dirigido

Guarda centro `C`, radio `R`, vector radial unitario inicial `A` y
tangente unitaria hacia delante `B`, con `A·B=0`. Tras ángulo positivo
`θ`, el punto es `C+R(A cosθ+B sinθ)`. La normal unitaria es `N=A×B`. Al
inicio, `R=|C1|`, `A=−C1/R`; `B` es la proyección normalizada del vector
vertical ascendente sobre el plano perpendicular a `A`.
Equivalentemente, usa la normal orientada sin normalizar
`(-C1.y,C1.x,0)` y `B=unit(N×A)`. La componente horizontal no nula
asegura una tangente existente que apunta hacia arriba.

Para el próximo centro define `q=Cnext−C`, `d=q·N`, `ρ=|q−dN|`. La
dirección radial más cercana es `U=(q−dN)/ρ`. La distancia al cuadrado
es `R²+|q|²−2R·q·U`, cuyo mínimo entre direcciones unitarias del plano
lo da la proyección normalizada. La unicidad asegura `ρ>0`. El ángulo
final es `atan2(U·B,U·A)`; si no es positivo, añade `2π`. La primera
visita y los extremos distintos lo sitúan estrictamente entre cero y
`2π`. La tangente hacia delante allí es `T=N×U`.

### Cambiar de círculo sin cancelación numérica

El nuevo vector radial es `R·U−q=δ·U−d·N`, con `δ=R−ρ`. El radio nuevo
es `hypot(δ,d)` y el radial unitario es `(δU−dN)/Rnew`. La normal
orientada es proporcional a `δN+dU`, pues `(δU−dN)×T=δN+dU`. Normaliza
su producto vectorial con el nuevo radial para recuperar la tangente. En
el tercer círculo usa `2π` sin buscar otro cambio.

Calcular primero el punto en coordenadas globales y restar el nuevo
centro puede perder el diminuto vector radial y estropear el plano
siguiente. Usa la diferencia racionalizada

`δ = (R²−|q|²+d²)/(R+ρ)`.

Se deduce de `ρ²=|q|²−d²`. Emplea sumas compensadas. Obtén
`T=unit(Nraw×q)` y `U=unit(T×N)` para evitar restar proyecciones casi
paralelas. Cuando `d=0`, conserva la normal original sin normalizar y
cambia su signo solo si `δ<0`; normalizarla repetidamente podría romper
la coplanaridad exacta. Los productos enteros iniciales caben en el
rango de enteros exactos de la coma flotante. Conserva `Rnew²=δ²+d²`
para el siguiente cambio. No declares nulo un radio positivo pequeño con
una tolerancia arbitraria.

### Medir el arco por encima del umbral

La altura es `Cz+R(Az cosθ+Bz sinθ)`. Define `F=R·hypot(Az,Bz)` y
`φ=atan2(Bz,Az)`. Si `F=0`, cuenta todo el arco o nada según su altura
constante. En otro caso, sea `u=(h−Cz)/F`: con `u≤−1` cuenta todo; con
`u≥1`, longitud cero. Para `−1<u<1`, toma `α=acos(u)`. Los ángulos
válidos forman intervalos `[φ−α+2πk,φ+α+2πk]`. Intersecta con `[0,L]`,
el ángulo realmente recorrido, suma las anchuras y multiplica por `R`.
Como `L≤2π`, `φ∈[-π,π]` y `α<π`, bastan desplazamientos `k=-2..2`. No
hay solapamiento salvo en extremos.

La identidad energética demuestra la condición de altura. La proyección
y la transferencia de tangente reconstruyen cada arco dirigido
prescrito. Las intersecciones cuentan exactamente los ángulos que
cumplen la condición; multiplicar por radio convierte ángulo en
longitud. Por ello la suma de los tres aportes es correcta.

## Notas por lenguaje

Hay tres arcos y un número fijo de intersecciones por experimento:
tiempo total `O(t)`, espacio geométrico auxiliar `O(1)` por experimento.
Guardar toda la entrada o salida ocupa hasta `O(t)`. En lenguajes con
enteros de 32 bits, convierte la rapidez a coma flotante antes de
elevarla al cuadrado. Las coordenadas pueden ser negativas; busca el
primer ángulo dirigido, no el arco no orientado más corto. Trata aparte
los círculos horizontales e incluye la última vuelta completa. C++ usa
`long double`; Go, Java, Rust y Python usan doble precisión y sumas
compensadas de tres términos. La estabilidad del radio y del plano sigue
siendo esencial aunque la longitud final sea grande.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2016_geometry.cpp](2016_geometry.cpp) | G++ 13.2 x64 | geometry | O(t) | AC | 0.062 s | 544 KB |
| [2016_geometry.go](2016_geometry.go) | Go 1.14 x64 | geometry | O(t) | AC | 0.031 s | 1292 KB |
| [2016_geometry.java](2016_geometry.java) | Java 1.8 | geometry | O(t) | AC | 0.156 s | 3624 KB |
| [2016_geometry.py](2016_geometry.py) | Python 3.12 x64 | geometry | O(t) | AC | 0.171 s | 2084 KB |
| [2016_geometry.rs](2016_geometry.rs) | Rust 1.75 x64 | geometry | O(t) | AC | 0.015 s | 544 KB |
