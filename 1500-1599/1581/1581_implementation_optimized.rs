use std::io::{self, BufWriter, Read, Write};

// the numbers are parsed by hand from the bytes of the input
fn read_int(input: &mut impl Iterator<Item = io::Result<u8>>) -> usize {
    let mut value = 0;
    let mut started = false;
    for byte in input.by_ref() {
        let c = byte.unwrap();
        if c.is_ascii_digit() {
            value = value * 10 + usize::from(c - b'0');
            started = true;
        } else if started {
            break;
        }
    }
    value
}

fn main() {
    const OUTPUT_BUFFER_SIZE: usize = 1024;
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes();
    let stdout = io::stdout();
    let mut output = BufWriter::with_capacity(OUTPUT_BUFFER_SIZE, stdout.lock());
    let n = read_int(&mut input);
    // the numbers are not stored: each is compared with the previous one
    let mut previous = read_int(&mut input);
    let mut count = 1;
    // each run of equal numbers is said as its length and then the number
    for _ in 1..n {
        let value = read_int(&mut input);
        if value == previous {
            count += 1;
        } else {
            write!(output, "{} {} ", count, previous).unwrap();
            previous = value;
            count = 1;
        }
    }
    writeln!(output, "{} {}", count, previous).unwrap();
}
