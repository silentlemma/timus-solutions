# 1576. Tarifas telefónicas

[Timus 1576](https://acm.timus.ru/problem.aspx?space=1&num=1576) · dificultad 147 · implementation

Problema original del folclore, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres tarifas: básica, una cuota N1 más C1 por minuto; combinada, una
cuota N2 que incluye T minutos, más C2 por cada minuto por encima de T;
ilimitada, una cuota N3. Las llamadas de como mucho 6 segundos son
gratis, y las más largas se redondean hacia arriba a minutos enteros.
Dadas hasta 1000 llamadas como mm:ss, hay que imprimir la factura del
mes con cada tarifa.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N1 y C1, luego N2, T y C2, luego N3, y luego K y las K duraciones.

## Salida

Tres líneas con el formato de los ejemplos.

## Ejemplos

### Ejemplo 1

Entrada:

```
135 1
220 10 1
300
5
00:05
00:10
09:59
07:00
01:01
```

Salida:

```
Basic:     155
Combined:  230
Unlimited: 300
```

### Ejemplo 2

Entrada:

```
10 2
100 1 1
1000
1
03:00
```

Salida:

```
Basic:     16
Combined:  102
Unlimited: 1000
```

## Solución

Se suman los minutos cobrados: una llamada de s segundos no añade nada
si s ≤ 6 y ⌈s / 60⌉ en otro caso. Con M minutos las facturas son
N1 + C1·M, N2 + C2·max(0, M − T) y N3, todas por debajo de 7·10⁷.
`O(K)`.

Detalles a tener en cuenta:

- una llamada de exactamente 6 segundos es gratis, una de 7 segundos
  cuesta un minuto entero, y una de exactamente un minuto cuesta uno
  (prueba 03);
- la tarifa combinada no cobra nada extra mientras los minutos no pasen
  de T, así que el exceso nunca es negativo;
- las etiquetas se alinean al mismo ancho: `Basic:` con cinco espacios,
  `Combined:` con dos y `Unlimited:` con uno.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1576_implementation.cpp](1576_implementation.cpp) | G++ 13.2 x64 | implementation | O(K) | AC | 0.015 s | 132 KB |
| [1576_implementation.go](1576_implementation.go) | Go 1.14 x64 | implementation | O(K) | AC | 0.015 s | 1168 KB |
| [1576_implementation.java](1576_implementation.java) | Java 1.8 | implementation | O(K) | AC | 0.109 s | 2244 KB |
| [1576_implementation.py](1576_implementation.py) | Python 3.12 x64 | implementation | O(K) | AC | 0.078 s | 508 KB |
| [1576_implementation.rs](1576_implementation.rs) | Rust 1.75 x64 | implementation | O(K) | AC | 0.015 s | 232 KB |
