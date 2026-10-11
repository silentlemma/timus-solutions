use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let half = n / 2;
    // 1 + 9 k^2 with k = 11...1 (half ones), and 9 k^2 = k 10^half - k
    let answer = match half {
        0 => "1".to_string(),
        1 => "10".to_string(),
        _ => "1".repeat(half - 1) + "0" + &"8".repeat(half - 2) + "90",
    };
    writeln!(io::stdout().lock(), "{}", answer).unwrap();
}
