use std::io::{self, BufRead, BufWriter, Write};

fn number(input: &mut impl BufRead) -> usize {
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

fn write_group(
    output: &mut impl Write,
    falls: &[bool],
    group: bool,
    count: usize,
) -> io::Result<()> {
    writeln!(output, "{count}")?;
    let mut separator = "";
    for (edge, &fall) in falls.iter().enumerate() {
        if fall == group {
            write!(output, "{separator}{}", edge + 1)?;
            separator = " ";
        }
    }
    writeln!(output)
}

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut output = BufWriter::new(io::stdout().lock());
    let n = number(&mut input);
    let first = number(&mut input);
    let mut previous = first;
    let mut falls = vec![false; n];
    let mut count = 0;
    // The signed differences sum to zero, so only the signs need to be stored.
    for (edge, fall) in falls.iter_mut().enumerate() {
        let current = if edge + 1 < n {
            number(&mut input)
        } else {
            first
        };
        *fall = previous > current;
        count += usize::from(*fall);
        previous = current;
    }
    if count == 0 {
        falls[0] = true;
        count = 1;
    }
    writeln!(output, "YES")?;
    write_group(&mut output, &falls, true, count)?;
    write_group(&mut output, &falls, false, n - count)?;
    output.flush()
}
