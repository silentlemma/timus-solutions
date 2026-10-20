use std::io::{self, Read};

const MIN_SUM: i64 = 3;

fn longest_chain(mut first: i64, mut second: i64) -> i64 {
    if first > second {
        std::mem::swap(&mut first, &mut second);
    }
    let difference = second - first;
    if difference == 0 {
        return 2;
    }
    if difference == 1 {
        return second - 1;
    }
    if difference == 2 {
        if second % 2 == 1 {
            return second - 1;
        }
        return second / 2;
    }
    // A longest chain joins two distinct residue classes modulo the difference.
    2 * ((second - MIN_SUM) / difference + 1)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let first = tokens.next().unwrap().parse().unwrap();
    let second = tokens.next().unwrap().parse().unwrap();
    println!("{}", longest_chain(first, second));
}
