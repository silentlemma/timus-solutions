use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|w| w.parse::<u32>().unwrap());
    let (l, k, h) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
    // the time to reach x is x h / k plus a part that repeats every k km
    // and lies between 0 and h, so the last l mod k km take 0 to h hours
    let whole = l / k;
    let slowest = whole + u32::from(l % k > 0);
    println!("{:.8} {:.8}", f64::from(whole * h), f64::from(slowest * h));
}
