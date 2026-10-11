use std::io::{self, Read};

const FLOORS: usize = 1000;
// ten eggs already allow a binary search over all the floors
const EGGS: usize = 10;

fn main() {
    // best[k][n]: the fewest drops that settle n floors with k eggs; with d
    // drops and k eggs one can tell apart reach(d, k) floors, where
    // reach(d, k) = reach(d - 1, k - 1) + reach(d - 1, k) + 1
    let mut best = vec![vec![0usize; FLOORS + 1]; EGGS + 1];
    let mut reach = [0usize; EGGS + 1];
    let mut d = 0;
    while reach[1] < FLOORS {
        d += 1;
        let mut next = [0usize; EGGS + 1];
        for k in 1..=EGGS {
            next[k] = FLOORS.min(reach[k - 1] + reach[k] + 1);
            for n in reach[k] + 1..=next[k] {
                best[k][n] = d;
            }
        }
        reach = next;
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let mut out = String::new();
    for pair in v.chunks(2) {
        if pair[0] == 0 && pair[1] == 0 {
            break;
        }
        out += &format!("{}\n", best[pair[0].min(EGGS)][pair[1]]);
    }
    print!("{}", out);
}
