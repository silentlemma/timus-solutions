use std::io::{self, Read};

fn solve(order: usize) -> String {
    let size = 1 << order;
    let mask = size - 1;
    let mut seen = vec![false; size];
    seen[0] = true;
    let mut result = Vec::with_capacity(size + order - 1);
    result.resize(order, b'0');
    let mut window = 0;
    for _ in 0..size - 1 {
        window = (window << 1) & mask;
        if !seen[window | 1] {
            window |= 1;
            result.push(b'1');
        } else {
            result.push(b'0');
        }
        seen[window] = true;
    }
    String::from_utf8(result).unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let order: usize = input.trim().parse().unwrap();
    println!("{}", solve(order));
}
