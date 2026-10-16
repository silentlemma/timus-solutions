use std::io::{self, Read};

const TURNS: usize = 4;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut k: u64 = it.next().unwrap().parse().unwrap();
    // the four cells a quarter turn takes into each other form an orbit; a
    // grille opens exactly one cell of every orbit
    let mut orbit = vec![vec![usize::MAX; n]; n];
    let mut orbits = 0;
    for r in 0..n {
        for c in 0..n {
            if orbit[r][c] != usize::MAX {
                continue;
            }
            let (mut rr, mut cc) = (r, c);
            for _ in 0..TURNS {
                orbit[rr][cc] = orbits;
                let keep = rr;
                rr = cc;
                cc = n - 1 - keep;
            }
            orbits += 1;
        }
    }
    // left[o]: cells of orbit o not passed yet, None once its window is cut
    let mut left: Vec<Option<u64>> = vec![Some(TURNS as u64); orbits];
    let mut out = String::new();
    for row in orbit.iter() {
        for &o in row.iter() {
            let rest = match left[o] {
                None => {
                    out.push('0');
                    continue;
                }
                Some(rest) => rest - 1,
            };
            left[o] = Some(rest);
            // grilles with a 0 here: every open orbit picks one of its
            // remaining cells
            let with_zero: u64 = left.iter().flatten().product();
            if k <= with_zero {
                out.push('0');
            } else {
                k -= with_zero;
                out.push('1');
                left[o] = None;
            }
        }
        out.push('\n');
    }
    print!("{}", out);
}
