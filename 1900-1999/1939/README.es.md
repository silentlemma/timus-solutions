# 1939. El límite entre pasar y frenar

[Timus 1939](https://acm.timus.ru/problem.aspx?space=1&num=1939) · difficulty 841 · math

Original problem from Open Ural FU Championship 2012 | by Denis Dublennykh (prepared by Egor Shchelkonogov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un vehículo de longitud l y altura h se acerca a velocidad constante v.
La reja tiene altura inicial H y puede empezar a bajar a velocidad x
en cualquier instante. Al advertir el cierre se puede soltar la tracción
y frenar con desaceleración a hasta detenerse, o continuar. Inicialmente
hay distancia suficiente para parar antes del portón si se frena enseguida.
Decidir si existe un inicio de cierre que haga inevitable la colisión
con cualquier decisión. Todo contacto es fatal. Límites: 1 segundo, 64 MB.

## Entrada

Primero l,h,H con h<H; después v,x,a. Los seis son enteros positivos
de hasta 1000. Longitudes en centímetros, v y x en cm/s y a en cm/s².
No se proporciona la distancia actual al portón.

## Salida

Crash si algún inicio de cierre fuerza una colisión; en otro caso Safe.
Respetar exactamente estas mayúsculas y minúsculas.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
1 1 1000
1 1 1000
```

```
Safe
```

```
1000 1 2
1000 1 1
```

```
Crash
```

## Solución

Sea d la distancia del frente al portón cuando comienza el cierre.
La reja llega a altura h en T=(H−h)/x. Frenar inmediatamente da
distancia de parada S=v²/(2a).

Parar es seguro solo si d>S. En igualdad el frente queda en el plano
de la puerta y acabará tocando la reja. Pasar es seguro solo si
d+l<vT: la parte trasera debe salir antes de T; igualdad también toca.

Retrasar la suelta no mejora ninguna cota. Un retraso δ≥0 aumenta
la distancia final a S+vδ y toda trayectoria permitida tiene velocidad
como máximo v. Nadie frena antes que la parada inmediata ni pasa antes
que el movimiento constante. Si ambos extremos fallan, ningún retraso salva.

Si S+l<vT, cualquier d queda cubierto: frenar con d>S, continuar con
d≤S. Si no, elegir d=S: no se para estrictamente antes del portón ni
sale la trasera estrictamente antes de T. Ese instante es alcanzable
porque la distancia inicial supera S. Hay choque inevitable exactamente
cuando S+l≥vT. Un único instante peligroso aislado también cuenta.

Multiplicar por el valor positivo 2ax da la condición entera exacta

x·(v²+2al) ≥ 2av·(H−h).

Imprimir Crash cuando se cumple, incluida igualdad. No hacen falta
divisiones ni épsilon. La longitud del vehículo y la pérdida H−h importan.

Tiempo y espacio O(1), con un número fijo de operaciones.

Usar ≥ para Crash por el contacto en ambas fronteras. No olvidar la
parte trasera, sustituir H−h por H, confundir tiempo y distancia de
frenado ni probar solo una posición actual desconocida. Un épsilon
puede borrar diferencias significativas de una unidad entre productos grandes.

## Notas por lenguaje

El lado izquierdo alcanza 3 000 000 000 y excede enteros de 32 bits;
el derecho no supera 1 998 000 000. Todos los operandos son de 64 bits
antes de multiplicar: long long en C++, int64 en Go, long en Java,
i64 en Rust. Python usa enteros arbitrarios. Se imprime una palabra y LF.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1939_math.cpp](1939_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 380 KB |
| [1939_math.go](1939_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1092 KB |
| [1939_math.java](1939_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 404 KB |
| [1939_math.py](1939_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 408 KB |
| [1939_math.rs](1939_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 224 KB |
