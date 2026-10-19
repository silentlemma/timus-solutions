use std::io::{self, Read};

fn required_input(current: i32, history: &[(i32, i32)]) -> i32 {
    let mut answer = current - 2;
    for &(displayed, entered) in history {
        answer += displayed - entered - 2;
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count = tokens.next().unwrap().parse::<usize>().unwrap();
    let current = tokens.next().unwrap().parse::<i32>().unwrap();
    let history: Vec<(i32, i32)> = (0..count)
        .map(|_| {
            let displayed = tokens.next().unwrap().parse().unwrap();
            let entered = tokens.next().unwrap().parse().unwrap();
            (displayed, entered)
        })
        .collect();
    let answer = required_input(current, &history);
    if answer >= 0 {
        println!("{}", answer);
    } else {
        println!("Big Bang!");
    }
}
