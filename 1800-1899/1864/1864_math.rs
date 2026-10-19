use std::io::{self, Read};

const MONEY: i64 = 100;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let data: Vec<i64> = input.split_ascii_whitespace().map(|v| v.parse().unwrap()).collect();
    let (n, bought) = (data[0], &data[1..]);
    // everybody, Den too, drinks total / (n + 1); in units of 1 / (n + 1)
    // litre, friend i paid for bought[i] (n + 1) - total litres of others
    let total: i64 = bought.iter().sum();
    let over: Vec<i64> = bought.iter().map(|&b| (b * (n + 1) - total).max(0)).collect();
    let all: i64 = over.iter().sum();
    let shares: Vec<String> = over.iter().map(|&x| (MONEY * x / all).to_string()).collect();
    println!("{}", shares.join(" "));
}
