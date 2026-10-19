# 1942. El desplazamiento más cercano para la mayor clase

[Timus 1942](https://acm.timus.ru/problem.aspx?space=1&num=1942) · difficulty 647 · geometry

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

Sea S=1000. Analizar cadenas decimales como milésimas enteras X,Y,
rellenando la fracción con ceros; evitar truncar un producto en flotante.
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

Tiempo O(S²+n), S=1000, y almacenamiento auxiliar O(S²). Los programas
completos conservan O(n) puntos o entrada, por lo que su espacio total
es O(S²+n). Cantidad≤50000, coordenadas escaladas dentro de ±100000,
q≤500000: bastan 32 bits con signo. La tabla ocupa unos 4 MB.

No girar ejes, fusionar registros coincidentes ni usar el valor absoluto
de la parte fraccionaria negativa. La distancia es secundaria a la
cantidad. La parte entera no cambia la clase; residuos cercanos a 1
admiten pequeños traslados negativos. No hace falta epsilon para agrupar
o comparar q.

## Notas por lenguaje

C++, Go y Java normalizan restos negativos; Python con módulo positivo
y Rust rem_euclid ya dan ese rango. Los analizadores son exactos incluso
para fracciones negativas con parte entera cero. Python y Go usan
frecuencias compactas de 32 bits; Java fija la configuración regional.
Se imprimen nueve decimales, error de redondeo≤5·10⁻¹⁰. Solo la raíz final
usa flotantes; pertenencia de clase y desempates son exactos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1942_geometry.cpp](1942_geometry.cpp) | G++ 13.2 x64 | geometry | O(S^2+n) | AC | 0.015 s | 4808 KB |
| [1942_geometry.go](1942_geometry.go) | Go 1.14 x64 | geometry | O(S^2+n) | AC | 0.093 s | 8956 KB |
| [1942_geometry.java](1942_geometry.java) | Java 1.8 | geometry | O(S^2+n) | AC | 0.156 s | 6104 KB |
| [1942_geometry.py](1942_geometry.py) | Python 3.12 x64 | geometry | O(S^2+n) | AC | 0.281 s | 11476 KB |
| [1942_geometry.rs](1942_geometry.rs) | Rust 1.75 x64 | geometry | O(S^2+n) | AC | 0.046 s | 6012 KB |
