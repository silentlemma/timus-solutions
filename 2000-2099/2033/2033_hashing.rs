use std::collections::HashMap;
use std::io::{self, Read};

const RECORDS: usize = 6;

struct Record {
    model: String,
    price: i32,
}

fn solve(records: &[Record]) -> String {
    let mut groups = HashMap::new();
    for record in records {
        let stats = groups
            .entry(record.model.clone())
            .or_insert((0, record.price));
        stats.0 += 1;
        stats.1 = stats.1.min(record.price);
    }
    let mut answer = String::new();
    let (mut best_count, mut best_price) = (-1, 0);
    for (model, (count, price)) in groups {
        if count > best_count
            || count == best_count && price < best_price
            || count == best_count && price == best_price && model < answer
        {
            answer = model;
            best_count = count;
            best_price = price;
        }
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let mut records = Vec::new();
    for _ in 0..RECORDS {
        if tokens.next().is_none() {
            return;
        }
        let model = tokens.next().unwrap().to_owned();
        let price = tokens.next().unwrap().parse().unwrap();
        records.push(Record { model, price });
    }
    println!("{}", solve(&records));
}
