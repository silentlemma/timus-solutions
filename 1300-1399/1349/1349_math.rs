use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // by Fermat's last theorem only the first and second powers have answers
    let answer = match input.trim().parse::<u32>().unwrap() {
        1 => "1 2 3",
        2 => "3 4 5",
        _ => "-1",
    };
    println!("{}", answer);
}
