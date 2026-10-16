use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let touches: Vec<usize> = if n == 2 {
        vec![1, 1]
    } else {
        // sweep 2..n-1 and back: the first pass catches one parity of the
        // start, the second pass the other
        (2..n).chain((2..n).rev()).collect()
    };
    let line: Vec<String> = touches.iter().map(|p| p.to_string()).collect();
    println!("{}\n{}", touches.len(), line.join(" "));
}
