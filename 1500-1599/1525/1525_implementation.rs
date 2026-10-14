use std::io::{self, Read};

const AXES: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let size: Vec<i64> = (0..AXES)
        .map(|_| it.next().unwrap().parse().unwrap())
        .collect();
    // empty when there are no instructions
    let program = it.next().unwrap_or("").as_bytes();
    // the moves along each axis: decrease, increase
    let (down, up) = (b"ldb", b"ruf");
    let mut total = 1i64;
    for (a, &len) in size.iter().enumerate() {
        // each move keeps neighbouring starts at most one apart and in order,
        // so the finishes fill the range between the extreme starts
        let (mut low, mut high) = (1i64, len);
        for &step in program {
            if step == up[a] {
                low = (low + 1).min(len);
                high = (high + 1).min(len);
            } else if step == down[a] {
                low = (low - 1).max(1);
                high = (high - 1).max(1);
            }
        }
        total *= high - low + 1;
    }
    println!("{}", total);
}
