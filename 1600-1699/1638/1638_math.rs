use std::cmp::Ordering;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut nums = text
        .split_ascii_whitespace()
        .map(|w| w.parse::<i64>().unwrap());
    let mut next = || nums.next().unwrap();
    let (pages, cover, start, stop) = (next(), next(), next(), next());
    // on a shelf a volume's first page faces its right neighbour and its
    // last page faces the left one
    let whole = pages + 2 * cover;
    let length = match start.cmp(&stop) {
        Ordering::Equal => pages,
        Ordering::Less => 2 * cover + (stop - start - 1) * whole,
        Ordering::Greater => 2 * pages + 2 * cover + (start - stop - 1) * whole,
    };
    println!("{}", length);
}
