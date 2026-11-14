use std::io::{self, BufRead, Write};

const SOURCE: u8 = b'1';
const TARGET: u8 = b'2';
const SPARE: u8 = b'3';
const MAX_DISKS: usize = 31;
const DECIMAL: u32 = 10;
const RESULT_DIGITS: usize = 10;

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut rods = [0; MAX_DISKS];
    let mut count = 0;
    let mut header = true;
    let mut started = false;
    loop {
        let buffer = input.fill_buf()?;
        if buffer.is_empty() {
            break;
        }
        for &c in buffer {
            if header {
                if c.is_ascii_digit() {
                    started = true;
                } else if started {
                    header = false;
                }
            } else if c.is_ascii_digit() {
                rods[count] = c;
                count += 1;
            }
        }
        let consumed = buffer.len();
        input.consume(consumed);
    }

    let (mut source, mut target, mut spare) = (SOURCE, TARGET, SPARE);
    let mut moves = 0u32;
    let mut output = io::stdout().lock();
    // The largest remaining disk fixes the next bit of the move number.
    for &rod in rods[..count].iter().rev() {
        moves <<= 1;
        if rod == target {
            moves |= 1;
            std::mem::swap(&mut source, &mut spare);
        } else if rod == source {
            std::mem::swap(&mut target, &mut spare);
        } else {
            return output.write_all(b"-1\n");
        }
    }
    let mut digits = [b'\n'; RESULT_DIGITS + 1];
    let mut cursor = RESULT_DIGITS;
    loop {
        cursor -= 1;
        digits[cursor] = b'0' + (moves % DECIMAL) as u8;
        moves /= DECIMAL;
        if moves == 0 {
            break;
        }
    }
    output.write_all(&digits[cursor..])
}
