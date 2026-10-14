use std::io::{self, Read};

const FREE: i64 = 6; // calls of up to six seconds cost nothing
const MINUTE: i64 = 60;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let mut number = || words.next().unwrap().parse::<i64>().unwrap();
    let (n1, c1) = (number(), number());
    let (n2, t, c2) = (number(), number(), number());
    let n3 = number();
    let k = number() as usize;
    let minutes: i64 = text
        .split_ascii_whitespace()
        .filter(|w| w.contains(':'))
        .take(k)
        .map(|w| {
            let (mm, ss) = w.split_once(':').unwrap();
            mm.parse::<i64>().unwrap() * MINUTE + ss.parse::<i64>().unwrap()
        })
        .filter(|&seconds| seconds > FREE)
        .map(|seconds| (seconds + MINUTE - 1) / MINUTE) // a started minute counts in full
        .sum();
    println!("Basic:     {}", n1 + c1 * minutes);
    println!("Combined:  {}", n2 + c2 * (minutes - t).max(0));
    println!("Unlimited: {}", n3);
}
