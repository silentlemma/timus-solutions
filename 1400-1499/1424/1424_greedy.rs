use std::collections::BinaryHeap;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let mut next = || it.next().unwrap();
    let (n, m, k, price) = (next(), next(), next(), next());
    let mut starts = vec![Vec::new(); n + 1];
    let mut finish = vec![0usize; k + 1];
    for i in 1..=k {
        let s = next();
        finish[i] = next();
        starts[s].push(i);
    }
    let mut ends = vec![0usize; n + 1];
    let mut taken = vec![false; k + 1];
    let mut on_board = BinaryHeap::new(); // riders by the farthest stop first
    let mut riding = 0;
    for stop in 1..=n {
        riding -= ends[stop];
        for &i in &starts[stop] {
            taken[i] = true;
            on_board.push((finish[i], i));
            ends[finish[i]] += 1;
            riding += 1;
        }
        // too many: drop whoever would ride the longest
        while riding > m {
            let (f, i) = on_board.pop().unwrap();
            taken[i] = false;
            ends[f] -= 1;
            riding -= 1;
        }
    }
    let chosen: Vec<String> = (1..=k)
        .filter(|&i| taken[i])
        .map(|i| i.to_string())
        .collect();
    println!("{}", chosen.len() * price);
    println!("{}", chosen.join(" "));
}
