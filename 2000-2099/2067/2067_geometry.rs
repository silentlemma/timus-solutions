use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let n = v[0] as usize;
    let s: Vec<i64> = (0..n).map(|i| v[1 + 2 * i]).collect();
    let r: Vec<i64> = (0..n).map(|i| v[2 + 2 * i]).collect();
    // v, u are best friends exactly when every other point lies on the
    // segment vu: all points collinear, v and u the two extreme ones
    let (mut low, mut high) = (0, 0);
    for i in 1..n {
        if (s[1] - s[0]) * (r[i] - r[0]) != (s[i] - s[0]) * (r[1] - r[0]) {
            println!("0");
            return;
        }
        if (s[i], r[i]) < (s[low], r[low]) {
            low = i;
        }
        if (s[i], r[i]) > (s[high], r[high]) {
            high = i;
        }
    }
    println!("1\n{} {}", low + 1, high + 1);
}
