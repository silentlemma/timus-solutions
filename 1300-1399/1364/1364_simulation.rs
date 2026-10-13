use std::io::{self, Read, Write};

// east, south, west, north: turning right moves one step along this list
const STEPS: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let mut next = || it.next().unwrap();
    let (n, m) = (next(), next());
    let (rt, ct, rl, cl, t) = (next(), next(), next(), next(), next());
    // dig the spiral up to the treasure, remembering the order of the graves,
    // with a frame of dug cells around the cemetery standing for the wall
    let (h, w) = (n as usize + 2, m as usize + 2);
    let mut seen = vec![vec![false; w]; h];
    for r in 0..h {
        seen[r][0] = true;
        seen[r][w - 1] = true;
    }
    for c in 0..w {
        seen[0][c] = true;
        seen[h - 1][c] = true;
    }
    let mut path = vec![(1, 1)];
    seen[1][1] = true;
    let (mut r, mut c, mut d) = (1i32, 1i32, 0usize);
    while (r, c) != (rt, ct) {
        let (nr, nc) = (r + STEPS[d].0, c + STEPS[d].1);
        if seen[nr as usize][nc as usize] {
            d = (d + 1) % STEPS.len();
            continue;
        }
        r = nr;
        c = nc;
        seen[r as usize][c as usize] = true;
        path.push((r, c));
    }
    // Lara runs along the tunnel, at most t graves either way
    let here = path.iter().position(|&p| p == (rl, cl)).unwrap() as i32;
    let lo = (here - t).max(0) as usize;
    let hi = (here + t).min(path.len() as i32 - 1) as usize;
    let mut out = String::new();
    for &(pr, pc) in &path[lo..=hi] {
        out.push_str(&format!("{} {}\n", pr, pc));
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
