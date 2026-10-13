use std::io::{self, Read, Write};

const ADD: i64 = 1; // record kinds; any other kind ends the input
const ASK: i64 = 2;

/// A 3D Fenwick tree, indices from 1.
struct Fenwick {
    n: usize,
    side: usize,
    tree: Vec<i64>,
}

impl Fenwick {
    fn add(&mut self, x: usize, y: usize, z: usize, k: i64) {
        let mut i = x;
        while i <= self.n {
            let mut j = y;
            while j <= self.n {
                let base = (i * self.side + j) * self.side;
                let mut w = z;
                while w <= self.n {
                    self.tree[base + w] += k;
                    w += w & w.wrapping_neg();
                }
                j += j & j.wrapping_neg();
            }
            i += i & i.wrapping_neg();
        }
    }

    fn prefix(&self, x: usize, y: usize, z: usize) -> i64 {
        let mut total = 0;
        let mut i = x;
        while i > 0 {
            let mut j = y;
            while j > 0 {
                let base = (i * self.side + j) * self.side;
                let mut w = z;
                while w > 0 {
                    total += self.tree[base + w];
                    w -= w & w.wrapping_neg();
                }
                j -= j & j.wrapping_neg();
            }
            i -= i & i.wrapping_neg();
        }
        total
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let side = n + 1;
    let mut f = Fenwick {
        n,
        side,
        tree: vec![0; side * side * side],
    };
    let mut out = String::new();
    loop {
        let kind = it.next().unwrap();
        let mut next = || it.next().unwrap() as usize + 1;
        if kind == ADD {
            let (x, y, z) = (next(), next(), next());
            let k = it.next().unwrap();
            f.add(x, y, z, k);
        } else if kind == ASK {
            let (x1, y1, z1) = (next() - 1, next() - 1, next() - 1);
            let (x2, y2, z2) = (next(), next(), next());
            // inclusion and exclusion over the eight corners of the box
            let total = f.prefix(x2, y2, z2)
                - f.prefix(x1, y2, z2)
                - f.prefix(x2, y1, z2)
                - f.prefix(x2, y2, z1)
                + f.prefix(x1, y1, z2)
                + f.prefix(x1, y2, z1)
                + f.prefix(x2, y1, z1)
                - f.prefix(x1, y1, z1);
            out.push_str(&total.to_string());
            out.push('\n');
        } else {
            break;
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
