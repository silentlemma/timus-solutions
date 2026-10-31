use std::io::{self, Read};

const RECORDS: usize = 6;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    // six borrowed names and prices need neither cloned strings nor a hash table.
    let mut records = [("", 0i32); RECORDS];
    for record in &mut records {
        words.next().unwrap();
        *record = (
            words.next().unwrap(),
            words.next().unwrap().parse().unwrap(),
        );
    }
    let (mut answer, mut best_count, mut best_price) = ("", 0, 0);
    for &(model, _) in &records {
        let (mut count, mut cheapest) = (0, i32::MAX);
        for &(other, price) in &records {
            if other == model {
                count += 1;
                cheapest = cheapest.min(price);
            }
        }
        if count > best_count
            || count == best_count && cheapest < best_price
            || count == best_count && cheapest == best_price && model < answer
        {
            answer = model;
            best_count = count;
            best_price = cheapest;
        }
    }
    println!("{}", answer);
}
