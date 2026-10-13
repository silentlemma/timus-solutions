use std::io::{self, Read};

const NINE: i64 = 9;
const BASE: i64 = 10;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let records: Vec<&str> = (0..n).map(|_| it.next().unwrap()).collect();
    let total: i64 = records.iter().map(|r| r.parse::<i64>().unwrap()).sum();
    let diff = it.next().unwrap().parse::<i64>().unwrap() - total;
    if diff == 0 {
        println!("Input has no error.");
        return;
    }
    // swapping digits a (at 10^(i+1)) and b (at 10^i) adds 9 * (b - a) * 10^i
    if diff % NINE == 0 {
        let (mut step, mut place) = (diff / NINE, 0usize);
        while step % BASE == 0 {
            step /= BASE;
            place += 1;
        }
        if step.abs() < BASE {
            for (number, rec) in records.iter().enumerate() {
                let mut digits = rec.as_bytes().to_vec();
                if digits.len() < place + 2 {
                    continue;
                }
                let hi = digits.len() - 2 - place; // index of the digit at 10^(i+1)
                if digits[hi + 1] as i64 - digits[hi] as i64 != step {
                    continue;
                }
                if hi == 0 && digits[1] == b'0' {
                    continue; // the swap would make a leading zero
                }
                digits.swap(hi, hi + 1);
                println!(
                    "Error in record #{}. Correct number is: {}.",
                    number + 1,
                    String::from_utf8(digits).unwrap()
                );
                return;
            }
        }
    }
    println!("Unrecoverable error.");
}
