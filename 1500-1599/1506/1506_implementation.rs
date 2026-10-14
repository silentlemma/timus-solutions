use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let nums: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, k) = (nums[0], nums[1]);
    let nums = &nums[2..2 + n];
    let height = (n + k - 1) / k; // the fewest rows that hold n numbers in k columns
    let mut out = String::new();
    for row in 0..height {
        // column c holds the numbers c * height ... c * height + height - 1
        for c in (0..k).take_while(|c| c * height + row < n) {
            out += &format!("{:4}", nums[c * height + row]);
        }
        out.push('\n');
    }
    print!("{}", out);
}
