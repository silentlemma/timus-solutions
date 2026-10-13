use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut boss = vec![0usize; n + 1];
    let mut price = vec![0u64; n + 1];
    for i in 2..=n {
        boss[i] = it.next().unwrap();
        price[i] = it.next().unwrap() as u64;
    }
    // cut[v]: the cheapest way to separate v from every private below it,
    // or None until v gets a subordinate, so privates cannot be cut
    let mut cut: Vec<Option<u64>> = vec![None; n + 1];
    for v in (2..=n).rev() {
        let cost = match cut[v] {
            Some(c) => c.min(price[v]),
            None => price[v],
        };
        let p = boss[v];
        cut[p] = Some(cut[p].unwrap_or(0) + cost);
    }
    println!("{}.00", cut[1].unwrap());
}
