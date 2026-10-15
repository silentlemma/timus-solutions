use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<f64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    // Sandro's own spot holds no demon: stay there and reach the farthest one
    let farthest = nums[1..].chunks(2).map(|p| p[0].hypot(p[1])).fold(0.0, f64::max);
    println!("0 0 {:.10}", farthest);
}
