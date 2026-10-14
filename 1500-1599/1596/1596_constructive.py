import sys
from array import array

MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
SMALLEST = 6  # blocks have sides from 6 to 11
LARGEST = 11
USUAL = 8  # the side of most blocks
# a closed tour of each block, one direction per cell, row by row; each
# also moves between (1, C-2) and (3, C-1) and between (R-2, 1) and (R-1, 3)
TOURS = {
    (6, 6): "516516177626345432322514745366748838",
    (6, 7): "126211617888687268332123613455535887774734",
    (6, 8): "156525625787878632685264127421145455883877487738",
    (6, 9): "525156562757868786141163114342262714356735766348744348",
    (6, 10): "556115556257672287163424233814322854521275386366367487338348",
    (6, 11): "125226211667788756851812825437134352432148325565585858834747478784",
    (7, 6): "116666158528336332126534147312556438337788",
    (7, 8): "11661266128715123333873452624362143688245563556837774734",
    (7, 10): "5516556512727728771234861362421271874312342717441255648367663433883888",
    (8, 6): "126622128728734724522744732166128234355534778734",
    (8, 7): "12622661788818121283432113381717834146362855655343377734",
    (8, 8): "5555252277676782341516143461671431235782347475123566686634843888",
    (8, 9): "156621166128768118325484734558514386176784638115862826756575534378747734",
    (8, 10): ("55565226125277517788341445571814616862245445882842124372183837856655647788778734"),
    (8, 11): (
        "1166621652212827811782337377431145267456674454274884662115568145363565536554637834743834"
    ),
    (9, 6): "115512778712328368375416145866743166322536345566748834",
    (9, 8): "526552625776871814421814376757325221862834336814121754123453673677884388",
    (9, 10): (
        "521155651277721177121447381442346256131232743336123475463762115476451234634666663388843888"
    ),
    (10, 6): "156562128782323124724264143538136836522836123184558534777734",
    (10, 7): "1165666178881852127343275786147156414184647278636121582454855347778734",
    (10, 8): ("11666566128715123333623412674382143516641732641832548234127522325485453477387744"),
    (10, 9): (
        "121656562728868782522322244141474584171774636315184232128757744128487518558535636774747838"
    ),
    (10, 10): (
        "555115126272672887183481637114174111473651442722227743332224346238641814"
        "7852623474656655363788477834"
    ),
    (10, 11): (
        "156615161265287888281832161667434137351141361467476413652742763564322481"
        "58332128548285385558538556677743774434"
    ),
    (11, 6): "525616727218144732741518124114328348755412744164513512336636348848",
    (11, 8): (
        "5565552217678712345514143773261213426836148485123285648432556512143333125463466637388388"
    ),
    (11, 10): (
        "115652561672817812183283864332113571213814383628145214766724124444362814"
        "83166638126883872455555355847774777734"
    ),
}


def sides(length):
    """Cuts a side into pieces from 6 to 11 long, all even if it is even."""
    out = []
    while length >= USUAL + SMALLEST:
        out.append(USUAL)
        length -= USUAL
    if length > LARGEST:
        out.append(SMALLEST)
        length -= SMALLEST
    out.append(length)
    return out


def main():
    n, m = (int(x) for x in sys.stdin.read().split())
    if n * m % 2:
        print("No solution")
        return
    # the tour as an undirected cycle: the two neighbours of every cell
    one = array("i", [0]) * (n * m)  # a million ints in lists would not fit
    two = array("i", [0]) * (n * m)
    rows, cols = sides(n), sides(m)
    top = 0
    for h in rows:
        left = 0
        for w in cols:
            tour = TOURS[h, w]
            for i in range(h):
                for j in range(w):
                    dr, dc = MOVES[int(tour[i * w + j]) - 1]
                    u = (top + i) * m + left + j
                    v = u + dr * m + dc
                    one[u] = v  # the next cell of u
                    two[v] = u  # the cell before v
            left += w
        top += h

    def swap(u, old, new):
        if one[u] == old:
            one[u] = new
        else:
            two[u] = new

    def join(a, b, c, d):
        """Drops the moves a-b and c-d of two cycles and adds a-c and b-d."""
        swap(a, b, c)
        swap(b, a, d)
        swap(c, d, a)
        swap(d, c, b)

    top = 0
    for h in rows:
        left = cols[0]
        for w in cols[1:]:
            # the left block's move (1, C-2)-(3, C-1) and the right block's
            # corner move (0, 0)-(2, 1) give way to two moves across
            a = (top + 1) * m + left - 2
            c = top * m + left
            join(a, a + 2 * m + 1, c, c + 2 * m + 1)
            left += w
        top += h
    top = rows[0]
    for h in rows[1:]:
        # the top block's (R-2, 1)-(R-1, 3) and the bottom block's (0, 0)-(1, 2)
        a = (top - 2) * m + 1
        c = top * m
        join(a, a + m + 2, c, c + m + 2)
        top += h
    # walk the cycle from the top left cell and write each move
    digit = {dr * m + dc: ord(str(k + 1)) for k, (dr, dc) in enumerate(MOVES)}
    out = bytearray(b"1" * (n * m))
    prev, cur = -1, 0
    for _ in range(n * m):
        nxt = one[cur] if one[cur] != prev else two[cur]
        out[cur] = digit[nxt - cur]
        prev, cur = cur, nxt
    # the digits at even places, spaces and line ends between them
    text = bytearray(2 * n * m)
    text[0::2] = out
    text[1::2] = (b" " * (m - 1) + b"\n") * n
    sys.stdout.buffer.write(text)


main()
