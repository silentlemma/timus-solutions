use std::io::{self, Read};

const ROLLS: usize = 70;
const DIRS: usize = 6;
const TURN: f64 = 60.0; // degrees between neighbouring directions
const OFF: i32 = 80; // coordinates stay within ROLLS of the origin
const SIZE: usize = 2 * OFF as usize + 1;
// the six directions of a hexagonal lattice, as integer combinations of
// the first two of them
const UA: [i32; DIRS] = [1, 0, -1, -1, 0, 1];
const UB: [i32; DIRS] = [0, 1, 1, 0, -1, -1];
const CLASSES: [f64; 2] = [0.0, 90.0]; // starting edges at 0 and 180, or at 90 and 270 degrees

fn index(a: i32, b: i32, d: usize) -> usize {
    (((a + OFF) as usize) * SIZE + (b + OFF) as usize) * DIRS + d
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (tx, ty) = (v[0], v[1]);
    // a jump through the base in half steps: (1 + sqrt 3) / 2 = 1/2 + sin 60
    let side = (1.0 + 2.0 * TURN.to_radians().sin()) / 2.0;
    let mut best = tx.hypot(ty); // no rolls at all
    for start in CLASSES {
        let w: Vec<(f64, f64)> = (0..DIRS)
            .map(|k| {
                let angle = (start + TURN * k as f64).to_radians();
                (angle.cos(), angle.sin())
            })
            .collect();
        // a state is a triangle lying on the table: twice its apex position
        // (in steps of the base jump) and the direction from the apex to the
        // base edge; it costs one roll to reach from the start
        let mut cost = vec![ROLLS; SIZE * SIZE * DIRS];
        let mut buckets: Vec<Vec<(i32, i32, usize)>> = vec![Vec::new(); ROLLS + 1];
        for u in [0, DIRS / 2] {
            let s = (UA[u], UB[u], (u + DIRS / 2) % DIRS);
            cost[index(s.0, s.1, s.2)] = 1;
            buckets[1].push(s);
        }
        for c in 1..ROLLS {
            let mut i = 0;
            while i < buckets[c].len() {
                let (a, b, d) = buckets[c][i];
                i += 1;
                if cost[index(a, b, d)] != c {
                    continue;
                }
                // roll onto the base: its centre is half a step beyond the apex
                let (ea, eb) = ((a + UA[d]) as f64, (b + UB[d]) as f64);
                let x = side * (ea * w[0].0 + eb * w[1].0);
                let y = side * (ea * w[0].1 + eb * w[1].1);
                best = best.min((x - tx).hypot(y - ty));
                // a side face is one roll away, the far side of the base two
                let next = [
                    (a, b, (d + 1) % DIRS, 1),
                    (a, b, (d + DIRS - 1) % DIRS, 1),
                    (a + 2 * UA[d], b + 2 * UB[d], (d + DIRS / 2) % DIRS, 2),
                ];
                for (na, nb, nd, add) in next {
                    let nc = c + add;
                    if nc < ROLLS && cost[index(na, nb, nd)] > nc {
                        cost[index(na, nb, nd)] = nc;
                        buckets[nc].push((na, nb, nd));
                    }
                }
            }
        }
    }
    println!("{:.4}", best);
}
