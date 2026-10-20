use std::io::{self, Read};

fn blue_wins(n: i64, r1: i64, mut c1: i64, r2: i64, mut c2: i64) -> bool {
    // Reflect the board so Blue starts to the left of Red.
    if c1 > c2 {
        c1 = n + 1 - c1;
        c2 = n + 1 - c2;
    }
    let gap = c2 - c1;
    let left = c1 - 1;
    let right = n - c2;
    if r1 == r2 {
        return left > right || (left == right && gap % 2 == 0);
    }
    if gap == 0 || left == right {
        return false;
    }
    if gap == 1 {
        return true;
    }
    // A one-column tail advantage makes the gap parity decisive.
    if left == right + 1 || right == left + 1 {
        return gap % 2 == 1;
    }
    left > right
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_whitespace()
        .map(|value| value.parse::<i64>().unwrap());
    let n = values.next().unwrap();
    let r1 = values.next().unwrap();
    let c1 = values.next().unwrap();
    let r2 = values.next().unwrap();
    let c2 = values.next().unwrap();
    println!(
        "{}",
        if blue_wins(n, r1, c1, r2, c2) {
            "Blue"
        } else {
            "Red"
        }
    );
}
