use std::io;

const SPLIT: u32 = 3;

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    // no power of two is divisible by 3, so from a multiple of 3 every move
    // leaves a non-multiple, and from a non-multiple taking 1 or 2 stones
    // leaves a multiple; the remainder is also the smallest such move
    let rest = line
        .trim()
        .chars()
        .map(|c| c.to_digit(10).unwrap())
        .sum::<u32>()
        % SPLIT;
    if rest == 0 {
        println!("2");
    } else {
        println!("1\n{}", rest);
    }
}
