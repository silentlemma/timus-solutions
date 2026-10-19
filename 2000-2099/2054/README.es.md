# 2054. Altura solar mediante dos rotaciones

[Timus 2054](https://acm.timus.ru/problem.aspx?space=1&num=2054) · difficulty 5878 · geometry

Problema original de Dmitry Ivankov, del Campeonato de Programación Deportiva de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La Tierra es una esfera cuyo eje mantiene la dirección y está inclinado
ε = 23.439281° respecto a la normal de su órbita circular; la traslación
y la rotación son antihorarias vistas desde el norte. Un año tiene
exactamente 365 días de 24 horas solares iguales, y al mediodía del 21
de junio, solsticio de verano del norte, el Sol está en el meridiano del
observador. La luz solar es paralela a la recta Tierra–Sol. Para
momentos dados, hallar la altura del Sol sobre el horizonte en una
latitud dada, o 0 si está por debajo. Los límites son 1 segundo y 64 MB.

## Entrada

La primera línea tiene la latitud l, −89.99 ≤ l ≤ 89.99 con a lo sumo
dos decimales, y el número de consultas n, 1 ≤ n ≤ 8760. Cada consulta
es `d m h`: un día válido de un año no bisiesto, un mes entre `jan feb
mar apr may jun jul aug sep oct nov dec` y una hora entera 0 ≤ h ≤ 23.

## Salida

Para cada consulta, la altura del Sol en grados, entre 0 y 90.

## Evaluación

Los números se comparan con error absoluto o relativo 10⁻⁶.

## Ejemplos

```
56 3
17 nov 12
17 nov 22
7 jul 12
```

```
14.4968100457
0.0000000000
56.4916089122
```

```
-66.57 1
22 jun 12
```

```
0.0000000000
```

En el primer ejemplo la latitud es 56° norte. El 17 de noviembre al
mediodía se obtiene aproximadamente 14.4968100457°; a las 22:00 el Sol
está bajo el horizonte y corresponde cero. El 7 de julio al mediodía se
obtiene aproximadamente 56.4916089122°. El segundo ejemplo usa latitud
sur −66.57°, poco después del solsticio boreal y durante el invierno
local; el producto escalar es negativo y se imprime cero.

## Solución

### Órbita y giro en el mismo sistema

Los argumentos trigonométricos están en radianes. Sea `D` el día del año
desde cero, calculado con las longitudes mensuales y `d−1`. El solsticio
tiene `D₀=171`. Las horas desde el 21 de junio al mediodía y la fase
orbital son `t=24(D−171)+h−12` y `θ=2πt/8760`. La parte horaria es
necesaria: la traslación continúa entre medianoche y mediodía.

Elegimos ejes ecuatoriales inerciales: `z` apunta al polo norte y `x` al
meridiano inicial del observador. El vector unitario desde la Tierra
hacia el Sol es `S=(cos ε cos θ, sin θ, sin ε cos θ)`. Los coeficientes
de `cos θ` y `sin θ` son vectores unitarios perpendiculares en el plano
orbital inclinado. En `θ=0` la componente norte es máxima, como exige el
solsticio de verano boreal.

Un día solar mide el giro respecto de la dirección Tierra–Sol en
movimiento. En una órbita hay una vuelta adicional respecto de los ejes
inerciales: 366 giros durante 365 días solares. Por tanto, la fase del
meridiano es `ψ=2π·366t/8760` módulo una vuelta. La expresión
equivalente usada al calcular es `H=2π(h−12)/24` y `ψ=θ+H`, pues el
término omitido es un número entero de vueltas diarias. Es necesario
conservar la parte orbital de `ψ`; orientar de nuevo el meridiano hacia
el Sol cada fecha describe otro modelo.

Con `φ=lπ/180`, la normal unitaria exterior al plano tangente es
`N=(cos φ cos ψ, cos φ sin ψ, sin φ)`.
Ambos vectores están expresados en los mismos ejes. Su producto es
`u=cos φ cos ε cos ψ cos θ + cos φ sin ψ sin θ + sin φ sin ε cos θ`.

### Por qué la fórmula da el ángulo pedido

El radio de una esfera es perpendicular al plano tangente, así que `N`
apunta al cenit local. El producto de los vectores unitarios `N` y `S`
es el coseno del ángulo entre el cenit y el Sol. Cuando el Sol es
visible, su altura es el ángulo complementario y tiene seno `u`. La
única solución en `[0,π/2]` es `asin(u)`. Si `u≤0`, el Sol está en el
horizonte o por debajo y corresponde cero. En consecuencia
`asin(max(0,u))` produce el resultado solicitado en todos los casos.

El calendario obtiene exactamente las horas transcurridas, la traslación
uniforme determina `S` y la rotación uniforme determina `N`. El
argumento del producto escalar completa la corrección del algoritmo. En
el mediodía inicial, `u=cos(φ−ε)`; por ejemplo, para latitud 23.44° la
altura es 89.999281°, útil para comprobar la proximidad al cenit.

No añadir un día bisiesto ni desplazar el 21 de junio. El origen es
mediodía, no medianoche. Incluir la hora en la fase orbital y conservar
toda la precisión de la inclinación. Distinguir giro inercial y fase
solar diaria: una fórmula de declinación con el meridiano realineado al
Sol pierde la fase prescrita. No usar valor absoluto durante la noche.
Limitar el argumento antes del arcoseno, especialmente cerca del cenit.
Calcular cada fecha desde el mismo origen, sin depender del orden de
consultas.

## Notas por lenguaje

Precalculamos doce desplazamientos mensuales y los coeficientes `cos φ
cos ε`, `cos φ` y `sin φ sin ε`. Cada consulta calcula `θ`, `ψ` y el
producto, limita el valor a `[0,1]` para proteger contra redondeos, toma
el arcoseno y convierte a grados. Se imprimen diez decimales. No se
necesita simular pasos de tiempo ni una biblioteca astronómica.

Cada consulta cuesta `O(1)` y el total `O(n)`. El estado matemático
auxiliar, incluido el calendario fijo, ocupa `O(1)`. C++ y Go emiten las
respuestas mediante buffers; Python y Rust conservan entrada y salida, y
Java acumula la salida, por lo que esos buffers necesitan `O(n)`
memoria. Todos usan doble precisión; Python se ejecuta en CPython 3.12.
Java fija la configuración decimal. Las horas transcurridas se calculan
con enteros, incluso antes del solsticio cuando son negativas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2054_geometry.cpp](2054_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 524 KB |
| [2054_geometry.go](2054_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.046 s | 1524 KB |
| [2054_geometry.java](2054_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.171 s | 6556 KB |
| [2054_geometry.py](2054_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.109 s | 2852 KB |
| [2054_geometry.rs](2054_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.046 s | 668 KB |
