use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    // dryness and position, so a sort orders by both
    let mut flowers: Vec<(i64, i64)> = it.take(n).zip(0..).collect();
    flowers.sort_unstable();
    // a group of equal dryness is a segment of positions, watered by walking it once.
    // The walk ends at its left or right end, and those two states carry over
    let (mut at_left, mut at_right) = (0i64, 0i64);
    // the previous group, starting from the leftmost flower
    let (mut left, mut right) = (0i64, 0i64);
    let mut i = 0;
    while i < n {
        let mut j = i;
        while j < n && flowers[j].0 == flowers[i].0 {
            j += 1;
        }
        let (l, r) = (flowers[i].1, flowers[j - 1].1);
        let to_left = (at_left + (left - r).abs()).min(at_right + (right - r).abs()) + r - l;
        let to_right = (at_left + (left - l).abs()).min(at_right + (right - l).abs()) + r - l;
        at_left = to_left;
        at_right = to_right;
        left = l;
        right = r;
        i = j;
    }
    println!("{}", at_left.min(at_right) + n as i64);
}
