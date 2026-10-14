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
const TOURS: &[(usize, usize, &str)] = &[
    (6, 6, concat!("516516177626345432322514745366748838",)),
    (6, 7, concat!("126211617888687268332123613455535887774734",)),
    (
        6,
        8,
        concat!("156525625787878632685264127421145455883877487738",),
    ),
    (
        6,
        9,
        concat!("525156562757868786141163114342262714356735766348744348",),
    ),
    (
        6,
        10,
        concat!("556115556257672287163424233814322854521275386366367487338348",),
    ),
    (
        6,
        11,
        concat!("125226211667788756851812825437134352432148325565585858834747478784",),
    ),
    (7, 6, concat!("116666158528336332126534147312556438337788",)),
    (
        7,
        8,
        concat!("11661266128715123333873452624362143688245563556837774734",),
    ),
    (
        7,
        10,
        concat!("5516556512727728771234861362421271874312342717441255648367663433883888",),
    ),
    (
        8,
        6,
        concat!("126622128728734724522744732166128234355534778734",),
    ),
    (
        8,
        7,
        concat!("12622661788818121283432113381717834146362855655343377734",),
    ),
    (
        8,
        8,
        concat!("5555252277676782341516143461671431235782347475123566686634843888",),
    ),
    (
        8,
        9,
        concat!("156621166128768118325484734558514386176784638115862826756575534378747734",),
    ),
    (
        8,
        10,
        concat!(
            "555652261252775177883414455718146168622454458828421243721838378566556477",
            "88778734",
        ),
    ),
    (
        8,
        11,
        concat!(
            "116662165221282781178233737743114526745667445427488466211556814536356553",
            "6554637834743834",
        ),
    ),
    (
        9,
        6,
        concat!("115512778712328368375416145866743166322536345566748834",),
    ),
    (
        9,
        8,
        concat!("526552625776871814421814376757325221862834336814121754123453673677884388",),
    ),
    (
        9,
        10,
        concat!(
            "521155651277721177121447381442346256131232743336123475463762115476451234",
            "634666663388843888",
        ),
    ),
    (
        10,
        6,
        concat!("156562128782323124724264143538136836522836123184558534777734",),
    ),
    (
        10,
        7,
        concat!("1165666178881852127343275786147156414184647278636121582454855347778734",),
    ),
    (
        10,
        8,
        concat!(
            "116665661287151233336234126743821435166417326418325482341275223254854534",
            "77387744",
        ),
    ),
    (
        10,
        9,
        concat!(
            "121656562728868782522322244141474584171774636315184232128757744128487518",
            "558535636774747838",
        ),
    ),
    (
        10,
        10,
        concat!(
            "555115126272672887183481637114174111473651442722227743332224346238641814",
            "7852623474656655363788477834",
        ),
    ),
    (
        10,
        11,
        concat!(
            "156615161265287888281832161667434137351141361467476413652742763564322481",
            "58332128548285385558538556677743774434",
        ),
    ),
    (
        11,
        6,
        concat!("525616727218144732741518124114328348755412744164513512336636348848",),
    ),
    (
        11,
        8,
        concat!(
            "556555221767871234551414377326121342683614848512328564843255651214333312",
            "5463466637388388",
        ),
    ),
    (
        11,
        10,
        concat!(
            "115652561672817812183283864332113571213814383628145214766724124444362814",
            "83166638126883872455555355847774777734",
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
