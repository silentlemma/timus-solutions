# 1970. Unir fotografías giradas y solapadas

[Timus 1970](https://acm.timus.ru/problem.aspx?space=1&num=1970) · difficulty 1254 · backtracking

Problema original del Concurso Individual Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una matriz de colores 10×10 fue fotografiada en nueve piezas 4×4. Antes
de girarlas y mezclarlas, sus esquinas superiores izquierdas ocupaban
todos los pares de {0,3,6}. Las fotos vecinas comparten una fila o columna
completa. Cada foto puede girarse por múltiplos de 90 grados, sin reflejos.
Reconstruir cualquier matriz compatible usando cada foto exactamente una
vez. Existe solución. Límites: 1 segundo, 64 MB.

## Entrada

Nueve matrices 4×4 con enteros de color entre 0 y 99 inclusive. Una línea
vacía separa matrices; los demás espacios no importan. Cantidad y tamaños
son fijos.

## Salida

Diez filas de diez colores separados por espacios. Se acepta cualquier
matriz cuyos nueve recortes indicados correspondan a las fotos giradas.

## Evaluación

Un comprobador recorta las nueve piezas de la matriz impresa y las
empareja con las fotos de entrada admitiendo giros, cada foto una vez;
se acepta cualquier matriz válida.

## Ejemplos

```
1 1 9 9
1 9 1 1
9 1 1 1
9 1 1 9

9 1 1 9
9 1 1 1
9 1 1 1
9 1 1 9

9 1 1 9
9 1 1 1
1 9 1 1
1 1 9 9

9 1 1 9
1 1 1 1
1 1 1 1
9 1 1 9

9 1 1 9
1 1 1 9
1 1 9 1
9 9 1 1

9 1 1 9
1 1 1 9
1 1 1 9
9 1 1 9

9 9 1 1
1 1 9 1
1 1 1 9
9 1 1 9

9 9 9 9
1 1 1 1
1 1 1 1
9 1 1 9

9 1 1 9
1 9 9 1
1 1 1 1
9 9 9 9
```

```
1 1 9 9 9 9 9 9 1 1
1 9 1 1 1 1 1 1 9 1
9 1 1 1 1 1 1 1 1 9
9 1 1 9 1 1 9 1 1 9
9 1 1 1 1 1 1 1 1 9
9 1 1 1 1 1 1 1 1 9
9 1 1 9 1 1 9 1 1 9
9 1 1 1 9 9 1 1 1 9
1 9 1 1 1 1 1 1 9 1
1 1 9 9 9 9 9 9 1 1
```

## Solución

Precalcular los cuatro giros de cada foto. Un estado contiene identidad
y orientación; conservar solo una copia de orientaciones iguales de una
foto, pero mantener fotos distintas como recursos distintos. Guardar los
bordes superior e inferior de izquierda a derecha, y los laterales de
arriba abajo. Dos estados vecinos son compatibles si sus bordes comunes
de cuatro colores son iguales; no invertir otra vez el borde.

Las nueve posiciones forman una cuadrícula 3×3, inicialmente con todos
los estados conservados. Elegir recursivamente la posición vacía con menos
candidatos; desempatar por más vecinos. Probar cada estado, eliminar todas
las orientaciones de su foto de las demás posiciones e intersectar los
dominios vecinos con las máscaras precalculadas de compatibilidad. Si un
dominio vacío no tiene candidatos, descartar la rama. Copiar nueve máscaras
por nivel permite deshacer los cambios fácilmente.

El resultado completo puede girarse globalmente. Por ello la primera foto
puede conservar su orientación de entrada, en cualquier posición. Solo se
elimina simetría global, sin obligarla a estar en una esquina o en el centro.
Como hay hasta 36 estados, basta una máscara de 64 bits.

### Corrección

Cada estado es un giro permitido. Eliminar la máscara completa de su foto
impide reutilizarla. Las intersecciones imponen exactamente las igualdades
con vecinos ya colocados, sin quitar completaciones válidas. La heurística
solo cambia el orden. Toda solución puede girarse para que la primera foto
tenga orientación cero, y giros idénticos son indistinguibles; por tanto
estas reducciones preservan alguna solución.

En una asignación completa coinciden todos los bordes vecinos. Cuando se
encuentran cuatro fotos, sus esquinas coinciden transitivamente a través
de los bordes, sin condición diagonal adicional. Los recortes 4×4 con
desplazamientos 0,3,6 cubren todo el tablero 10×10. Copiar sus celdas produce
una matriz consistente con cada foto una vez. La búsqueda exhaustiva y
la existencia garantizada aseguran encontrarla.

Para m fotos de lado s, una cota conservadora es
`O(ms² + (4m)²s + m!·4^m·m²)` de tiempo y `O(m²+ms²)` de memoria, incluidos los
dominios copiados en la recursión. Aquí m=9, s=4; la propagación reduce
mucho las ramas. Para tamaños variables sigue siendo búsqueda exponencial.
El término `O(ms²)` incluye leer, girar, comparar orientaciones duplicadas
y copiar los píxeles de las fotos a la salida.

En el ejemplo, las filas 0…3 y columnas 0…3 de salida son exactamente
la primera foto. Las filas 3…6 y columnas 0…3 son la segunda, compartiendo
la fila `9 1 1 9`. Los otros siete recortes utilizan una vez cada foto
restante; la unión da el patrón 10×10 mostrado.

El paso es tres, no cuatro: hay solapamiento. No se permiten reflejos.
Comparar los cuatro colores del borde en orden coherente. No reutilizar
una foto aunque sea idéntica a otra. El giro global fija una orientación,
no una posición. Usar máscaras de 64 bits para 36 estados. Deshacer también
el arreglo de posiciones: copiar dominios no restaura ese arreglo.

## Notas por lenguaje

Python usa enteros arbitrarios y bit_count. C++, Go 1.14, Java 8 y Rust
1.75 usan máscaras de 64 bits y operaciones de conteo de bits y ceros
finales. Java crea un Solver nuevo por entrada. La profundidad máxima es nueve.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1970_backtracking.cpp](1970_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(m*s^2+(4*m)^2*s+m!*4^m*m^2) | AC | 0.015 s | 400 KB |
| [1970_backtracking.go](1970_backtracking.go) | Go 1.14 x64 | backtracking | O(m*s^2+(4*m)^2*s+m!*4^m*m^2) | AC | 0.031 s | 1120 KB |
| [1970_backtracking.java](1970_backtracking.java) | Java 1.8 | backtracking | O(m*s^2+(4*m)^2*s+m!*4^m*m^2) | AC | 0.140 s | 1824 KB |
| [1970_backtracking.py](1970_backtracking.py) | Python 3.12 x64 | backtracking | O(m*s^2+(4*m)^2*s+m!*4^m*m^2) | AC | 0.078 s | 1044 KB |
| [1970_backtracking.rs](1970_backtracking.rs) | Rust 1.75 x64 | backtracking | O(m*s^2+(4*m)^2*s+m!*4^m*m^2) | AC | 0.015 s | 236 KB |
