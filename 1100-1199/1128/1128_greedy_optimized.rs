use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| parse_integer::<usize>(t));
    let n = tok.next().unwrap();
    let enemies: Vec<Vec<usize>> = (0..n)
        .map(|_| {
            let k = tok.next().unwrap();
            (0..k).map(|_| tok.next().unwrap() - 1).collect()
        })
        .collect();
    let mut side = vec![0u8; n];
    let mut work: Vec<usize> = (0..n).collect();
    // a child with two or more enemies on its side has at most one on the
    // other, so moving it removes at least one pair of enemies sharing a
    // group; the moves stop after at most as many steps as there are pairs
    while let Some(v) = work.pop() {
        let same = enemies[v].iter().filter(|&&u| side[u] == side[v]).count();
        if same >= 2 {
            side[v] ^= 1;
            work.extend(&enemies[v]);
            work.push(v);
        }
    }
    let (group, other): (Vec<usize>, Vec<usize>) = (1..=n).partition(|&v| side[v - 1] == side[0]);
    let small = if group.len() <= other.len() {
        group
    } else {
        other
    };
    let list: Vec<String> = small.iter().map(|v| v.to_string()).collect();
    println!("{}\n{}", small.len(), list.join(" "));
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.
fn parse_integer<T>(word: &str) -> T
where
    T: From<u8> + std::ops::Add<Output = T> + std::ops::Sub<Output = T> + std::ops::Mul<Output = T>,
{
    let digits = word.as_bytes();
    let negative = digits[0] == b'-';
    let start = usize::from(negative || digits[0] == b'+');
    let mut value = T::from(0);
    for &byte in &digits[start..] {
        let digit = T::from(byte - b'0');
        let scaled = value * T::from(10);
        value = if negative {
            scaled - digit
        } else {
            scaled + digit
        };
    }
    value
}
