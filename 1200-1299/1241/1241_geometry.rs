use std::io::{self, Read};

// the four small triangles of a unit square, cut by both its diagonals
const EAST: usize = 1;
const NORTH: usize = 2;
const WEST: usize = 3;
const PARTS: usize = 4;
// outward directions of a triangle's edges, counterclockwise from +x
const RIGHT: u32 = 1 << 0;
const UP_RIGHT: u32 = 1 << 1;
const UP: u32 = 1 << 2;
const UP_LEFT: u32 = 1 << 3;
const LEFT: u32 = 1 << 4;
const DOWN_LEFT: u32 = 1 << 5;
const DOWN: u32 = 1 << 6;
const DOWN_RIGHT: u32 = 1 << 7;
const TRIANGLE: u32 = 3;
const HEADER: usize = 3;
const CUT: usize = 4;

struct Pieces {
    parent: Vec<usize>,
    out: Vec<u32>,
}

impl Pieces {
    fn find(&mut self, mut a: usize) -> usize {
        while self.parent[a] != a {
            self.parent[a] = self.parent[self.parent[a]];
            a = self.parent[a];
        }
        a
    }

    // joins two small triangles, or records their outward directions when a
    // cut separates them
    fn side(&mut self, a: usize, da: u32, b: usize, db: u32, cut: bool) {
        if cut {
            self.out[a] |= da;
            self.out[b] |= db;
        } else {
            let (ra, rb) = (self.find(a), self.find(b));
            self.parent[ra] = rb;
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (m, n) = (v[0] as usize, v[1] as usize);
    // a cut runs from border to border, so it is a whole line of one of the
    // four kinds: x = c, y = c, x - y = c or x + y = c
    let (mut vert, mut hor) = (vec![false; m + 1], vec![false; n + 1]);
    let (mut diff, mut sum) = (vec![false; m + n + 1], vec![false; m + n + 1]);
    for c in v[HEADER..].chunks(CUT) {
        let [x1, y1, x2, y2] = [c[0], c[1], c[2], c[CUT - 1]];
        if x1 == x2 {
            vert[x1 as usize] = true;
        } else if y1 == y2 {
            hor[y1 as usize] = true;
        } else if x2 - x1 == y2 - y1 {
            diff[(x1 - y1 + n as i64) as usize] = true;
        } else {
            sum[(x1 + y1) as usize] = true;
        }
    }
    let size = m * n * PARTS;
    let mut p = Pieces {
        parent: (0..size).collect(),
        out: vec![0; size],
    };
    for i in 0..m {
        for j in 0..n {
            let s = (i * n + j) * PARTS;
            let (e, no, w) = (s + EAST, s + NORTH, s + WEST);
            let d = i + n - j;
            p.side(s, UP_RIGHT, e, DOWN_LEFT, sum[i + j + 1]);
            p.side(s, UP_LEFT, w, DOWN_RIGHT, diff[d]);
            p.side(e, UP_LEFT, no, DOWN_RIGHT, diff[d]);
            p.side(no, DOWN_LEFT, w, UP_RIGHT, sum[i + j + 1]);
            if j == 0 {
                p.out[s] |= DOWN;
            } else {
                p.side(s, DOWN, s - PARTS + NORTH, UP, hor[j]);
            }
            if i == 0 {
                p.out[w] |= LEFT;
            } else {
                p.side(w, LEFT, s - n * PARTS + EAST, RIGHT, vert[i]);
            }
            if j == n - 1 {
                p.out[no] |= UP;
            }
            if i == m - 1 {
                p.out[e] |= RIGHT;
            }
        }
    }
    // every piece is convex with sides in these 8 directions, one side per
    // direction, so a piece is a triangle when its edges face 3 directions
    let mut faces = vec![0u32; size];
    for a in 0..size {
        let r = p.find(a);
        faces[r] |= p.out[a];
    }
    let count = (0..size)
        .filter(|&a| p.find(a) == a && faces[a].count_ones() == TRIANGLE)
        .count();
    println!("{}", count);
}
