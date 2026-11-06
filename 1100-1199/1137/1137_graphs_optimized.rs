use std::io::{self, BufWriter, Read, Write};

const STOPS: usize = 1000;
const SEGMENTS: usize = 20_000;

fn number(input: &mut impl Iterator<Item = u8>) -> usize {
    let first = input.find(|byte| byte.is_ascii_digit()).unwrap();
    let mut value = usize::from(first - b'0');
    for byte in input.take_while(u8::is_ascii_digit) {
        value = value * 10 + usize::from(byte - b'0');
    }
    value
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map(Result::unwrap);
    let routes = number(&mut input);
    let mut first = [0u16; STOPS + 1];
    let (mut next, mut destination) = ([0u16; SEGMENTS + 1], [0u16; SEGMENTS + 1]);
    let (mut start, mut edges) = (0, 0);
    for _ in 0..routes {
        let count = number(&mut input);
        let mut from = number(&mut input);
        if start == 0 {
            start = from;
        }
        for _ in 0..count {
            let to = number(&mut input);
            edges += 1;
            next[edges] = first[from];
            destination[edges] = to as u16;
            first[from] = edges as u16;
            from = to;
        }
    }
    if start == 0 {
        println!("0");
        return;
    }
    // The stack grows from the front and the completed route from the back.
    // Together they hold at most one initial stop and one stop per used edge.
    let mut route = [0u16; SEGMENTS + 1];
    route[0] = start as u16;
    let (mut depth, mut done) = (1, edges + 1);
    while depth != 0 {
        let stop = route[depth - 1];
        let edge = first[usize::from(stop)] as usize;
        if edge == 0 {
            depth -= 1;
            done -= 1;
            route[done] = stop;
        } else {
            first[usize::from(stop)] = next[edge];
            route[depth] = destination[edge];
            depth += 1;
        }
    }
    if done != 0 {
        println!("0");
        return;
    }
    let mut out = BufWriter::new(io::stdout().lock());
    write!(out, "{}", edges).unwrap();
    for stop in &route[..=edges] {
        write!(out, " {}", stop).unwrap();
    }
    writeln!(out).unwrap();
    out.flush().unwrap();
}
