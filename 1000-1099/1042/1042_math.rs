use std::io::{self, Read};

const WORD_BITS: usize = 64;

fn get(row: &[u64], c: usize) -> bool {
    row[c / WORD_BITS] >> (c % WORD_BITS) & 1 == 1
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    // equation v over GF(2): the chosen technicians turn valve v an odd number
    // of times; bit n of an equation is its right-hand side
    let words = n / WORD_BITS + 1;
    let mut eq = vec![vec![0u64; words]; n];
    for e in eq.iter_mut() {
        e[n / WORD_BITS] |= 1 << (n % WORD_BITS);
    }
    for t in 0..n {
        loop {
            let v = it.next().unwrap();
            if v == -1 {
                break;
            }
            eq[v as usize - 1][t / WORD_BITS] |= 1 << (t % WORD_BITS);
        }
    }
    // Gauss-Jordan elimination: column c ends with a single 1, in its pivot row
    let mut pivot_of = vec![usize::MAX; n];
    let mut rank = 0;
    for c in 0..n {
        let r = match (rank..n).find(|&r| get(&eq[r], c)) {
            Some(r) => r,
            None => continue,
        };
        eq.swap(r, rank);
        let row = eq[rank].clone();
        for i in 0..n {
            if i != rank && get(&eq[i], c) {
                for k in 0..words {
                    eq[i][k] ^= row[k];
                }
            }
        }
        pivot_of[c] = rank;
        rank += 1;
    }
    if (rank..n).any(|r| get(&eq[r], n)) {
        println!("No solution");
        return;
    }
    // independent technicians make the solution unique, so it is also the shortest
    let chosen: Vec<String> = (0..n)
        .filter(|&c| pivot_of[c] != usize::MAX && get(&eq[pivot_of[c]], n))
        .map(|c| (c + 1).to_string())
        .collect();
    println!("{}", chosen.join(" "));
}
