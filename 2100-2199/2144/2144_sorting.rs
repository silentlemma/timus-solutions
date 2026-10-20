use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<u32>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut boxes = Vec::with_capacity(n);
    let mut ok = true;
    for _ in 0..n {
        let k = it.next().unwrap() as usize;
        let sizes: Vec<u32> = it.by_ref().take(k).collect();
        if sizes.windows(2).any(|w| w[0] > w[1]) {
            ok = false;
        }
        boxes.push((sizes[0], sizes[k - 1]));
    }
    // Sorting by the first size, and then by the last, gives a valid order if any exists.
    boxes.sort();
    if boxes.windows(2).any(|w| w[0].1 > w[1].0) {
        ok = false;
    }
    println!("{}", if ok { "YES" } else { "NO" });
}
