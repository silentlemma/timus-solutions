use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    // the teacher's dates come sorted, so each of the student's dates is
    // looked up by binary search, counting repeats every time
    let known: Vec<i64> = (0..n).map(|_| it.next().unwrap()).collect();
    let m = it.next().unwrap() as usize;
    let count = it
        .take(m)
        .filter(|year| known.binary_search(year).is_ok())
        .count();
    println!("{}", count);
}
