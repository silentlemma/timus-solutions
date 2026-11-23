use std::collections::{HashSet, VecDeque};
use std::io::{self, Read};

const CANS: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let cap: Vec<usize> = input.split_whitespace().map(|x| parse_integer(x)).collect();
    let sz: Vec<usize> = cap.iter().map(|c| c + 1).collect();
    let code = |v: &[usize; CANS]| (v[0] * sz[1] + v[1]) * sz[2] + v[2];
    // a state (x, y, z) as one number; every move leaves some can empty or full
    let mut seen = vec![false; sz[0] * sz[1] * sz[2]];
    seen[0] = true;
    let mut queue = VecDeque::from(vec![[0usize; CANS]]);
    let mut volumes = HashSet::new();
    while let Some(v) = queue.pop_front() {
        for mask in 1..1usize << CANS {
            volumes.insert(
                (0..CANS)
                    .filter(|&i| mask >> i & 1 == 1)
                    .map(|i| v[i])
                    .sum::<usize>(),
            );
        }
        for i in 0..CANS {
            for j in 0..=CANS {
                let mut w = v;
                if j == CANS {
                    w[i] = cap[i]; // fill can i from the pump up to the brim
                } else if i != j {
                    // pour i into j
                    let amount = v[i].min(cap[j] - v[j]);
                    w[i] -= amount;
                    w[j] += amount;
                }
                let k = code(&w);
                if !seen[k] {
                    seen[k] = true;
                    queue.push_back(w);
                }
            }
        }
    }
    volumes.remove(&0);
    println!("{}", volumes.len());
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
