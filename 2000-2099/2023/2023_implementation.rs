use std::io::{self, Read};

fn solve(names: &[&str]) -> i32 {
    let mut position = 0_i32;
    let mut steps = 0;
    for name in names {
        let initial = name.as_bytes()[0];
        let target = if b"APOR".contains(&initial) {
            0
        } else if b"BMS".contains(&initial) {
            1
        } else {
            2
        };
        steps += (target - position).abs();
        position = target;
    }
    steps
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let names: Vec<&str> = tokens.take(count).collect();
    println!("{}", solve(&names));
}
