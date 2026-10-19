use std::io::{self, Read};

fn palindrome_counts(word: &[u8]) -> (Vec<i32>, Vec<i32>) {
    let n = word.len();
    let size = n as i32;
    let mut radii = vec![0i32; n];
    let mut ending = vec![0i32; n + 1];
    let mut starting = vec![0i32; n + 1];
    let (mut left, mut right) = (0i32, -1i32);
    for center in 0..n {
        let c = center as i32;
        let mut radius = if c > right {
            1
        } else {
            radii[(left + right - c) as usize].min(right - c + 1)
        };
        while c - radius >= 0
            && c + radius < size
            && word[(c - radius) as usize] == word[(c + radius) as usize]
        {
            radius += 1;
        }
        radii[center] = radius;
        if c + radius - 1 > right {
            left = c - radius + 1;
            right = c + radius - 1;
        }
        ending[center] += 1;
        ending[(c + radius) as usize] -= 1;
        starting[(c - radius + 1) as usize] += 1;
        starting[center + 1] -= 1;
    }
    left = 0;
    right = -1;
    for center in 0..n {
        let c = center as i32;
        let mut radius = if c > right {
            0
        } else {
            radii[(left + right - c + 1) as usize].min(right - c + 1)
        };
        while c - radius - 1 >= 0
            && c + radius < size
            && word[(c - radius - 1) as usize] == word[(c + radius) as usize]
        {
            radius += 1;
        }
        radii[center] = radius;
        if c + radius - 1 > right {
            left = c - radius;
            right = c + radius - 1;
        }
        if radius != 0 {
            ending[center] += 1;
            ending[(c + radius) as usize] -= 1;
            starting[(c - radius) as usize] += 1;
            starting[center] -= 1;
        }
    }
    let (mut count_ending, mut count_starting) = (0, 0);
    for i in 0..n {
        count_ending += ending[i];
        count_starting += starting[i];
        ending[i] = count_ending;
        starting[i] = count_starting;
    }
    (ending, starting)
}

fn solve(word: &[u8]) -> i64 {
    let (ending, starting) = palindrome_counts(word);
    let mut answer = 0i64;
    for cut in 0..word.len().saturating_sub(1) {
        answer += i64::from(ending[cut]) * i64::from(starting[cut + 1]);
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    println!("{}", solve(input.trim().as_bytes()));
}
