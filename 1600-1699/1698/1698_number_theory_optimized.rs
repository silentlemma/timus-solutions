use std::io;

const MAX_DIGITS: usize = 2000;
const BASE: u32 = 10;
const LAST_DIGIT: u32 = 5;
const ONE_DIGIT_SOLUTIONS: u32 = 3;

fn count_solutions(n: usize) -> u32 {
    let mut digits = [0u32; MAX_DIGITS];
    let mut carry = LAST_DIGIT * LAST_DIGIT / BASE;
    let mut count = ONE_DIGIT_SOLUTIONS;
    for place in 1..n {
        // Symmetric off-diagonal pairs contribute twice to the square.
        let middle = place / 2;
        let previous = &digits[1..place];
        let pairs = previous
            .iter()
            .zip(previous.iter().rev())
            .take((place - 1) / 2);
        let pair_sum: u32 = pairs.map(|(&a, &b)| a * b).sum();
        let diagonal = if place % 2 == 0 {
            digits[middle] * digits[middle]
        } else {
            0
        };
        let total = carry + 2 * pair_sum + diagonal;
        let digit = total % BASE;
        digits[place] = digit;
        carry = total / BASE + digit;
        count += u32::from(digit != 0) + u32::from(digit != BASE - 1);
    }
    count
}

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let n = line.trim().parse().unwrap();
    println!("{}", count_solutions(n));
}
