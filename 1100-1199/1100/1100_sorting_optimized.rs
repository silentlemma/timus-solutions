use std::io::{self, BufWriter, Read, Write};

const MOST: usize = 100;
const BUFFER_SIZE: usize = 8192;
const DECIMAL_DIGITS: usize = 10;

// numbers are read and written by hand through 8 KB buffers: with 150 000
// lines this is much faster than parsing a String and writeln!
struct Input<R> {
    reader: R,
    buffer: [u8; BUFFER_SIZE],
    position: usize,
    length: usize,
}

impl<R: Read> Input<R> {
    fn read_byte(&mut self) -> Option<u8> {
        if self.position == self.length {
            self.length = self.reader.read(&mut self.buffer).unwrap();
            self.position = 0;
            if self.length == 0 {
                return None;
            }
        }
        let c = self.buffer[self.position];
        self.position += 1;
        Some(c)
    }

    fn read_int(&mut self) -> u32 {
        let mut value = 0;
        let mut started = false;
        while let Some(c) = self.read_byte() {
            if c.is_ascii_digit() {
                value = value * 10 + u32::from(c - b'0');
                started = true;
            } else if started {
                break;
            }
        }
        value
    }
}

fn write_int(output: &mut impl Write, mut value: u32) {
    let mut digits = [0; DECIMAL_DIGITS];
    let mut start = digits.len();
    loop {
        start -= 1;
        digits[start] = b'0' + (value % 10) as u8;
        value /= 10;
        if value == 0 {
            break;
        }
    }
    output.write_all(&digits[start..]).unwrap();
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        reader: stdin.lock(),
        buffer: [0; BUFFER_SIZE],
        position: 0,
        length: 0,
    };
    let n = input.read_int();
    // bubble sort never swaps equal scores, so teams with the same score keep
    // their input order: a counting sort by score does the same
    let mut buckets = vec![Vec::<u32>::new(); MOST + 1];
    for _ in 0..n {
        let team = input.read_int();
        let solved = input.read_int() as usize;
        buckets[solved].push(team);
    }
    let stdout = io::stdout();
    let mut output = BufWriter::with_capacity(BUFFER_SIZE, stdout.lock());
    for solved in (0..=MOST).rev() {
        for &team in &buckets[solved] {
            write_int(&mut output, team);
            output.write_all(b" ").unwrap();
            write_int(&mut output, solved as u32);
            output.write_all(b"\n").unwrap();
        }
    }
    output.flush().unwrap();
}
