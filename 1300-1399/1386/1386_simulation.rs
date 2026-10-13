use std::fmt::Write as _;
use std::io::{self, Read};

const COMMANDS: usize = 4;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let cells = n * m;
    // go[k][c]: the cell reached from cell c by command k, cells numbered by rows
    let mut go = vec![vec![0usize; cells]; COMMANDS];
    for row in go.iter_mut() {
        for c in row.iter_mut() {
            let (r, col) = (it.next().unwrap(), it.next().unwrap());
            *c = (r - 1) * m + (col - 1);
        }
    }
    let s = it.next().unwrap();
    // the distinct cells the player may stand on, and when each was last added
    let mut cur: Vec<usize> = (0..cells).collect();
    let mut next: Vec<usize> = Vec::with_capacity(cells);
    let mut mark = vec![usize::MAX; cells];
    for step in 0..s {
        let to = &go[it.next().unwrap() - 1];
        next.clear();
        for &c in &cur {
            let t = to[c];
            if mark[t] != step {
                mark[t] = step;
                next.push(t);
            }
        }
        std::mem::swap(&mut cur, &mut next);
    }
    cur.sort_unstable();
    let mut out = String::new();
    writeln!(out, "{}", cur.len()).unwrap();
    for &c in &cur {
        writeln!(out, "{} {}", c / m + 1, c % m + 1).unwrap();
    }
    print!("{}", out);
}
