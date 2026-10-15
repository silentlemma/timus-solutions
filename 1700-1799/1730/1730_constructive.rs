use std::io::{self, Read};

fn gcd(a: usize, b: usize) -> usize {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn build(lo: usize, hi: usize, owner: &[usize], animals: &[&str], rows: &mut Vec<String>) -> usize {
    if owner[lo] == owner[hi - 1] {
        rows.push(animals[owner[lo]].to_string());
    } else {
        let mid = (lo + hi) / 2;
        let left = build(lo, mid, owner, animals, rows);
        let right = build(mid, hi, owner, animals, rows);
        rows.push(format!("{} {}", left, right));
    }
    rows.len()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let animals: Vec<&str> = it.next().unwrap().split('-').collect();
    let mut parts = Vec::new();
    let mut leaves = 1;
    for _ in 0..animals.len() {
        let mut fraction = it.next().unwrap().split('/').map(|w| w.parse::<usize>().unwrap());
        let (a, b) = (fraction.next().unwrap(), fraction.next().unwrap());
        let g = gcd(a, b);
        let (a, b) = (a / g, b / g);
        // a crossing halves every share, so only shares with a power of
        // two below can come out
        if !b.is_power_of_two() {
            println!("No solution");
            return;
        }
        leaves = leaves.max(b);
        parts.push((a, b));
    }
    // give each animal its share of the equal leaves, in order, and cross
    // halves of the leaves; a half that is one animal is just that animal
    let mut owner = Vec::with_capacity(leaves);
    for (i, &(a, b)) in parts.iter().enumerate() {
        owner.extend(std::iter::repeat(i).take(a * (leaves / b)));
    }
    let mut rows = Vec::new();
    build(0, leaves, &owner, &animals, &mut rows);
    println!("{}\n{}", rows.len(), rows.join("\n"));
}
