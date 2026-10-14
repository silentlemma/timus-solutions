use std::io::{self, Read, Write};

const MOVES: [(i64, i64); 8] = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
];
const SMALLEST: usize = 6; // blocks have sides from 6 to 11
const LARGEST: usize = 11;
const USUAL: usize = 8; // the side of most blocks

// a closed tour of each block, one direction per cell, row by row; each
// also moves between (1, C-2) and (3, C-1) and between (R-2, 1) and (R-1, 3)
// printed by 1596_constructive_table.py
const TOURS: &[(usize, usize, &str)] = &[
    (6, 6, concat!("121666728218124734145382556534373784",)),
    (6, 7, concat!("121262677812181247734343252275665343477884",)),
    (
        6,
        8,
        concat!("526116625778871814175764322113123538683874847788",),
    ),
    (
        6,
        9,
        concat!("556121612572787718346824712126833382545576586733874884",),
    ),
    (
        6,
        10,
        concat!("522226166672727866181448564134146574133255655765343773874784",),
    ),
    (
        6,
        11,
        concat!("126262522221781871171815437844614326734363325536556653674743877884",),
    ),
    (7, 6, concat!("511516721212343332544312544114376666348838",)),
    (
        7,
        8,
        concat!("15666566518711163254443457511382146828345465556837388734",),
    ),
    (
        7,
        10,
        concat!("5526552612756772771834351477165473576222572413758234646665663488488844",),
    ),
    (
        8,
        6,
        concat!("116566178212326434355312543134513512336636348848",),
    ),
    (
        8,
        7,
        concat!("15611165787818356773253425627458412517331234667663488488",),
    ),
    (
        8,
        8,
        concat!("5556551252777712341446161468524214754442322485123553674674844888",),
    ),
    (
        8,
        9,
        concat!("515526516775277816348117432356157512144558412342333312356468666348488888",),
    ),
    (
        8,
        10,
        concat!(
            "111566151277827717123173564382345525331254583484665468714512546646663634",
            "78387888",
        ),
    ),
    (
        8,
        11,
        concat!(
            "156155655161287867781232352432636734722455821471832234251318771412356654",
            "4676834843834788",
        ),
    ),
    (
        9,
        6,
        concat!("151512778712357382744562742612348118322212743436748848",),
    ),
    (
        9,
        8,
        concat!("552215127777271234816388376523125475241234553712313423123466846634888888",),
    ),
    (
        9,
        10,
        concat!(
            "121166226677886585185286326434351311433211576573281435736718328436521435",
            "566856367487738338",
        ),
    ),
    (
        10,
        6,
        concat!("522516777812147836745562521644345418146728145282356538338784",),
    ),
    (
        10,
        7,
        concat!("5525512726771234284487415612523382835357121433168544181235666383484788",),
    ),
    (
        10,
        8,
        concat!(
            "525116127778771854865718724513123757422214736812345466143224421234376636",
            "74887888",
        ),
    ),
    (
        10,
        9,
        concat!(
            "556521612577787718346676762327526382347621512727463714345583882155263512",
            "346336666338843388",
        ),
    ),
    (
        10,
        10,
        concat!(
            "555615166212671887183484137714175685876235555214187234545414148146236211",
            "8488383235658565683783874784",
        ),
    ),
    (
        10,
        11,
        concat!(
            "126215666161787822781812435637736333261658821233111754454147878416522855",
            "78436543351164225566446653434733877784",
        ),
    ),
    (
        11,
        6,
        concat!("511516771812547332347562342116346818545782744562573512346666348848",),
    ),
    (
        11,
        8,
        concat!(
            "552125127277271634381382542183427427111632736814345552321414463274234812",
            "3565676834848788",
        ),
    ),
    (
        11,
        10,
        concat!(
            "552125556272777817123428216644548784451251218332323161471412147318416434",
            "17333712121548381234856767667388448488",
        ),
    ),
];

/// Cuts a side into pieces from 6 to 11 long, all even if it is even.
fn sides(mut length: usize) -> Vec<usize> {
    let mut out = Vec::new();
    while length >= USUAL + SMALLEST {
        out.push(USUAL);
        length -= USUAL;
    }
    if length > LARGEST {
        out.push(SMALLEST);
        length -= SMALLEST;
    }
    out.push(length);
    out
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<usize> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    if v.len() < 2 {
        return;
    }
    let (n, m) = (v[0], v[1]);
    if n * m % 2 == 1 {
        println!("No solution");
        return;
    }
    // the tour as an undirected cycle: the two neighbours of every cell
    let mut one = vec![0usize; n * m];
    let mut two = vec![0usize; n * m];
    let (rows, cols) = (sides(n), sides(m));
    let mut top = 0;
    for &h in &rows {
        let mut left = 0;
        for &w in &cols {
            let tour = TOURS
                .iter()
                .find(|t| t.0 == h && t.1 == w)
                .unwrap()
                .2
                .as_bytes();
            for i in 0..h {
                for j in 0..w {
                    let (dr, dc) = MOVES[(tour[i * w + j] - b'1') as usize];
                    let u = (top + i) * m + left + j;
                    let v = (u as i64 + dr * m as i64 + dc) as usize;
                    one[u] = v; // the next cell of u
                    two[v] = u; // the cell before v
                }
            }
            left += w;
        }
        top += h;
    }
    // drops the moves a-b and c-d of two cycles and adds a-c and b-d
    let mut join = |a: usize, b: usize, c: usize, d: usize| {
        for &(u, old, now) in &[(a, b, c), (b, a, d), (c, d, a), (d, c, b)] {
            if one[u] == old {
                one[u] = now;
            } else {
                two[u] = now;
            }
        }
    };
    top = 0;
    for &h in &rows {
        let mut left = cols[0];
        for &w in &cols[1..] {
            // the left block's move (1, C-2)-(3, C-1) and the right block's
            // corner move (0, 0)-(2, 1) give way to two moves across
            let (a, c) = ((top + 1) * m + left - 2, top * m + left);
            join(a, a + 2 * m + 1, c, c + 2 * m + 1);
            left += w;
        }
        top += h;
    }
    top = rows[0];
    for &h in &rows[1..] {
        // the top block's (R-2, 1)-(R-1, 3) and the bottom block's (0, 0)-(1, 2)
        let (a, c) = ((top - 2) * m + 1, top * m);
        join(a, a + m + 2, c, c + m + 2);
        top += h;
    }
    // walk the cycle from the top left cell and write each move
    let mut out = vec![b' '; 2 * n * m];
    let (mut prev, mut cur) = (usize::MAX, 0);
    for _ in 0..n * m {
        let next = if one[cur] != prev { one[cur] } else { two[cur] };
        let dr = (next / m) as i64 - (cur / m) as i64;
        let dc = (next % m) as i64 - (cur % m) as i64;
        let d = MOVES.iter().position(|&mv| mv == (dr, dc)).unwrap();
        out[2 * cur] = b'1' + d as u8;
        if cur % m == m - 1 {
            out[2 * cur + 1] = b'\n';
        }
        prev = cur;
        cur = next;
    }
    io::stdout().write_all(&out).unwrap();
}
