use std::io::{self, Read};

const GROUPS: usize = 4; // both courses, only the first, only the second, neither

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input.split_whitespace().map(|t| t.parse().unwrap()).collect();
    let (n, m) = (v[0], v[1]);
    let column: Vec<Vec<usize>> =
        (0..m).map(|j| (0..n).map(|i| v[2 + i * m + j]).collect()).collect();
    let (mut best, mut best_a, mut best_b) = (n + 1, 0, 0);
    // every pair of courses is tried: the four groups of a pair are counted
    // in one pass over the programs
    for a in 0..m {
        for b in a + 1..m {
            let mut count = [0usize; GROUPS];
            for i in 0..n {
                count[2 * column[a][i] + column[b][i]] += 1;
            }
            let worst = *count.iter().max().unwrap();
            if worst < best {
                best = worst;
                best_a = a + 1;
                best_b = b + 1;
            }
        }
    }
    println!("{}\n{} {}", best, best_a, best_b);
}
