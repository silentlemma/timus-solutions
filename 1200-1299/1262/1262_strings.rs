use std::io::{self, Read};

// Roman digits needed for each decimal digit: -, I, II, III, IV, V, VI,
// VII, VIII, IX
const LENGTHS: [usize; 10] = [0, 1, 2, 3, 2, 1, 2, 3, 4, 2];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let total: usize = input
        .trim()
        .bytes()
        .map(|c| LENGTHS[(c - b'0') as usize])
        .sum();
    println!("{}", total);
}
