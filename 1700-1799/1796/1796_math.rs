use std::io::{self, Read};

const NOTES: &[i64] = &[10, 50, 100, 500, 1000, 5000];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let data: Vec<i64> = input.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let (counts, price) = (&data[..NOTES.len()], data[NOTES.len()]);
    let total: i64 = counts.iter().zip(NOTES.iter()).map(|(c, note)| c * note).sum();
    let smallest = counts
        .iter()
        .zip(NOTES.iter())
        .find(|(c, _)| **c > 0)
        .map(|(_, &note)| note)
        .unwrap();
    // k tickets fit when k * price <= total, and taking away the smallest
    // note must leave too little: total - smallest < k * price
    let answers: Vec<String> =
        ((total - smallest) / price + 1..=total / price).map(|k| k.to_string()).collect();
    println!("{}\n{}", answers.len(), answers.join(" "));
}
