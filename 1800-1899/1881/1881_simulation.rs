use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut number = || words.next().unwrap().parse::<i32>().unwrap();
    let (h, w, n) = (number(), number(), number());
    let mut lines = 1;
    let mut used = -1;
    for word in words.take(n as usize) {
        let length = word.len() as i32;
        // a word after another one on the line needs a space before it
        if used + 1 + length > w {
            lines += 1;
            used = -1;
        }
        used += 1 + length;
    }
    println!("{}", (lines + h - 1) / h);
}
