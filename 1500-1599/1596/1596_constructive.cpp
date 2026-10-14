#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const int DIRECTIONS = 8;
const int MOVES[DIRECTIONS][2] = {{2, 1}, {2, -1}, {-2, 1}, {-2, -1},
                                  {1, 2}, {1, -2}, {-1, 2}, {-1, -2}};
const int SMALLEST = 6, LARGEST = 11; // blocks have sides from 6 to 11
const int USUAL = 8;                  // the side of most blocks

struct Base {
    int rows, cols;
    const char *dirs;
};

// a closed tour of each block, one direction per cell, row by row; each
// also moves between (1, C-2) and (3, C-1) and between (R-2, 1) and (R-1, 3)
// printed by 1596_constructive_table.py
const Base TOURS[] = {
    {6, 6, "121666728218124734145382556534373784"},
    {6, 7, "121262677812181247734343252275665343477884"},
    {6, 8, "526116625778871814175764322113123538683874847788"},
    {6, 9, "556121612572787718346824712126833382545576586733874884"},
    {6, 10, "522226166672727866181448564134146574133255655765343773874784"},
    {6, 11, "126262522221781871171815437844614326734363325536556653674743877884"},
    {7, 6, "511516721212343332544312544114376666348838"},
    {7, 8, "15666566518711163254443457511382146828345465556837388734"},
    {7, 10, "5526552612756772771834351477165473576222572413758234646665663488488844"},
    {8, 6, "116566178212326434355312543134513512336636348848"},
    {8, 7, "15611165787818356773253425627458412517331234667663488488"},
    {8, 8, "5556551252777712341446161468524214754442322485123553674674844888"},
    {8, 9, "515526516775277816348117432356157512144558412342333312356468666348488888"},
    {8, 10, "11156615127782771712317356438234552533125458348466546871451254664666363478387888"},
    {8, 11,
     "156155655161287867781232352432636734722455821471832234251318771412356654"
     "4676834843834788"},
    {9, 6, "151512778712357382744562742612348118322212743436748848"},
    {9, 8, "552215127777271234816388376523125475241234553712313423123466846634888888"},
    {9, 10,
     "121166226677886585185286326434351311433211576573281435736718328436521435"
     "566856367487738338"},
    {10, 6, "522516777812147836745562521644345418146728145282356538338784"},
    {10, 7, "5525512726771234284487415612523382835357121433168544181235666383484788"},
    {10, 8, "52511612777877185486571872451312375742221473681234546614322442123437663674887888"},
    {10, 9,
     "556521612577787718346676762327526382347621512727463714345583882155263512"
     "346336666338843388"},
    {10, 10,
     "555615166212671887183484137714175685876235555214187234545414148146236211"
     "8488383235658565683783874784"},
    {10, 11,
     "126215666161787822781812435637736333261658821233111754454147878416522855"
     "78436543351164225566446653434733877784"},
    {11, 6, "511516771812547332347562342116346818545782744562573512346666348848"},
    {11, 8,
     "552125127277271634381382542183427427111632736814345552321414463274234812"
     "3565676834848788"},
    {11, 10,
     "552125556272777817123428216644548784451251218332323161471412147318416434"
     "17333712121548381234856767667388448488"},
};

// cuts a side into pieces from 6 to 11 long, all even if it is even
vector<int> sides(int length) {
    vector<int> out;
    while (length >= USUAL + SMALLEST) {
        out.push_back(USUAL);
        length -= USUAL;
    }
    if (length > LARGEST) {
        out.push_back(SMALLEST);
        length -= SMALLEST;
    }
    out.push_back(length);
    return out;
}

vector<int> one, two; // the two neighbours of every cell on the cycle

void swapEdge(int u, int old, int now) {
    if (one[u] == old)
        one[u] = now;
    else
        two[u] = now;
}

// drops the moves a-b and c-d of two cycles and adds a-c and b-d
void join(int a, int b, int c, int d) {
    swapEdge(a, b, c);
    swapEdge(b, a, d);
    swapEdge(c, d, a);
    swapEdge(d, c, b);
}

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    if (n * m % 2 == 1) {
        printf("No solution\n");
        return 0;
    }
    one.assign(n * m, 0);
    two.assign(n * m, 0);
    vector<int> rows = sides(n), cols = sides(m);
    int top = 0;
    for (int h : rows) {
        int left = 0;
        for (int w : cols) {
            const char *tour = nullptr;
            for (const Base &b : TOURS)
                if (b.rows == h && b.cols == w)
                    tour = b.dirs;
            for (int i = 0; i < h; i++)
                for (int j = 0; j < w; j++) {
                    const int *mv = MOVES[tour[i * w + j] - '1'];
                    int u = (top + i) * m + left + j;
                    int v = u + mv[0] * m + mv[1];
                    one[u] = v; // the next cell of u
                    two[v] = u; // the cell before v
                }
            left += w;
        }
        top += h;
    }
    top = 0;
    for (int h : rows) {
        int left = cols[0];
        for (size_t k = 1; k < cols.size(); k++) {
            // the left block's move (1, C-2)-(3, C-1) and the right block's
            // corner move (0, 0)-(2, 1) give way to two moves across
            int a = (top + 1) * m + left - 2, c = top * m + left;
            join(a, a + 2 * m + 1, c, c + 2 * m + 1);
            left += cols[k];
        }
        top += h;
    }
    top = rows[0];
    for (size_t k = 1; k < rows.size(); k++) {
        // the top block's (R-2, 1)-(R-1, 3) and the bottom block's (0, 0)-(1, 2)
        int a = (top - 2) * m + 1, c = top * m;
        join(a, a + m + 2, c, c + m + 2);
        top += rows[k];
    }
    // walk the cycle from the top left cell and write each move
    vector<char> out(2 * n * m);
    int prev = -1, cur = 0;
    for (int k = 0; k < n * m; k++) {
        int next = one[cur] != prev ? one[cur] : two[cur];
        int dr = next / m - cur / m, dc = next % m - cur % m;
        for (int d = 0; d < DIRECTIONS; d++)
            if (MOVES[d][0] == dr && MOVES[d][1] == dc)
                out[2 * cur] = '1' + d;
        out[2 * cur + 1] = cur % m == m - 1 ? '\n' : ' ';
        prev = cur;
        cur = next;
    }
    fwrite(out.data(), 1, out.size(), stdout);
}
