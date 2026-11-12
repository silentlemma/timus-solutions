#![no_main]

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn system_read(fd: i32, buffer: *mut u8, length: u32) -> i32;
    #[link_name = "_write"]
    fn system_write(fd: i32, buffer: *const u8, length: u32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "read"]
    fn system_read(fd: i32, buffer: *mut u8, length: usize) -> isize;
    #[link_name = "write"]
    fn system_write(fd: i32, buffer: *const u8, length: usize) -> isize;
}

fn read_input(buffer: &mut [u8]) -> usize {
    // SAFETY: the writable slice stays live for the call, and its length is bounded by INPUT_SIZE.
    // Both CRT _read and POSIX read write no more than the supplied length.
    let count = unsafe {
        #[cfg(windows)]
        {
            system_read(0, buffer.as_mut_ptr(), buffer.len() as u32)
        }
        #[cfg(not(windows))]
        {
            system_read(0, buffer.as_mut_ptr(), buffer.len())
        }
    };
    if count > 0 {
        count as usize
    } else {
        0
    }
}

fn write_all(mut buffer: &[u8]) -> bool {
    while !buffer.is_empty() {
        // SAFETY: this live slice contains at most OUTPUT_SIZE readable bytes.
        // Both write functions access at most the specified length and return a byte count.
        let count = unsafe {
            #[cfg(windows)]
            {
                system_write(1, buffer.as_ptr(), buffer.len() as u32)
            }
            #[cfg(not(windows))]
            {
                system_write(1, buffer.as_ptr(), buffer.len())
            }
        };
        if count <= 0 {
            return false;
        }
        buffer = &buffer[count as usize..];
    }
    true
}

const INPUT_SIZE: usize = 8192;

struct Input {
    bytes: [u8; INPUT_SIZE],
    position: usize,
    length: usize,
}

impl Input {
    fn new() -> Self {
        Self {
            bytes: [0; INPUT_SIZE],
            position: 0,
            length: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.position == self.length {
            self.length = read_input(&mut self.bytes);
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let value = self.bytes[self.position];
        self.position += 1;
        value
    }
    fn number(&mut self) -> i32 {
        let mut c = self.byte();
        while c != 0 && c <= b' ' {
            c = self.byte();
        }
        let sign = if c == b'-' {
            c = self.byte();
            -1
        } else {
            1
        };
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + i32::from(c - b'0');
            c = self.byte();
        }
        sign * value
    }
}

const MAX_PLAYERS: usize = 1000;
const SCORES: usize = 7;
const TEAMS: usize = 2;
const OUTPUT_SIZE: usize = 10000;

fn take(
    head: &mut [[u16; SCORES]; TEAMS],
    next: &[[u16; MAX_PLAYERS + 1]; TEAMS],
    team: usize,
    score: &mut i32,
    step: i32,
) -> usize {
    while head[team][*score as usize] == 0 {
        *score += step;
    }
    let bucket = *score as usize;
    let id = head[team][bucket] as usize;
    head[team][bucket] = next[team][id];
    id
}

fn append_number(mut value: usize, output: &mut [u8], used: &mut usize) {
    const MAX_DIGITS: usize = 4;
    let mut digits = [0_u8; MAX_DIGITS];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] = b'0' + (value % 10) as u8;
        value /= 10;
        if value == 0 {
            break;
        }
    }
    for &digit in &digits[first..] {
        output[*used] = digit;
        *used += 1;
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input::new();
    let n = input.number() as usize;
    let mut head = [[0_u16; SCORES]; TEAMS];
    let mut next = [[0_u16; MAX_PLAYERS + 1]; TEAMS];
    let mut totals = [0_i32; TEAMS];
    for team in 0..TEAMS {
        for id in 1..=n {
            let score = input.number() as usize;
            totals[team] += score as i32;
            next[team][id] = head[team][score];
            head[team][score] = id as u16;
        }
    }
    let mut step = [1_i32; TEAMS];
    let mut score = [0_i32; TEAMS];
    if totals[0] > totals[1] {
        step[1] = -1;
        score[1] = (SCORES - 1) as i32;
    } else if totals[0] < totals[1] {
        step[0] = -1;
        score[0] = (SCORES - 1) as i32;
    }
    let mut output = [0_u8; OUTPUT_SIZE];
    let mut used = 0;
    for _ in 0..n {
        let first = take(&mut head, &next, 0, &mut score[0], step[0]);
        let second = take(&mut head, &next, 1, &mut score[1], step[1]);
        append_number(first, &mut output, &mut used);
        output[used] = b' ';
        used += 1;
        append_number(second, &mut output, &mut used);
        output[used] = b'\n';
        used += 1;
    }
    if write_all(&output[..used]) {
        0
    } else {
        1
    }
}
