use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_line(&mut input)?;
    let mut tokens = input.split_ascii_whitespace();
    let depth: u64 = tokens.next().unwrap().parse().unwrap();
    let mut path = tokens.next().unwrap().parse::<u64>().unwrap() - 1;

    let (mut left, mut right) = (1, 1);
    let mut leading_left = depth - 1;
    // Follow the path backwards, tracking the coefficients of the two bounds.
    while path != 0 {
        if path & 1 == 0 {
            left += right;
        } else {
            right += left;
        }
        path >>= 1;
        leading_left -= 1;
    }
    println!("{} {}", right, left + leading_left * right);
    Ok(())
}
