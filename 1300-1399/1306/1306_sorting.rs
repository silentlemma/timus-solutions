use std::collections::BinaryHeap;
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let mut line = String::new();
    input.read_line(&mut line).unwrap();
    let n: usize = line.trim().parse().unwrap();
    // the n / 2 + 1 smallest numbers seen so far, as a max-heap: half the
    // input is enough, because the median is the largest or second largest
    let keep = n / 2 + 1;
    let mut heap: BinaryHeap<i32> = BinaryHeap::with_capacity(keep);
    // one number per line, read line by line: the whole input (up to 3 MB)
    // would not fit the 1 MB memory limit
    for _ in 0..n {
        line.clear();
        input.read_line(&mut line).unwrap();
        let value: i32 = line.trim().parse().unwrap();
        if heap.len() < keep {
            heap.push(value);
        } else if value < *heap.peek().unwrap() {
            heap.pop();
            heap.push(value);
        }
    }
    let top = i64::from(heap.pop().unwrap());
    if n % 2 == 1 {
        println!("{}.0", top);
    } else {
        let total = top + i64::from(heap.pop().unwrap());
        println!("{}.{}", total / 2, if total % 2 == 1 { "5" } else { "0" });
    }
}
