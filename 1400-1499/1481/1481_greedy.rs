use std::io::{self, Read};

fn flip(side: u8) -> u8 {
    if side == b'L' {
        b'R'
    } else {
        b'L'
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut weights: Vec<u32> = (0..n)
        .map(|_| it.next().unwrap().parse().unwrap())
        .collect();
    weights.sort_unstable();
    let record = it.next().unwrap().as_bytes();
    // the weights in use always form a block of the sorted list whose
    // neighbours stand on opposite pans, so the pan of the largest one wins,
    // and a change adds a new largest weight, any other step a new smallest
    let changes = record.windows(2).filter(|w| w[0] != w[1]).count();
    let (mut low, mut high) = (n - 1 - changes, n - 1 - changes);
    let (mut low_side, mut high_side) = (record[0], record[0]);
    let mut out = format!("{} {}\n", weights[low], record[0] as char);
    for i in 1..n {
        if record[i] != record[i - 1] {
            high += 1;
            high_side = flip(high_side);
            out.push_str(&format!("{} {}\n", weights[high], high_side as char));
        } else {
            low -= 1;
            low_side = flip(low_side);
            out.push_str(&format!("{} {}\n", weights[low], low_side as char));
        }
    }
    print!("{}", out);
}
