use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let rules: Vec<(usize, usize)> = (0..m)
        .map(|_| (it.next().unwrap(), it.next().unwrap()))
        .collect();
    let mut place = vec![0; n + 1];
    for (i, subject) in it.take(n).enumerate() {
        place[subject] = i;
    }
    // the plan is right exactly when every rule points forward in it; a
    // rule from a subject to itself can never hold
    let ok = rules.iter().all(|&(s, u)| place[s] < place[u]);
    println!("{}", if ok { "YES" } else { "NO" });
}
