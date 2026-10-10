use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut students: Vec<(i32, i32, i32)> = (0..n)
        .map(|_| (it.next().unwrap(), it.next().unwrap(), it.next().unwrap()))
        .collect();
    students.sort();
    // moving the start earlier changes nobody's order or wait, it only adds
    // the same amount to every deadline: the answer is the worst lateness
    let (mut busy_until, mut worst) = (0, 0);
    for (ready, talk, deadline) in students {
        busy_until = busy_until.max(ready) + talk;
        worst = worst.max(busy_until - deadline);
    }
    println!("{}", worst);
}
