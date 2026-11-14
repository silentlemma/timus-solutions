use std::io::{self, BufRead, BufWriter, Write};

const CLASSES: usize = 4;

fn magnitude(input: &mut impl BufRead) -> usize {
    let mut value = 0;
    let mut started = false;
    loop {
        let buffer = input.fill_buf().unwrap();
        if buffer.is_empty() {
            return value;
        }
        let mut consumed = 0;
        for &byte in buffer {
            consumed += 1;
            if byte.is_ascii_digit() {
                value = value * 10 + usize::from(byte - b'0');
                started = true;
            } else if started {
                input.consume(consumed);
                return value;
            }
        }
        input.consume(consumed);
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let count = magnitude(&mut input);
    let mut indices = vec![0u16; count * CLASSES];
    let mut sizes = [0; CLASSES];
    for index in 1.. {
        let x = magnitude(&mut input);
        let y = magnitude(&mut input);
        let group = 2 * (x & 1) + (y & 1);
        let start = group * count;
        indices[start + sizes[group]] = index;
        sizes[group] += 1;
        if sizes[group] == count {
            let stdout = io::stdout();
            let mut output = BufWriter::new(stdout.lock());
            writeln!(output, "OK").unwrap();
            for (i, index) in indices[start..start + count].iter().enumerate() {
                if i != 0 {
                    write!(output, " ").unwrap();
                }
                write!(output, "{index}").unwrap();
            }
            writeln!(output).unwrap();
            break;
        }
    }
}
