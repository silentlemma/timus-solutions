use std::io::{self, Read};

const MANY: u8 = 2;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (weight, n) = (v[0], v[1]);
    let mut card = vec![0];
    card.extend_from_slice(&v[2..2 + n]);
    // ways[i][s]: how many sets of the first i cards weigh s, counted up to 2
    let mut ways = vec![vec![0u8; weight + 1]];
    ways[0][0] = 1;
    for i in 1..=n {
        let mut row = ways[i - 1].clone();
        for s in card[i]..=weight {
            row[s] = MANY.min(row[s] + ways[i - 1][s - card[i]]);
        }
        ways.push(row);
    }
    match ways[n][weight] {
        0 => {
            println!("0");
            return;
        }
        MANY => {
            println!("-1");
            return;
        }
        _ => {}
    }
    // the only set: card i is in it exactly when the rest cannot be made
    // from the cards before it
    let mut missing = Vec::new();
    let mut s = weight;
    for i in (1..=n).rev() {
        if ways[i - 1][s] == 1 {
            missing.push(i);
        } else {
            s -= card[i];
        }
    }
    let out: Vec<String> = missing.iter().rev().map(|i| i.to_string()).collect();
    println!("{}", out.join(" "));
}
