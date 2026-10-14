use std::io::{self, Read};

const DIM: usize = 3; // x, y, z, then vx, vy, vz
const COORDS: usize = 2 * DIM;

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s.split_ascii_whitespace();
    let n: usize = match it.next() {
        Some(w) => w.parse().unwrap(),
        None => return,
    };
    let d: f64 = it.next().unwrap().parse().unwrap();
    let obj: Vec<Vec<f64>> = (0..n)
        .map(|_| {
            (0..COORDS)
                .map(|_| it.next().unwrap().parse().unwrap())
                .collect()
        })
        .collect();
    let mut best = f64::INFINITY;
    let mut pair = None;
    for i in 0..n {
        for j in i + 1..n {
            let (p, q) = (&obj[i], &obj[j]);
            // |p + v t| = d for the relative position p and velocity v:
            // (v.v) t^2 + 2 (p.v) t + (p.p - d^2) = 0
            let (mut a, mut b, mut c) = (0.0, 0.0, -d * d);
            for k in 0..DIM {
                let (dp, dv) = (q[k] - p[k], q[DIM + k] - p[DIM + k]);
                a += dv * dv;
                b += dp * dv;
                c += dp * dp;
            }
            if a == 0.0 {
                continue;
            }
            let disc = b * b - a * c;
            if disc < 0.0 {
                continue;
            }
            // the earlier root; the pair starts apart, so a negative one
            // means they are moving away
            let t = (-b - disc.sqrt()) / a;
            if t >= 0.0 && t < best {
                best = t;
                pair = Some((i + 1, j + 1));
            }
        }
    }
    match pair {
        None => println!("OK"),
        Some((a, b)) => println!("ALARM!\n{:.3} {} {}", best, a, b),
    }
}
