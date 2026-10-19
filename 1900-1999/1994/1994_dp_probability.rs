use std::io::{self, Read};

fn build(limit: usize, maximum_spies: usize) -> Vec<Vec<f64>> {
    let mut choose: Vec<Vec<f64>> = Vec::new();
    for size in 0..=limit {
        let mut row = vec![1.0; size + 1];
        for j in 1..size {
            row[j] = choose[size - 1][j - 1] + choose[size - 1][j];
        }
        choose.push(row);
    }
    let mut table = vec![vec![0.0; maximum_spies + 1]; limit + 1];
    for size in 1..=limit {
        table[size][0] = size as f64;
        for spies in 1..=maximum_spies.min(size - 1) {
            let loyal = size - spies;
            let mut best: f64 = 0.0;
            for retained in 1..size {
                let lower = retained.saturating_sub(loyal);
                let upper = spies.min((retained - 1) / 2);
                let mut weighted = 0.0;
                for remaining in lower..=upper {
                    weighted += choose[spies][remaining]
                        * choose[loyal][retained - remaining]
                        * table[retained - remaining][remaining];
                }
                best = best.max(weighted / choose[size][retained]);
            }
            table[size][spies] = best;
        }
    }
    table
}
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let total: usize = tokens.next().unwrap().parse().unwrap();
    let spies: usize = tokens.next().unwrap().parse().unwrap();
    let answer = if total <= 2 * spies {
        0.0
    } else {
        build(total - spies, spies)[total - spies][spies]
    };
    println!("{:.12}", answer);
}
