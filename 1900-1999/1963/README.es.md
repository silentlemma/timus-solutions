# 1963. Puntos del borde en ejes de reflexión

[Timus 1963](https://acm.timus.ru/problem.aspx?space=1&num=1963) · difficulty 496 · geometry

Original problem from Open Ural FU Personal Contest 2013 | by Alexander Ipatov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado un cuadrilátero simple en orden de borde, contar sus puntos de borde
distintos situados en algún eje de reflexión de la figura completa.
Puede ser cóncavo. Ninguna terna de vértices consecutivos es colineal y
los lados opuestos no se cortan. Límites: 1 segundo, 64 MB.

## Entrada

Cuatro líneas con coordenadas enteras x,y de los vértices en orden
cíclico. El valor absoluto de cada coordenada es como máximo 1000.

## Salida

Un entero: cantidad de puntos distintos del borde sobre ejes de simetría.
La reflexión respecto del eje debe conservar toda la figura.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
0 0
1 2
2 2
2 1
```

```
2
```

```
0 0
2 1
2 2
0 2
```

```
0
```

## Solución

En el primer ejemplo, reflejar en y=x fija (0,0) y (2,2), e intercambia
(1,2) con (2,1). Los dos vértices fijos del único eje dan 2. En el segundo
ejemplo ninguna de las cuatro reflexiones posibles de vértices conserva
el polígono, por lo que se obtiene 0.

Numerar los vértices p_i de 0 a 3. Una reflexión envía esquinas a esquinas
e invierte el orden del borde. Su permutación tiene la forma
i→(s−i) mod 4 para s=0,…,3: solo hay cuatro candidatos.

Si s es par, dos vértices opuestos quedan fijos y definen el eje. Si es
impar, se intercambian dos pares de vértices adyacentes y el eje pasa
por los puntos medios de esos lados opuestos. Guardar sus puntos A,B en
coordenadas dobles: un vértice es 2p y un punto medio es p+q. Así las
posiciones semienteras siguen siendo exactas. Omitir D=B−A si es cero.

Para cada par p,q de la permutación propuesta, comprobar

(p+q−A)×D=0 y (p−q)·D=0.

El producto vectorial indica que el punto medio está sobre el eje y el
escalar que el segmento es perpendicular. Juntos expresan exactamente
que p se refleja en q, también si p=q. Aceptar el candidato únicamente
si pasan los cuatro pares, usando enteros.

Toda simetría real satisface estos requisitos. A la inversa, la
permutación de orden cíclico invertido envía cada arista a su arista
correspondiente: conserva borde y región encerrada. La prueba también
vale para cuadriláteros cóncavos.

Un eje válido corta el borde precisamente en sus dos puntos definitorios:
vértices opuestos para s par o puntos medios para s impar. Otro cruce
obligaría a una arista a cortar una arista reflejada distinta fuera de
un vértice común, imposible en un polígono simple. Tampoco puede quedar
un lado entero sobre el eje, porque estas permutaciones no fijan dos
vértices consecutivos.

Insertar ambos puntos dobles de cada eje válido en un conjunto y devolver
el tamaño de la unión. Se cuentan puntos distintos sin suponer que las
intersecciones de ejes diferentes son distintas.

Tiempo `O(1)` y espacio `O(1)`: cuatro candidatos, cuatro pares por cada
uno y como máximo ocho puntos almacenados.

No asumir convexidad ni usar solo longitudes de lados o diagonales.
También importan los ejes por puntos medios de lados opuestos; sus
coordenadas pueden ser semienteras. Mantener el orden del borde: deben
preservarse las aristas, además del conjunto de vértices. No hacen falta
flotantes ni epsilon; las cuatro permutaciones inversas completan la lista.

## Notas por lenguaje

C++, Go 1.14, Java 8 y Rust 1.75 usan enteros de 64 bits para productos.
Python 3.12 usa enteros exactos. C++/Go/Python/Rust guardan puntos dobles
en conjuntos; Java busca duplicados en una lista de hasta ocho puntos.
No hacen falta recursión ni bibliotecas geométricas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1963_geometry.cpp](1963_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 396 KB |
| [1963_geometry.go](1963_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1100 KB |
| [1963_geometry.java](1963_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1676 KB |
| [1963_geometry.py](1963_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 712 KB |
| [1963_geometry.rs](1963_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 232 KB |
