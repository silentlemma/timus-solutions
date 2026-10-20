use std::io::{self, Read};

fn gcd(mut left: u64, mut right: u64) -> u64 {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let values: Vec<u64> = (0..n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let total: u64 = values.iter().sum();

    // The two exceptional chests change a prefix and a suffix gcd.
    let mut marked = vec![false; n];
    let mut current = total;
    for (index, &value) in values.iter().enumerate() {
        let next = gcd(current, value);
        if next != current {
            marked[index] = true;
        }
        current = next;
    }
    current = total;
    for index in (0..n).rev() {
        let next = gcd(current, values[index]);
        if next != current {
            marked[index] = true;
        }
        current = next;
    }

    let mut fixed = total;
    let mut critical = Vec::new();
    for (index, &value) in values.iter().enumerate() {
        if marked[index] {
            critical.push(value);
        } else {
            fixed = gcd(fixed, value);
        }
    }

    let count = critical.len();
    let mut suffix = vec![fixed; count + 1];
    for index in (0..count).rev() {
        suffix[index] = gcd(critical[index], suffix[index + 1]);
    }
    let mut answer = suffix[0];
    let mut before = fixed;
    for first in 0..count {
        let mut running = before;
        for second in first + 1..count {
            answer = answer.max(gcd(running, suffix[second + 1]));
            running = gcd(running, critical[second]);
        }
        before = gcd(before, critical[first]);
    }

    println!("{}", answer);
}
