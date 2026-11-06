use std::io::{self, BufRead, Write};

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut header = String::new();
    input.read_line(&mut header)?;
    let mut values = header.split_ascii_whitespace();
    let size: usize = values.next().unwrap().parse().unwrap();
    let start: u16 = values.next().unwrap().parse().unwrap();
    let mut incoming = vec![Vec::<u16>::new(); size + 1];
    let (mut from, mut to, mut missing) = (1, 1, 0);
    loop {
        let block = input.fill_buf()?;
        if block.is_empty() {
            break;
        }
        for &byte in block {
            if byte != b'0' && byte != b'1' {
                continue;
            }
            if byte == b'0' && from != to {
                incoming[to].push(from as u16);
                missing += 1;
            }
            to += 1;
            if to > size {
                from += 1;
                to = 1;
            }
        }
        let consumed = block.len();
        input.consume(consumed);
    }

    // Traverse reversed channels so Hierholzer's pop order gives the forward route.
    let mut stack = Vec::with_capacity(missing + 1);
    stack.push(start);
    let mut previous = None;
    let mut output = io::BufWriter::new(io::stdout().lock());
    while let Some(&city) = stack.last() {
        if let Some(next) = incoming[city as usize].pop() {
            stack.push(next);
        } else {
            if let Some(before) = previous {
                writeln!(output, "{before} {city}")?;
            }
            previous = stack.pop();
        }
    }
    output.flush()
}
