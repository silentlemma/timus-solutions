use std::io::{self, Read};

const FAR: i32 = 2000; // beyond every coordinate

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<i32> = text
        .split_ascii_whitespace()
        .map(|w| w.parse().unwrap())
        .collect();
    let x = nums[1];
    let walls = &nums[2..];
    // the nearest obstacles on both sides; walking away from the exit is
    // promised to meet one, so the one needed below always exists
    let left = walls
        .iter()
        .filter(|&&w| w < 0)
        .fold(-FAR, |a, &w| a.max(w));
    let right = walls.iter().filter(|&&w| w > 0).fold(FAR, |a, &w| a.min(w));
    if x < left || x > right {
        println!("Impossible"); // an obstacle stands between the start and the exit
    } else if x > 0 {
        println!("{} {}", x, -2 * left + x);
    } else {
        println!("{} {}", 2 * right - x, -x);
    }
}
