use std::io::{self, Read};

const CEILING: i64 = 0;
const TURNIP: i64 = -1;
const FREE: i64 = -2;
const ONE: usize = 0; // the turnip's weight of 1
const MASS: usize = 1; // the unknown mass
const FIELDS: usize = 4; // type, two rope ends and the axle
const PORTS: usize = FIELDS - 1;

fn rope(i: usize) -> usize {
    2 * i + 2 // tension in the rope over block i
}

fn axle(i: usize) -> usize {
    rope(i) + 1 // tension in the rope at the axle of block i
}

// every tension is a power of two times the tension at the root of its
// group: value(x) = 2^shift[x] * value(root)
struct Groups {
    parent: Vec<usize>,
    shift: Vec<i32>,
    zero: Vec<bool>, // the whole group must have no tension
}

impl Groups {
    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] == x {
            return x;
        }
        let up = self.parent[x];
        let root = self.find(up);
        self.shift[x] += self.shift[up];
        self.parent[x] = root;
        root
    }

    // value(x) = 2^k * value(y)
    fn tie(&mut self, x: usize, y: usize, k: i32) {
        let (rx, ry) = (self.find(x), self.find(y));
        if rx == ry {
            if self.shift[x] != k + self.shift[y] {
                self.zero[rx] = true;
            }
            return;
        }
        self.parent[rx] = ry;
        self.shift[rx] = k + self.shift[y] - self.shift[x];
        self.zero[ry] = self.zero[ry] || self.zero[rx];
    }
}

// the two rope ends and the axle, with the way they leave the block; a
// first-type block hangs its rope ends down
fn ports(i: usize, block: &[i64]) -> [(usize, i64, bool); PORTS] {
    let down = block[0] == 1;
    [
        (rope(i), block[1], down),
        (rope(i), block[2], down),
        (axle(i), block[PORTS], !down),
    ]
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let data: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = data[0] as usize;
    let blocks: Vec<&[i64]> = data[1..].chunks(FIELDS).take(n).collect();
    let size = 2 * n + 2;
    let mut g = Groups {
        parent: (0..size).collect(),
        shift: vec![0; size],
        zero: vec![false; size],
    };
    for i in 0..n {
        g.tie(axle(i), rope(i), 1); // the axle holds both ends of the rope
        for (node, target, down) in ports(i, blocks[i]) {
            if target == TURNIP {
                g.tie(node, ONE, 0);
            } else if target == FREE {
                g.tie(node, MASS, 0);
            } else if target != CEILING {
                // the other end leaves block target the opposite way
                let j = target as usize - 1;
                if let Some(&(other, _, _)) = ports(j, blocks[j])
                    .iter()
                    .find(|&&(_, back, other_down)| back == i as i64 + 1 && other_down != down)
                {
                    g.tie(node, other, 0);
                }
            }
        }
    }
    let (one, mass) = (g.find(ONE), g.find(MASS));
    if g.zero[one] {
        println!("No solution");
    } else if one == mass {
        println!("{:.4}", 2f64.powi(g.shift[MASS] - g.shift[ONE]));
    } else if g.zero[mass] {
        println!("{:.4}", 0.0);
    } else {
        println!("Any");
    }
}
