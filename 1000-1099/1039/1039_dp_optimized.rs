use std::io::{self, Read};

fn number(input: &mut impl Iterator<Item = u8>) -> i32 {
    let first = input.find(|byte| !byte.is_ascii_whitespace()).unwrap();
    let mut value = match first {
        b'+' | b'-' => 0,
        digit => i32::from(digit - b'0'),
    };
    for byte in input.take_while(u8::is_ascii_digit) {
        value = value * 10 + i32::from(byte - b'0');
    }
    if first == b'-' {
        -value
    } else {
        value
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map(Result::unwrap);
    let n = number(&mut input) as usize;
    let mut parent = vec![0u16; n + 1];
    let mut children = vec![0u16; n + 1];
    let mut scores = vec![(0, 0); n + 1];
    for (take, _) in &mut scores[1..] {
        *take = number(&mut input);
    }
    loop {
        let child = number(&mut input) as usize;
        if child == 0 {
            break;
        }
        let boss = number(&mut input) as usize;
        parent[child] = boss as u16;
        children[boss] += 1;
    }
    let mut ready = Vec::with_capacity(n);
    for (employee, &count) in children.iter().enumerate().skip(1) {
        if count == 0 {
            ready.push(employee as u16);
        }
    }
    let (mut head, mut total) = (0, 0);
    // A boss is ready once every direct report has contributed its scores.
    while head < ready.len() {
        let employee = usize::from(ready[head]);
        head += 1;
        let (take, skip) = scores[employee];
        let best = take.max(skip);
        let boss = usize::from(parent[employee]);
        if boss == 0 {
            total += best;
        } else {
            scores[boss].0 += skip;
            scores[boss].1 += best;
            children[boss] -= 1;
            if children[boss] == 0 {
                ready.push(parent[employee]);
            }
        }
    }
    println!("{}", total);
}
