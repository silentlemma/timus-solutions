# 1952. Sobrevivir a ataques de área alternos

[Timus 1952](https://acm.timus.ru/problem.aspx?space=1&num=1952) · difficulty 8217 · dp

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Denis Dublennykh.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n atacantes y m sanadores, N=n+m. Todos empiezan en (0,0), con salud
máxima H y velocidad v. Cada aura tiene máximo c, crecimiento r al lanzar
magia y descenso f al correr. Su potencia es continua, queda en [0,c] y
sigue activa durante el movimiento. Cada atacante resta su potencia por
segundo a la salud del objetivo. Cada sanador cura a todos los participantes
por segundo, hasta H. Inicialmente las auras atacantes valen cero y las
sanadoras están al máximo.

Al comenzar Storm todos corren en línea recta a su centro y después lanzan
magia. Cada persona recibe D de daño por segundo solo hasta llegar. En
Breath se elige una biyección entre personas y N sitios distintos: cada
persona corre directamente al suyo y después lanza magia, pero recibe D
durante todo Breath, incluso tras llegar. Pasar por otro sitio no permite
lanzar magia. Tail mata instantáneamente a todos; aparece una sola vez,
al final. Nunca hay tres Breath consecutivos. Cada duración permite todos
los desplazamientos posibles. Además, Storm permite a los supervivientes
recuperar salud completa y todas las potencias máximas. Cada D es
estrictamente mayor que la suma de máximos sanadores.

Si alguien llega a salud cero muere todo el grupo. Salud cero del objetivo
no detiene los ataques: hace falta un remate instantáneo con todos vivos
y reunidos en el centro del Storm activo. En la frontera entre ataques
todavía actúa el anterior. Hallar el primer índice que permite rematar.
Límites: 1 segundo, 64 MB.

## Entrada

Primero n,m,k: 1≤n,m≤9, N≤10, 1≤k≤10. Después H,v,G, siendo G la salud
del objetivo: 1≤H,G≤10⁹, 1≤v≤10⁶. Siguen n ternas atacantes y m sanadoras
c,r,f, todos enteros en [1,10⁶]. Cada uno de los k bloques comienza con
el nombre exacto del ataque. Storm tiene D,T y un centro x,y; Breath tiene
D,T y N sitios x,y; Tail no tiene parámetros. 1≤D,T≤10⁶ y
−1000≤x,y≤1000. Se cumplen todas las garantías anteriores. El tiempo de
viaje es la distancia euclídea dividida por v y puede ser irracional.

## Salida

Si no hay victoria, `You are not prepared`. Si la hay, `No useful loot again`
y en la línea siguiente el primer índice de ataque, empezando en 1.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
1 1 2
1 5 10
1 3 2
1 1 1
Storm
7 10
0 0
Tail
```

```
You are not prepared
```

```
1 1 2
1 5 10
1 3 2
1 1 1
Storm
7 11
0 0
Tail
```

```
No useful loot again
1
```

## Solución

Al terminar Storm se restablecen posiciones, salud y potencias. Dividir la
lista en bloques de cero, uno o dos Breath seguidos de Storm; el estado
inicial sirve como frontera virtual. Ignorar un sufijo de Breath sin Storm
antes de Tail. Solo el primer bloque empieza con potencia atacante cero.
Maximizar el daño de cada bloque sobrevivible y acumularlo: el siguiente
estado inicial es independiente gracias a la recuperación completa.

Sea L el mayor tiempo desde los últimos sitios hasta el centro siguiente.
Todos los sitios se ocupan, así que L no depende de la asignación. La última
persona en llegar recibe daño durante los Breath y hasta L. Como D supera
cualquier curación total, su salud disminuye estrictamente. Quienes llegan
antes evitan parte del daño y no tienen menos salud. Basta comprobar
supervivencia estricta en L; después todos están a salvo y pueden rematar
hasta terminar Storm.

Sea B la suma de máximos sanadores. La pérdida inevitable es
ΣBreath (D−B)T+(Dstorm−B)L; restarla de H da el presupuesto K. El coste de
un sanador asignado es la integral de c−power durante los Breath y los
primeros L segundos de Storm. Su suma debe ser estrictamente menor que K.
El peso de un atacante integra su potencia durante todo el bloque, incluido
el Storm completo. Integrar los tramos lineales descendentes y ascendentes,
limitados por cero y c. Calcular directamente el déficit evita restar
integrales de curación enormes casi iguales.

Procesar en orden cada grupo. Con un Breath, dp[S] es el peso óptimo al
asignar las primeras |S| personas a S. Con dos, dp[S,U] guarda los sitios
usados en cada capa. Añadir un sitio libre por capa y el peso de la persona.
Minimizar costes sanadores y maximizar daño atacante por separado. Para
cada máscara o par sanador sobrevivible, usar las máscaras complementarias
atacantes. La recurrencia enumera todas las inyecciones y conserva su
óptimo; los complementos ocupan los sitios restantes sin conflicto. Esto
prueba la factibilidad y el daño máximo. Sin Breath no hay asignación y
la supervivencia se decide comparando radicales directamente. Devolver el
primer Storm cuyo daño máximo acumulado sea ≥G.

### Comparaciones exactas

Un epsilon no distingue la muerte con salud exactamente cero. Para geometría
general, intervalos redondeados hacia fuera encierran viajes, integrales y
errores de asignación. Decidir solo si todo el intervalo prueba la relación;
en otro caso refinar exactamente la asignación restringida correspondiente.
Representar números mediante sumas canónicas Σ q_d√d, con coeficientes
racionales y d libres de cuadrados. Estos radicales son linealmente
independientes sobre Q: cero exacto equivale a todos los coeficientes cero.
Para una suma no nula, raíces cuadradas enteras dan cotas decimales cada
vez más precisas hasta excluir cero. También se resuelven así candidatos
solapados y empates del daño acumulado. No hay tolerancia fija.

Python usa Fraction para viajes racionales e integración exacta, y Surd
para viajes irracionales y las sumas de radicales resultantes. Antes de
construir el tensor exacto, dividir c,r,f de cada aura por su gcd y volver
a multiplicar sus costes por él. Una asignación exacta de una capa usa
emparejamiento. Con dos capas, los tensores idénticos de todos los miembros
también se reducen a un emparejamiento entre los dos conjuntos de sitios;
en otro caso se usa la DP exacta restringida de subconjuntos.

Por bloque con dos Breath, ambas DP ordinarias suman exactamente
N²·C(2N−2,N−1) transiciones: hasta 4 862 000 con N=10. Una capa cuesta
O(N·2ᴺ). La DP ordinaria nativa guarda pares de igual cardinalidad de forma
compacta, O(C(2N,N)) estados, hasta 184 756. Python direcciona O(4ᴺ)
casillas. Para una asignación exacta restringida de q personas, C++ y Java
también usan O(C(2q,q)) estados compactos, mientras Go, Rust y Python
reservan O(4^q) casillas. Los pesos requieren O(N³) tiempo y espacio;
multiplicar por bloques. Las comparaciones ambiguas añaden asignaciones
restringidas y
aritmética de precisión arbitraria: el recuento ordinario no acota por sí
solo su complejidad de bits. El argumento del signo garantiza terminación.

Breath sigue causando daño al llegar; correr no desactiva el aura; curar
afecta a todos. No compartir sitios ni rematar pasando por un centro viejo
durante Breath. Son legales Breath iniciales. Salud de participantes >0,
del objetivo puede ser cero. Potencia atacante inicial cero. La recuperación
completa de Storm es esencial para dividir bloques y también debe cumplirse
en pruebas de estrés. Usar rango suficiente para cuadrados de coordenadas,
velocidades y numeradores racionales. Los viajes racionales aún producen
costes fraccionarios: case_049–case_056 comprueban la frontera estricta de
salud y el umbral de daño al objetivo. No redondear estos costes a enteros
ni suponer que existe una ruta especial de escalado entero.

## Notas por lenguaje

Go y Java usan sus enteros de precisión arbitraria, Python sus enteros y
Fraction, C++ su propia aritmética larga con fracciones, división larga
y raíz cuadrada entera, y Rust sus propios números de dígitos de 32
bits. Java comparte los tensores de auras idénticas y libera de vez en
cuando objetos exactos temporales para mantener el montículo pequeño. El
refinamiento exacto recupera las elecciones mediante enlaces a los
padres en lugar de guardar un número simbólico en cada estado de
subconjunto.

Python decide primero en double con cotas de error garantizadas: una
relajación por emparejamiento y DP de compleción de una capa dan cotas
que resuelven la mayoría de las batallas, y la DP completa y la
aritmética exacta solo se ejecutan cuando las cotas no bastan. Se
ejecuta con PyPy, 0,83 s de 1 s en el juez; una versión anterior que
siempre ejecutaba la DP completa superaba el límite de tiempo en la
prueba 21 del juez. Rust sigue la solución en Go con bucles simples y
pocas funciones genéricas: una versión anterior en Rust agotaba el
tiempo de compilación del juez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1952_dp.cpp](1952_dp.cpp) | G++ 13.2 x64 | dp | O(k N^2 C(2N-2,N-1)) plus exact refinement | AC | 0.156 s | 3100 KB |
| [1952_dp.go](1952_dp.go) | Go 1.14 x64 | dp | O(k N^2 C(2N-2,N-1)) plus exact refinement | AC | 0.078 s | 17616 KB |
| [1952_dp.java](1952_dp.java) | Java 1.8 | dp | O(k N^2 C(2N-2,N-1)) plus exact refinement | AC | 0.312 s | 10864 KB |
| [1952_dp.py](1952_dp.py) | PyPy 3.10 x64 | dp | O(k N^2 C(2N-2,N-1)) plus exact refinement | AC | 0.828 s | 26964 KB |
| [1952_dp.rs](1952_dp.rs) | Rust 1.75 x64 | dp | O(k N^2 C(2N-2,N-1)) plus exact refinement | AC | 0.062 s | 4224 KB |
