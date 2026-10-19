use std::io::{self, Read};

const MOD: u64 = 998244353;
const ROOT: u64 = 3;
const DIRECT_LIMIT: usize = 32;

fn power(mut base: u64, mut exponent: u64) -> u64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent & 1 != 0 {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exponent >>= 1;
    }
    result
}

fn transform(data: &mut [u64], inverse: bool) {
    let n = data.len();
    let mut j = 0;
    for i in 1..n {
        let mut bit = n >> 1;
        while j & bit != 0 {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        if i < j {
            data.swap(i, j);
        }
    }
    let mut length = 2;
    while length <= n {
        let mut root = power(ROOT, (MOD - 1) / length as u64);
        if inverse {
            root = power(root, MOD - 2);
        }
        for start in (0..n).step_by(length) {
            let mut factor = 1;
            for j in 0..length / 2 {
                let first = data[start + j];
                let second = data[start + j + length / 2] * factor % MOD;
                let sum = first + second;
                data[start + j] = if sum >= MOD { sum - MOD } else { sum };
                data[start + j + length / 2] = if first >= second {
                    first - second
                } else {
                    first + MOD - second
                };
                factor = factor * root % MOD;
            }
        }
        length <<= 1;
    }
    if inverse {
        let scale = power(n as u64, MOD - 2);
        for value in data {
            *value = *value * scale % MOD;
        }
    }
}

fn matches(a: &[u8], b: &[u8]) -> Vec<usize> {
    let mut prefix = vec![0; b.len()];
    let mut j = 0;
    for i in 1..b.len() {
        while j > 0 && b[i] >> 1 != b[j] >> 1 {
            j = prefix[j - 1];
        }
        if b[i] >> 1 == b[j] >> 1 {
            j += 1;
        }
        prefix[i] = j;
    }
    let mut starts = Vec::new();
    j = 0;
    for (i, value) in a.iter().enumerate() {
        while j > 0 && value >> 1 != b[j] >> 1 {
            j = prefix[j - 1];
        }
        if value >> 1 == b[j] >> 1 {
            j += 1;
        }
        if j == b.len() {
            starts.push(i + 1 - b.len());
            j = prefix[j - 1];
        }
    }
    starts
}

fn solve(a: &[u8], b: &[u8]) -> Option<(usize, usize)> {
    let (n, m) = (a.len(), b.len());
    if m > n {
        return None;
    }
    let starts = matches(a, b);
    if starts.is_empty() {
        return None;
    }
    let (mut best, mut answer) = (m + 1, 0);
    if starts.len() <= DIRECT_LIMIT {
        for &start in &starts {
            let changes = (0..m).filter(|&j| (a[start + j] ^ b[j]) & 1 != 0).count();
            if changes < best {
                best = changes;
                answer = start + 1;
            }
        }
        return Some((best, answer));
    }
    let size = (n + m - 1).next_power_of_two();
    let (mut first, mut second) = (vec![0; size], vec![0; size]);
    let mut prefix = vec![0; n + 1];
    for i in 0..n {
        first[i] = (a[i] & 1) as u64;
        prefix[i + 1] = prefix[i] + first[i] as usize;
    }
    let mut ones = 0;
    for i in 0..m {
        second[m - 1 - i] = (b[i] & 1) as u64;
        ones += (b[i] & 1) as usize;
    }
    transform(&mut first, false);
    transform(&mut second, false);
    for i in 0..size {
        first[i] = first[i] * second[i] % MOD;
    }
    transform(&mut first, true);
    for &start in &starts {
        let changes = prefix[start + m] - prefix[start] + ones - 2 * first[start + m - 1] as usize;
        if changes < best {
            best = changes;
            answer = start + 1;
        }
    }
    Some((best, answer))
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let values: Vec<u8> = tokens.map(|s| u8::from_str_radix(s, 2).unwrap()).collect();
    match solve(&values[..n], &values[n..n + m]) {
        None => println!("No"),
        Some((changes, start)) => println!("Yes\n{} {}", changes, start),
    }
}
