use std::io::{self, Read, Write};

const PERCENT: usize = 100;
const PERIODS_PER_BLOCK: usize = 80;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut words = input.split_ascii_whitespace();
    let mut count: usize = words.next().unwrap().parse().unwrap();
    let brightness: usize = words.next().unwrap().parse().unwrap();

    let mut block = [b'0'; PERCENT * PERIODS_PER_BLOCK];
    let mut remainder = 0;
    for lamp in &mut block[..PERCENT] {
        remainder += brightness;
        if remainder >= PERCENT {
            *lamp = b'1';
            remainder -= PERCENT;
        }
    }
    // The remainder returns to zero after PERCENT lamps.
    let mut filled = PERCENT;
    while filled < block.len() {
        let copied = filled.min(block.len() - filled);
        block.copy_within(..copied, filled);
        filled += copied;
    }

    let mut output = io::stdout().lock();
    while count >= block.len() {
        output.write_all(&block)?;
        count -= block.len();
    }
    output.write_all(&block[..count])?;
    output.write_all(b"\n")?;
    output.flush()
}
