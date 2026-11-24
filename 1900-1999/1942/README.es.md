# 1942. El desplazamiento más cercano para la mayor clase

[Timus 1942](https://acm.timus.ru/problem.aspx?space=1&num=1942) · difficulty 646 · geometry

Original problem from Open Ural FU Personal Contest 2012 | by Vitaliy Belokobilskiy, Sergey Madzhuga.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados n puntos del plano, trasladar una vez el origen sin girar los ejes.
Un punto cuenta cuando sus dos nuevas coordenadas son enteras. Maximizar
la cantidad y, entre esos desplazamientos, minimizar la distancia euclídea.
Los puntos coincidentes son registros distintos y cuentan por separado.
Límites: 1 segundo, 64 MB.

## Entrada

n con 1≤n≤50000, seguido de n pares de coordenadas reales, cada una de
valor absoluto≤100 y hasta tres decimales. Se permiten signos y partes
decimales más cortas.

## Salida

La cantidad máxima como entero y la distancia mínima, con error absoluto
no mayor que 10⁻⁵.

## Evaluación

Un comprobador verifica el número de puntos de forma exacta y la
longitud del desplazamiento con error absoluto 10⁻⁵.

## Ejemplos

```
3
0.500 0.200
0.500 0.500
-0.500 0.200
```

```
2 0.53852
```

```
2
1.000 1.000
1.000 1.000
```

```
2 0.00000
```

## Solución

Sea S=1000. Omitir la parte entera y analizar solo la fracción con su
signo como milésimas enteras X,Y, rellenando con ceros. Esto conserva
el residuo sin convertir una cantidad ilimitada de ceros iniciales;
evitar truncar un producto en flotante.
Dos puntos pueden hacerse enteros juntos exactamente cuando ambas
diferencias de coordenadas son enteras. Por tanto, comparten residuos
normalizados rx=X mod S y ry=Y mod S en 0..999.

Contar cada par en un vector de S² celdas, índice rx·S+ry. Todo traslado
útil pertenece a una clase y hace enteros precisamente sus puntos; la
mayor frecuencia es la cantidad máxima.

Los orígenes de una clase son (rx/S+i,ry/S+j), i,j enteros. Minimizar
cada componente cuadrada de forma independiente: dx=min(rx,S−rx),
dy=min(ry,S−ry), en milésimas. Definir q=dx²+dy². Entre clases de máxima
frecuencia elegir el menor q; solo al final calcular sqrt(q)/S.

Las frecuencias crecen monótonamente. Tras cada incremento, mayor
cantidad gana y, en empate, menor q. Cada clase que alcanza un empate
se compara, conservando por inducción el mejor resultado procesado.
La partición prueba la cantidad óptima y las elecciones independientes
de enteros cercanos prueban la distancia mínima. En semienteros hay
dos traslados cercanos, pero su distancia cuadrada coincide.

Tiempo O(S²+L), S=1000 y L la longitud de entrada; espacio auxiliar O(S²).
Incluyendo puntos, entrada y tokens retenidos, el espacio total es O(S²+L).
Con tokens de longitud acotada se obtiene O(S²+n).
Cantidad≤50000, milésimas fraccionarias con signo dentro de ±999,
q≤500000: bastan 32 bits con signo. La tabla ocupa unos 4 MB.

No girar ejes, fusionar registros coincidentes ni usar el valor absoluto
de la parte fraccionaria negativa. La distancia es secundaria a la
cantidad. La parte entera no cambia la clase; residuos cercanos a 1
admiten pequeños traslados negativos. No hace falta epsilon para agrupar
o comparar q.
El test 34 escribe el cero con 4301 dígitos: los ceros iniciales son
válidos, pero convertir toda la cadena supera el límite predeterminado
de int en Python. Eliminar también los ceros iniciales antes de convertir n.
El test 35 usa n=0008: leer la cantidad en decimal, sin inferir base octal.

## Notas por lenguaje

C++, Go y Java normalizan restos negativos; Python con módulo positivo
y Rust rem_euclid ya dan ese rango. Los analizadores conservan residuos exactos incluso
para fracciones negativas con parte entera cero. Python y Go usan
frecuencias compactas de 32 bits; Java fija la configuración regional.
Se imprimen nueve decimales, error de redondeo≤5·10⁻¹⁰. Solo la raíz final
usa flotantes; pertenencia de clase y desempates son exactos.

## Soluciones optimizadas

La versión en C++ codifica cada par de residuos en un entero. Ordena las claves y cuenta los tramos iguales. Si dos frecuencias coinciden, compara las distancias al cuadrado y solo calcula la raíz para la respuesta. El tiempo es O(L + N log N), con L como longitud de entrada y N puntos. El espacio adicional es O(N). Las métricas corresponden al envío 11316985.

La versión para Java 1.8 también codifica cada par con un entero y cuenta los grupos tras ordenarlos. El envío 11317110 tardó 0.109 s y usó 804 KB frente a 0.125 s y 6036 KB de la base.

La versión para Python 3.12 x64 también codifica cada par con un entero y cuenta los grupos tras ordenarlos. El envío 11317108 tardó 0.203 s y usó 3384 KB frente a 0.281 s y 11584 KB de la base.

La versión para Rust 1.75 x64 también codifica cada par con un entero y cuenta los grupos tras ordenarlos. El envío 11317104 tardó 0.015 s y usó 412 KB frente a 0.031 s y 6016 KB de la base.

La versión para Go 1.14 x64 también codifica cada par con un entero y cuenta los grupos tras ordenarlos. El envío 11317099 tardó 0.031 s y usó 1260 KB frente a 0.078 s y 8908 KB de la base.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322162 · Go 1.14 x64 №11322163 · Java 1.8 №11322164 · Python 3.12 x64 №11322165 · Rust 1.75 x64 №11322166.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1942_geometry.cpp](1942_geometry.cpp) | G++ 13.2 x64 | geometry | O(S^2+L) | AC | 0.031 s | 4788 KB | 11322162 |
| [1942_geometry.go](1942_geometry.go) | Go 1.14 x64 | geometry | O(S^2+L) | AC | 0.078 s | 8908 KB | 11322163 |
| [1942_geometry.java](1942_geometry.java) | Java 1.8 | geometry | O(S^2+L) | AC | 0.125 s | 6036 KB | 11322164 |
| [1942_geometry.py](1942_geometry.py) | Python 3.12 x64 | geometry | O(S^2+L) | AC | 0.281 s | 11584 KB | 11322165 |
| [1942_geometry.rs](1942_geometry.rs) | Rust 1.75 x64 | geometry | O(S^2+L) | AC | 0.031 s | 6016 KB | 11322166 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1942_geometry_optimized.cpp](1942_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(L + N log N) | AC | 0.015 s | 344 KB | 11316985 |
| [1942_geometry_optimized.go](1942_geometry_optimized.go) | Go 1.14 x64 | geometry | O(L + N log N) | AC | 0.031 s | 1260 KB | 11317099 |
| [1942_geometry_optimized.rs](1942_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(L + N log N) | AC | 0.015 s | 412 KB | 11317104 |
| [1942_geometry_optimized.py](1942_geometry_optimized.py) | Python 3.12 x64 | geometry | O(L + N log N) | AC | 0.203 s | 3384 KB | 11317108 |
| [1942_geometry_optimized.java](1942_geometry_optimized.java) | Java 1.8 | geometry | O(L + N log N) | AC | 0.109 s | 804 KB | 11317110 |
