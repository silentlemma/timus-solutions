use std::io::{self, Read, Write};

fn arrange(mut values: Vec<i32>, capacity: i32) -> (usize, Vec<i32>) {
    values.sort_unstable();
    let mut queue = Vec::with_capacity(values.len());
    let (mut left, mut right, mut trips) = (0, values.len(), 0);
    while right - left >= 2 {
        if values[left] + values[right - 1] > capacity {
            // The largest value cannot share a trip with any remaining value.
            queue.push(values[left]);
            queue.push(values[right - 1]);
            left += 1;
            right -= 1;
            trips += 2;
        } else {
            queue.push(values[left]);
            queue.push(values[left + 1]);
            left += 2;
            trips += 1;
        }
    }
    if left < right {
        queue.push(values[left]);
        trips += 1;
    }
    (trips, queue)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let capacity: i32 = tokens.next().unwrap().parse().unwrap();
    let values = (0..count)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let (trips, queue) = arrange(values, capacity);
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    writeln!(out, "{}", trips).unwrap();
    for (index, value) in queue.iter().enumerate() {
        if index > 0 {
            write!(out, " ").unwrap();
        }
        write!(out, "{}", value).unwrap();
    }
    writeln!(out).unwrap();
}
