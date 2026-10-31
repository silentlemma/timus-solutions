use std::io::{self, Read, Write};

const CHAR_COUNT: usize = 128;
const DEGREE: usize = 3;
const EDGE_COUNT: usize = 12;
// the cube: A B C D around the bottom face, E F G H above them
const EDGES: [&[u8]; EDGE_COUNT] = [
    b"AB", b"BC", b"CD", b"DA", b"EF", b"FG", b"GH", b"HE", b"AE", b"BF", b"CG", b"DH",
];
const CELLS: &[u8] = b"ABCDEFGH";
// the cube is bipartite; every operation changes one chamber of each side
const EVEN: &[u8] = b"ACFH";

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // ascii labels index fixed arrays; every cube vertex has three neighbors.
    let mut count = [0i32; CHAR_COUNT];
    let mut balance = 0;
    for (&c, value) in CELLS.iter().zip(input.split_ascii_whitespace()) {
        count[c as usize] = value.parse().unwrap();
        balance += if EVEN.contains(&c) {
            count[c as usize]
        } else {
            -count[c as usize]
        };
    }
    let mut out = io::BufWriter::new(io::stdout().lock());
    if balance != 0 {
        writeln!(out, "IMPOSSIBLE").unwrap();
        return;
    }
    let mut near = [[0u8; DEGREE]; CHAR_COUNT];
    let mut degree = [0; CHAR_COUNT];
    for edge in EDGES {
        let (a, b) = (edge[0] as usize, edge[1] as usize);
        near[a][degree[a]] = edge[1];
        degree[a] += 1;
        near[b][degree[b]] = edge[0];
        degree[b] += 1;
    }
    // streaming avoids a growing output string; each operation has four bytes.
    let mut emit = |a: u8, b: u8, sign: u8| {
        out.write_all(&[a, b, sign, b'\n']).unwrap();
    };
    // annihilate along every edge as long as both ends hold duons; afterwards
    // every edge has an empty end
    for edge in EDGES {
        let (a, b) = (edge[0] as usize, edge[1] as usize);
        let k = count[a].min(count[b]);
        for _ in 0..k {
            emit(edge[0], edge[1], b'-');
        }
        count[a] -= k;
        count[b] -= k;
    }
    // what is left can only sit at two opposite corners u and w, in equal
    // numbers; a pair made on the middle edge of a path u x y w removes both
    for &u in EVEN {
        let left = count[u as usize];
        if left == 0 {
            continue;
        }
        let w = *CELLS
            .iter()
            .find(|&&c| count[c as usize] > 0 && !EVEN.contains(&c))
            .unwrap();
        let x = near[u as usize][0];
        let y = *near[x as usize]
            .iter()
            .find(|c| near[w as usize].contains(c))
            .unwrap();
        for _ in 0..left {
            emit(x, y, b'+');
            emit(u, x, b'-');
            emit(y, w, b'-');
        }
        count[w as usize] -= left;
        count[u as usize] = 0;
    }
}
