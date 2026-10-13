use std::io::{self, Read};

// east, south, west, north: turning right moves one step along this list
const STEPS: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let mut next = || it.next().unwrap();
    let (n, m) = (next(), next());
    let (r1, c1, r2, c2) = (next(), next(), next(), next());
    // dig the whole spiral, numbering the graves by the night they are dug,
    // with a frame of dug cells around the cemetery standing for the wall
    let mut night = vec![vec![-1i32; m + 2]; n + 2];
    for r in 0..n + 2 {
        for c in 0..m + 2 {
            if r == 0 || r == n + 1 || c == 0 || c == m + 1 {
                night[r][c] = 0;
            }
        }
    }
    let (mut r, mut c, mut d) = (1usize, 1usize, 0usize);
    night[1][1] = 1;
    for day in 2..=(n * m) as i32 {
        loop {
            let (nr, nc) = (r as i32 + STEPS[d].0, c as i32 + STEPS[d].1);
            if night[nr as usize][nc as usize] < 0 {
                r = nr as usize;
                c = nc as usize;
                break;
            }
            d = (d + 1) % STEPS.len();
        }
        night[r][c] = day;
    }
    println!("{}", (night[r1][c1] - night[r2][c2]).abs());
}
