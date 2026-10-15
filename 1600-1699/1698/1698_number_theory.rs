use std::io::{self, Read};

const BASE: i64 = 10;
const FIVE: i64 = 5; // the last digit of one of the two endless solutions of x^2 = x

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let n: usize = text.trim().parse().unwrap();
    // x^2 ends with x exactly when x^2 = x mod 10^d for its d digits; besides
    // 0 and 1 the solutions are the endings of two 10-adic numbers, ...0625
    // and ...9376, whose digits other than the last add up to 9 place by place

    let mut digits = vec![FIVE]; // the 5-adic one, lowest digit first

    let mut carry = FIVE * FIVE / BASE; // carry into position d of the square so far
    for d in 1..n {
        // digit d of x^2: the products x_i x_j with i + j = d, plus the carry, and
        // a new digit c adds 2 * 5 * c, a multiple of 10: c is forced
        let total = carry + (1..d).map(|i| digits[i] * digits[d - i]).sum::<i64>();
        let c = total % BASE;
        digits.push(c);
        carry = (total + 2 * FIVE * c) / BASE;
    }
    let mut count = 1 + 2; // the numbers 1, 5 and 6

    for &digit in &digits[1..] {
        // a d + 1 digit number needs a nonzero leading digit
        count += (digit != 0) as i64 + (digit != BASE - 1) as i64;
    }
    println!("{}", count);
}
