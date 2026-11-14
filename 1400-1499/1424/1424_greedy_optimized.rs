use std::collections::BinaryHeap;
use std::io::{self, BufRead, BufWriter, Write};

const ID_BITS: u32 = 16;
const ID_MASK: u64 = (1 << ID_BITS) - 1;

fn number(input: &mut impl BufRead) -> usize {
    let (mut value, mut started) = (0, false);
    loop {
        let buffer = input.fill_buf().unwrap();
        if buffer.is_empty() {
            return value;
        }
        let mut consumed = 0;
        for &byte in buffer {
            consumed += 1;
            if byte.is_ascii_digit() {
                value = 10 * value + usize::from(byte - b'0');
                started = true;
            } else if started {
                input.consume(consumed);
                return value;
            }
        }
        input.consume(consumed);
    }
}

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let (stops, capacity) = (number(&mut input), number(&mut input));
    let (requests, price) = (number(&mut input), number(&mut input));
    let mut starts = vec![0u16; stops + 1];
    let mut ends = vec![0u16; stops + 1];
    let mut following = vec![0u16; requests + 1];
    let mut finish = vec![0u32; requests + 1];
    for id in 1..=requests {
        let start = number(&mut input);
        finish[id] = number(&mut input) as u32;
        following[id] = starts[start];
        starts[start] = id as u16;
    }

    let mut chosen = vec![false; requests + 1];
    let mut farthest = BinaryHeap::new();
    let mut riding = 0;
    let mut count = 0;
    for (stop, &first) in starts.iter().enumerate() {
        riding -= usize::from(ends[stop]);
        let mut id = usize::from(first);
        while id != 0 {
            let end = finish[id] as usize;
            chosen[id] = true;
            riding += 1;
            count += 1;
            ends[end] += 1;
            // A key orders by destination first and breaks ties by passenger number.
            farthest.push(((end as u64) << ID_BITS) | id as u64);
            if riding > capacity {
                let drop = farthest.pop().unwrap();
                chosen[(drop & ID_MASK) as usize] = false;
                ends[(drop >> ID_BITS) as usize] -= 1;
                riding -= 1;
                count -= 1;
            }
            id = usize::from(following[id]);
        }
    }
    let mut out = BufWriter::new(io::stdout().lock());
    writeln!(out, "{}", count as u64 * price as u64)?;
    let mut separator = "";
    for (id, &accepted) in chosen.iter().enumerate() {
        if accepted {
            write!(out, "{separator}{id}")?;
            separator = " ";
        }
    }
    writeln!(out)
}
