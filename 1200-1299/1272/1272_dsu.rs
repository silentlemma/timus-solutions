use std::io::{self, Read};

fn find(parent: &mut [usize], mut x: usize) -> usize {
    while parent[x] != x {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    x
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, k) = (it.next().unwrap(), it.next().unwrap());
    it.next(); // the bridges themselves do not matter
    let mut parent: Vec<usize> = (0..=n).collect();
    // tunnels are free; every bridge joins two of the remaining groups
    let mut groups = n;
    for _ in 0..k {
        let a = find(&mut parent, it.next().unwrap());
        let b = find(&mut parent, it.next().unwrap());
        if a != b {
            parent[a] = b;
            groups -= 1;
        }
    }
    println!("{}", groups - 1);
}
