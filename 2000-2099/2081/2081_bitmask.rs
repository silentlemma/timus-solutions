#![no_main]

use std::ffi::{c_int, c_void};

#[cfg(unix)]
extern "C" {
    fn read(fd: c_int, buffer: *mut c_void, count: usize) -> isize;
    fn write(fd: c_int, buffer: *const c_void, count: usize) -> isize;
}

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn read(fd: c_int, buffer: *mut c_void, count: u32) -> c_int;
    #[link_name = "_write"]
    fn write(fd: c_int, buffer: *const c_void, count: u32) -> c_int;
}

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const INPUT_SIZE: usize = 8_192;

fn read_into(block: &mut [u8]) -> Option<usize> {
    let mut filled = 0;
    while filled < block.len() {
        let slice = &mut block[filled..];
        // The unwritten part of the buffer can hold the requested bytes.
        let size = unsafe { read(STDIN, slice.as_mut_ptr().cast(), slice.len() as _) };
        if size < 0 {
            return None;
        }
        if size == 0 {
            break;
        }
        filled += size as usize;
    }
    Some(filled)
}

fn send(bytes: &[u8]) -> c_int {
    // The answer slice remains valid for the duration of the call.
    let written = unsafe { write(STDOUT, bytes.as_ptr().cast(), bytes.len() as _) };
    c_int::from(written as usize != bytes.len())
}

const RADIX: i32 = 10;
const SECONDS: i32 = 60;
const MINUTES: i32 = 60;
const WIDTH: usize = 3;
const COLUMNS: [usize; 4] = [0, 4, 10, 14];
const MAX_READINGS: usize = 100;
const OUTPUT_WIDTH: usize = b"00:00\n".len();
// Each bit corresponds to one cell in a 3 by 3 digit.
const GLYPHS: [u16; RADIX as usize] = [490, 288, 242, 434, 312, 410, 474, 290, 506, 442];
const PATTERNS: usize = 1 << (WIDTH * WIDTH);

const fn matches() -> [u16; PATTERNS] {
    let mut table = [0; PATTERNS];
    let mut pattern = 0;
    while pattern < table.len() {
        let mut digit = 0;
        while digit < GLYPHS.len() {
            if pattern as u16 & GLYPHS[digit] == pattern as u16 {
                table[pattern] |= 1 << digit;
            }
            digit += 1;
        }
        pattern += 1;
    }
    table
}

static MATCHES: [u16; PATTERNS] = matches();

fn highest(mask: u16) -> Option<i32> {
    (mask != 0).then(|| (u16::BITS - 1 - mask.leading_zeros()) as i32)
}

fn pair_at_most(tens: u16, units: u16, bound: i32) -> Option<i32> {
    if bound < 0 {
        return None;
    }
    let high = bound / RADIX;
    if tens & (1 << high) != 0 {
        let allowed_units = (1 << (bound % RADIX + 1)) - 1;
        if let Some(low) = highest(units & allowed_units) {
            return Some(high * RADIX + low);
        }
    }
    // A smaller tens digit lets the units digit take its maximum.
    let lower_tens = (1 << high) - 1;
    Some(highest(tens & lower_tens)? * RADIX + highest(units)?)
}

fn solve(data: &[u8]) -> c_int {
    let mut tokens = data
        .split(|byte| byte.is_ascii_whitespace())
        .filter(|token| !token.is_empty());
    let count = tokens
        .next()
        .unwrap()
        .iter()
        .fold(0_usize, |count, &digit| {
            count * RADIX as usize + usize::from(digit - b'0')
        });
    let mut output = [0; MAX_READINGS * OUTPUT_WIDTH];
    let mut bound = MINUTES * SECONDS - 1;
    for answer in output[..count * OUTPUT_WIDTH].chunks_exact_mut(OUTPUT_WIDTH) {
        let mut lit = [0; COLUMNS.len()];
        for row in 0..WIDTH {
            let line = tokens.next().unwrap();
            for (digit, &start) in COLUMNS.iter().enumerate() {
                for cell in 0..WIDTH {
                    if line[start + cell] != b'.' {
                        lit[digit] |= 1 << (row * WIDTH + cell);
                    }
                }
            }
        }
        let [m_tens, m_units, s_tens, s_units] = lit.map(|pattern| MATCHES[pattern]);
        let mut minute = pair_at_most(m_tens, m_units, bound / SECONDS).unwrap();
        let mut second = pair_at_most(s_tens, s_units, SECONDS - 1).unwrap();
        if minute == bound / SECONDS && second > bound % SECONDS {
            if let Some(reduced) = pair_at_most(s_tens, s_units, bound % SECONDS) {
                second = reduced;
            } else {
                minute = pair_at_most(m_tens, m_units, minute - 1).unwrap();
            }
        }
        answer.copy_from_slice(&[
            b'0' + (minute / RADIX) as u8,
            b'0' + (minute % RADIX) as u8,
            b':',
            b'0' + (second / RADIX) as u8,
            b'0' + (second % RADIX) as u8,
            b'\n',
        ]);
        bound = minute * SECONDS + second - 1;
    }
    send(&output[..count * OUTPUT_WIDTH])
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let mut block = [0; INPUT_SIZE];
    let Some(filled) = read_into(&mut block) else {
        return 1;
    };
    if filled < block.len() {
        return solve(&block[..filled]);
    }

    // Handle inputs padded with more whitespace than the stack buffer holds.
    let mut data = block.to_vec();
    loop {
        let Some(filled) = read_into(&mut block) else {
            return 1;
        };
        data.extend_from_slice(&block[..filled]);
        if filled < block.len() {
            return solve(&data);
        }
    }
}
