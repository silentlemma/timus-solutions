# 2136. Menos ladrillos para que un rectángulo no baje por una chimenea

[Timus 2136](https://acm.timus.ru/problem.aspx?space=1&num=2136) · dificultad 2330 · two_pointers

Problema original de Nikita Sivukhin, del concurso «Más vale tarde que nunca».

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una chimenea es una cuadrícula de h filas y anchura w. La fila i tiene
lᵢ ladrillos a la izquierda y rᵢ a la derecha, y las casillas libres
entre ellos forman un segmento no vacío. Un rectángulo a × b empieza
encima de la chimenea y se mueve de casilla en casilla, sin solaparse
nunca con un ladrillo, intentando salir por abajo. Añadir el menor
número de ladrillos, manteniendo no vacío el segmento libre de cada
fila, para que no pueda pasar. Los límites son 1 segundo y 256 MB.

## Entrada

h y w, 1 ≤ h ≤ 10⁵, 3 ≤ w ≤ 10⁹, luego a y b, 1 ≤ a ≤ 10⁹,
2 ≤ b ≤ 10⁹, y luego los pares lᵢ, rᵢ con lᵢ, rᵢ ≥ 1 y lᵢ + rᵢ < w.

## Salida

El menor número de ladrillos.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 5
1 2
2 1
1 1
1 1
1 1
2 1
1 1
1 1
```

Salida:

```
1
```

## Solución

Mientras el rectángulo cubre un conjunto fijo de a filas, puede
deslizarse de lado libremente dentro de su parte libre común. Un paso
hacia abajo de las filas i … i + a − 1 a las filas i + 1 … i + a conserva
las columnas, así que esas columnas deben estar libres en las a + 1
filas i … i + a. Con L y R los mayores números de ladrillos a la
izquierda y a la derecha en una ventana así de a + 1 filas, el paso es
posible exactamente cuando L + R + b ≤ w. Las filas por encima y por
debajo de la chimenea están vacías, así que las ventanas cerca de arriba
son más cortas, y el rectángulo pasa exactamente cuando cada ventana
permite su paso.

Para bloquearlo, una ventana debe llegar a L + R ≥ w − b + 1. Añadir
ladrillos a una sola fila sube L o R de uno en uno, y cada fila conserva
una casilla libre porque b ≥ 2, así que la respuesta es
max(0, w − b + 1 − máximo sobre las ventanas de (L + R)). Las ventanas de
a + 1 filas se recorren con dos colas dobles monótonas para los máximos,
en O(h).

En el ejemplo la ventana de las dos primeras filas tiene L + R = 3,
mientras que w − b + 1 = 4, así que un ladrillo más en una de esas filas
cierra el paso.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2136_two_pointers.cpp](2136_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(h) | AC | 0.046 s | 444 KB |
| [2136_two_pointers.go](2136_two_pointers.go) | Go 1.14 x64 | two_pointers | O(h) | AC | 0.031 s | 6324 KB |
| [2136_two_pointers.java](2136_two_pointers.java) | Java 1.8 | two_pointers | O(h) | AC | 0.140 s | 2188 KB |
| [2136_two_pointers.py](2136_two_pointers.py) | PyPy 3.10 x64 | two_pointers | O(h) | AC | 0.250 s | 18588 KB |
| [2136_two_pointers.rs](2136_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(h) | AC | 0.046 s | 3176 KB |
