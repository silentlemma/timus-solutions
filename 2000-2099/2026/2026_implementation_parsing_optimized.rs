#![no_main]

fn solve(pattern: &str, limit: usize) -> String {
    const ALPHABET: usize = 26;
    let mut fixed = [false; ALPHABET + 1];
    let mut positive = Vec::new();
    let mut negative = Vec::new();
    for (index, letter) in pattern.bytes().enumerate() {
        if letter != b'?' {
            fixed[(letter - b'a' + 1) as usize] = true;
        } else if index % 2 == 0 {
            if positive.len() < ALPHABET {
                positive.push(index);
            }
        } else {
            if negative.len() < ALPHABET {
                negative.push(index);
            }
        }
    }
    let fixed_count = fixed.iter().filter(|&&used| used).count();
    let needed = limit.saturating_sub(fixed_count);
    if positive.len() + negative.len() < needed {
        return "-1".to_string();
    }
    let missing: Vec<usize> = (1..=ALPHABET).filter(|&value| !fixed[value]).collect();
    let count = missing.len();
    let mut low = vec![0; count + 1];
    let mut high = vec![0; count + 1];
    for index in 0..count {
        low[index + 1] = low[index] + missing[index] - 1;
        high[index + 1] = high[index] + ALPHABET - missing[count - 1 - index];
    }
    let lower = needed.saturating_sub(negative.len());
    let upper = needed.min(positive.len());
    let mut best_cost = ALPHABET * ALPHABET;
    let mut chosen = 0;
    for take in lower..=upper {
        let cost = high[take] + low[needed - take];
        if cost < best_cost {
            best_cost = cost;
            chosen = take;
        }
    }
    let mut answer: Vec<u8> = pattern
        .bytes()
        .enumerate()
        .map(|(i, c)| {
            if c != b'?' {
                c
            } else if i % 2 == 0 {
                b'z'
            } else {
                b'a'
            }
        })
        .collect();
    for index in 0..chosen {
        answer[positive[index]] = b'a' + (missing[count - 1 - index] - 1) as u8;
    }
    for index in 0..needed - chosen {
        answer[negative[index]] = b'a' + (missing[index] - 1) as u8;
    }
    String::from_utf8(answer).unwrap()
}

fn solve_entry() {
    let input = String::from_utf8(native_read_all()).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let pattern = tokens.next().unwrap();
    let limit = parse_integer(tokens.next().unwrap());
    let answer = solve(&pattern, limit);
    native_write_all(answer.as_bytes());
    native_write_all(b"\n");
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.
fn parse_integer<T>(word: impl AsRef<[u8]>) -> T
where
    T: From<u8> + std::ops::Add<Output = T> + std::ops::Sub<Output = T> + std::ops::Mul<Output = T>,
{
    let digits = word.as_ref();
    let negative = digits[0] == b'-';
    let start = usize::from(negative || digits[0] == b'+');
    let mut value = T::from(0);
    for &byte in &digits[start..] {
        let digit = T::from(byte - b'0');
        let scaled = value * T::from(10);
        value = if negative {
            scaled - digit
        } else {
            scaled + digit
        };
    }
    value
}

// Return after all native output writes have completed.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    native_setup();
    solve_entry();
    0
}

const NATIVE_INPUT_BYTES: usize = 4096;

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn native_read(fd: i32, data: *mut u8, size: u32) -> i32;
    #[link_name = "_write"]
    fn native_write(fd: i32, data: *const u8, size: u32) -> i32;
    fn _setmode(fd: i32, mode: i32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "read"]
    fn native_read(fd: i32, data: *mut u8, size: usize) -> isize;
    #[link_name = "write"]
    fn native_write(fd: i32, data: *const u8, size: usize) -> isize;
}

fn native_setup() {
    #[cfg(windows)]
    {
        const BINARY_MODE: i32 = 0x8000;
        // SAFETY: descriptors zero/one are the inherited standard streams.
        unsafe {
            assert!(_setmode(0, BINARY_MODE) != -1);
            assert!(_setmode(1, BINARY_MODE) != -1);
        }
    }
}

fn native_read_all() -> Vec<u8> {
    let mut data = Vec::new();
    let mut block = [0_u8; NATIVE_INPUT_BYTES];
    loop {
        // SAFETY: the live writable array is passed with its bounded exact size.
        let count = unsafe {
            #[cfg(windows)]
            {
                native_read(0, block.as_mut_ptr(), block.len() as u32)
            }
            #[cfg(not(windows))]
            {
                native_read(0, block.as_mut_ptr(), block.len())
            }
        };
        if count == 0 {
            break;
        }
        if count < 0 {
            #[cfg(not(windows))]
            if std::io::Error::last_os_error().kind() == std::io::ErrorKind::Interrupted {
                continue;
            }
            panic!("input read failed");
        }
        data.extend_from_slice(&block[..count as usize]);
    }
    data
}

fn native_write_all(mut data: &[u8]) {
    while !data.is_empty() {
        // SAFETY: the live readable slice is bounded by the documented output size.
        let count = unsafe {
            #[cfg(windows)]
            {
                native_write(1, data.as_ptr(), data.len() as u32)
            }
            #[cfg(not(windows))]
            {
                native_write(1, data.as_ptr(), data.len())
            }
        };
        if count < 0 {
            #[cfg(not(windows))]
            if std::io::Error::last_os_error().kind() == std::io::ErrorKind::Interrupted {
                continue;
            }
            panic!("output write failed");
        }
        assert!(count > 0);
        data = &data[count as usize..];
    }
}
