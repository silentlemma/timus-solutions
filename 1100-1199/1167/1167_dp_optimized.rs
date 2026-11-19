#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn read_byte() -> i32 {
    // SAFETY: getchar has no pointer arguments and reads the standard stream.
    unsafe { getchar() }
}

fn read_number() -> Option<i64> {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    if byte < 0 {
        return None;
    }
    let negative = byte == b'-' as i32;
    if negative || byte == b'+' as i32 {
        byte = read_byte();
    }
    let mut value = 0i64;
    while (b'0' as i32..=b'9' as i32).contains(&byte) {
        let digit = i64::from(byte - b'0' as i32);
        // Accumulating negatives directly also accepts i64::MIN.
        value = if negative {
            value * 10 - digit
        } else {
            value * 10 + digit
        };
        byte = read_byte();
    }
    Some(value)
}

fn number() -> i64 {
    read_number().unwrap()
}

fn write_byte(byte: u8) {
    // SAFETY: putchar accepts a byte promoted to int and has no pointers.
    unsafe {
        putchar(i32::from(byte));
    }
}

fn write_number(value: i64) {
    const DIGITS: usize = 20;
    let mut remaining = value.unsigned_abs();
    if value < 0 {
        write_byte(b'-');
    }
    let mut buffer = [0u8; DIGITS];
    let mut start = buffer.len();
    loop {
        start -= 1;
        buffer[start] = b'0' + (remaining % 10) as u8;
        remaining /= 10;
        if remaining == 0 {
            break;
        }
    }
    for &digit in &buffer[start..] {
        write_byte(digit);
    }
}

const UNREACHABLE: u16 = u16::MAX;
struct Layer<'a> {
    black: &'a [u16],
    previous: &'a [u16],
    current: &'a mut [u16],
}
impl Layer<'_> {
    fn cost(&self, left: usize, right: usize) -> u32 {
        let black = u32::from(self.black[right] - self.black[left]);
        black * ((right - left) as u32 - black)
    }
    fn solve(&mut self, low: usize, high: usize, first: usize, last: usize) {
        if low > high {
            return;
        }
        let middle = (low + high) / 2;
        let (mut best, mut split) = (u32::from(UNREACHABLE), first);
        for candidate in first..=last.min(middle - 1) {
            let value = u32::from(self.previous[candidate]) + self.cost(candidate, middle);
            if value < best {
                best = value;
                split = candidate;
            }
        }
        self.current[middle] = best as u16;
        if middle > low {
            self.solve(low, middle - 1, first, split);
        }
        self.solve(middle + 1, high, split, last);
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (count, groups) = (number() as usize, number() as usize);
    let mut black = vec![0u16; count + 1];
    for i in 0..count {
        black[i + 1] = black[i] + number() as u16;
    }
    // At most five hundred horses give fewer mixed pairs than the u16 sentinel.
    let (mut previous, mut current) = (vec![UNREACHABLE; count + 1], vec![UNREACHABLE; count + 1]);
    previous[0] = 0;
    for group in 1..=groups {
        current.fill(UNREACHABLE);
        Layer {
            black: &black,
            previous: &previous,
            current: &mut current,
        }
        .solve(group, count, group - 1, count - 1);
        std::mem::swap(&mut previous, &mut current);
    }
    write_number(i64::from(previous[count]));
    write_byte(b'\n');

    0
}
