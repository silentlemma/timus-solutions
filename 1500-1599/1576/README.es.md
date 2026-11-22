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

N1 y C1, luego N2, T y C2, luego N3, todos enteros de 1 a 1000, y luego
K (1 ≤ K ≤ 1000) y las K duraciones como mm:ss, donde 0 ≤ mm, ss ≤ 59.

## Salida

Tres líneas con el formato de los ejemplos.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

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

## Soluciones optimizadas

`1576_implementation_optimized.java`. Java lee cada llamada mm:ss como dos enteros sin dividir cadenas. Las llamadas de hasta seis segundos son gratuitas; las demás pagan mm+(ss>0) minutos. Solo conserva la suma. Las tres fórmulas tarifarias siguen iguales y usan int: hasta 1000 llamadas de 60 minutos facturados y tarifas de hasta 1000 limitan la factura máxima a 60001000. Búferes reutilizables de entrada y salida de 1024 bytes emiten las etiquetas, espacios y números exactos sin concatenación StringBuilder. Tiempo O(K), espacio auxiliar O(1). Los 3600 pares de minutos y segundos se verificaron mediante redondeo desde segundos.

Accepted exacto Java 1.8 #11327448: 0.078 s / 356 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/54, memoria 1/54. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Ambas métricas son primeras; cumple también la meta propia del lenguaje, sin asterisco. El registro optimizado documentado antes #11304530 era 0.125 s / 376 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1576_implementation_optimized.java`: 0.078 s / 356 KB; base didáctica conservada `1576_implementation.java`: 0.109 s / 2244 KB.

`1576_implementation_optimized.rs`. Conserva llamadas gratis de hasta seis segundos y redondeo por llamada facturada. Lee k mm:ss en flujo: el lector entero consume dos puntos, sin buscar ni dividir cadenas. Acumula solo minutos cobrados y conserva tres fórmulas, etiquetas y espacios de alineación. O(k) tiempo, O(1) espacio; mismas reglas de facturación.

Frente a `1576_implementation.rs`: tiempo 0.015 s → 0.015 s; memoria 232 KB → 52 KB.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1576_implementation_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1576_implementation.cpp](1576_implementation.cpp) | G++ 13.2 x64 | implementation | O(K) | AC | 0.015 s | 132 KB | 11287847 |
| [1576_implementation.go](1576_implementation.go) | Go 1.14 x64 | implementation | O(K) | AC | 0.015 s | 1168 KB | 11287851 |
| [1576_implementation.java](1576_implementation.java) | Java 1.8 | implementation | O(K) | AC | 0.109 s | 2244 KB | 11287858 |
| [1576_implementation.py](1576_implementation.py) | Python 3.12 x64 | implementation | O(K) | AC | 0.078 s | 508 KB | 11287853 |
| [1576_implementation.rs](1576_implementation.rs) | Rust 1.75 x64 | implementation | O(K) | AC | 0.015 s | 232 KB | 11287860 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1576_implementation_optimized.java](1576_implementation_optimized.java) | Java 1.8 | implementation | O(K) time; O(1) auxiliary space | AC | 0.078 s | 356 KB | 11327448 |
| [1576_implementation_optimized.rs](1576_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(k) time; O(1) space | AC | 0.015 s | 52 KB | 11325528 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
