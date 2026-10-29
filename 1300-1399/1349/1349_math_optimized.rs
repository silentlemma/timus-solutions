use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // by Fermat's last theorem only the first and second powers have answers
    let answer: &[u8] = match input.trim().parse::<u32>().unwrap() {
        1 => b"1 2 3\n",
        2 => b"3 4 5\n",
        _ => b"-1\n",
    };
    // the answer goes out as a byte string, without the formatting of println!
    io::stdout().write_all(answer).unwrap();
}
