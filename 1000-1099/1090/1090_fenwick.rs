use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, k) = (it.next().unwrap(), it.next().unwrap());
    let (mut best, mut best_row) = (-1i64, 0);
    let mut tree = vec![0usize; n + 1];
    for r in 1..=k {
        tree.iter_mut().for_each(|v| *v = 0);
        let mut jumps = 0i64;
        for i in 0..n {
            let x = it.next().unwrap();
            // each recruit jumps once for every earlier recruit with a larger
            // number: earlier minus those not larger, counted by the tree
            let mut smaller = 0;
            let mut j = x;
            while j > 0 {
                smaller += tree[j];
                j &= j - 1;
            }
            jumps += (i - smaller) as i64;
            let mut j = x;
            while j <= n {
                tree[j] += 1;
                j += j & j.wrapping_neg();
            }
        }
        if jumps > best {
            best = jumps;
            best_row = r;
        }
    }
    println!("{}", best_row);
}
