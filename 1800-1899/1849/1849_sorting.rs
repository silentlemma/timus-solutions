use std::io::{self, Read};

const SPAN: i64 = 10000; // coordinates lie in [-SPAN, SPAN]
const REACH: i64 = 10; // direction parts lie in [-REACH, REACH]
const WIDTH: i64 = 2 * SPAN + 1;
const TURN: i64 = 2 * REACH + 1;

fn gcd(a: i64, b: i64) -> i64 {
    let (mut a, mut b) = (a.abs(), b.abs());
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let rabbits_at: Vec<(i64, i64)> =
        (0..n).map(|_| (it.next().unwrap(), it.next().unwrap())).collect();
    let q = it.next().unwrap() as usize;
    let mut next = || it.next().unwrap();
    let (mut x, mut y, mut vx, mut vy) = (next(), next(), next(), next());
    let (ax, bx, ay, by) = (next(), next(), next(), next());
    let (avx, bvx, avy, bvy) = (next(), next(), next(), next());
    // every direction is filed under its primitive vector
    let mut primitive: Vec<(i64, i64)> = Vec::new();
    let mut code = vec![0usize; (TURN * TURN) as usize];
    for dx in -REACH..=REACH {
        for dy in -REACH..=REACH {
            let g = gcd(dx, dy);
            if g == 0 {
                continue;
            }
            let key = (dx / g, dy / g);
            let k = match primitive.iter().position(|&p| p == key) {
                Some(k) => k,
                None => {
                    primitive.push(key);
                    primitive.len() - 1
                }
            };
            code[((dx + REACH) * TURN + dy + REACH) as usize] = k;
        }
    }
    let kinds = primitive.len();
    let mut xs = vec![0i64; q];
    let mut ys = vec![0i64; q];
    let mut kind = vec![0usize; q];
    let mut start = vec![0usize; kinds + 1];
    for i in 0..q {
        xs[i] = x;
        ys[i] = y;
        kind[i] = code[((vx + REACH) * TURN + vy + REACH) as usize];
        start[kind[i] + 1] += 1;
        x = (ax * (x + SPAN) + bx) % WIDTH - SPAN;
        y = (ay * (y + SPAN) + by) % WIDTH - SPAN;
        vx = (avx * (vx + REACH) + bvx) % TURN - REACH;
        vy = (avy * (vy + REACH) + bvy) % TURN - REACH;
    }
    // the shots in order of their direction, by counting
    for k in 0..kinds {
        start[k + 1] += start[k];
    }
    let mut shots = vec![0usize; q];
    let mut fill = start[..kinds].to_vec();
    for i in 0..q {
        shots[fill[kind[i]]] = i;
        fill[kind[i]] += 1;
    }
    let (mut best, mut best_count) = (0usize, -1i64);
    let mut rabbits = vec![(0i64, 0i64); n];
    for k in 0..kinds {
        if start[k] == start[k + 1] {
            continue;
        }
        let (dx, dy) = primitive[k];
        // rabbits by the line along (dx, dy) and then by the place on it
        for (r, &(rx, ry)) in rabbits.iter_mut().zip(&rabbits_at) {
            *r = (rx * dy - ry * dx, rx * dx + ry * dy);
        }
        rabbits.sort_unstable();
        for &i in &shots[start[k]..start[k + 1]] {
            let line = xs[i] * dy - ys[i] * dx;
            let place = xs[i] * dx + ys[i] * dy;
            let from = rabbits.partition_point(|&r| r < (line, place));
            let to = rabbits.partition_point(|&r| r.0 <= line);
            let got = (to - from) as i64;
            // a later shot wins a tie
            if got > best_count || (got == best_count && i > best) {
                best = i;
                best_count = got;
            }
        }
    }
    println!("{} {}", best + 1, best_count);
}
