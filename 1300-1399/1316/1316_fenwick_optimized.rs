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

const INPUT_SIZE: usize = 256;

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
    fn word(&mut self) -> u8 {
        let mut c = self.byte();
        while c != 0 && c <= b' ' {
            c = self.byte();
        }
        let first = c;
        while c > b' ' {
            c = self.byte();
        }
        first
    }
    fn price(&mut self) -> i32 {
        let mut c = self.byte();
        while c != 0 && c <= b' ' {
            c = self.byte();
        }
        let mut whole = 0;
        while c.is_ascii_digit() {
            whole = whole * 10 + i32::from(c - b'0');
            c = self.byte();
        }
        let (mut fraction, mut digits) = (0, 0);
        if c == b'.' {
            c = self.byte();
            while c.is_ascii_digit() {
                fraction = fraction * 10 + i32::from(c - b'0');
                digits += 1;
                c = self.byte();
            }
        }
        while digits < DECIMAL_PLACES {
            fraction *= 10;
            digits += 1;
        }
        whole * CENTS + fraction
    }
}

const OUTPUT_SIZE: usize = 64;
const MAX_DIGITS: usize = 20;

fn write_number(output: &mut [u8], used: &mut usize, mut value: usize) {
    let mut digits = [0; MAX_DIGITS];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] = b'0' + (value % 10) as u8;
        value /= 10;
        if value == 0 {
            break;
        }
    }
    let count = digits.len() - first;
    output[*used..*used + count].copy_from_slice(&digits[first..]);
    *used += count;
}

const MAX_OPERATIONS: usize = 100000;
const CENTS: i32 = 100;
const DECIMAL_PLACES: i32 = 2;
const BID: i32 = -1;
const DEL: i32 = -2;

struct Operation {
    price: i32,
    amount: i32,
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input::new();
    let mut operations = Vec::with_capacity(MAX_OPERATIONS);
    let mut prices = Vec::with_capacity(MAX_OPERATIONS);
    loop {
        let command = input.word();
        if command == b'Q' || command == 0 {
            break;
        }
        let price = input.price();
        let amount = match command {
            b'B' => {
                prices.push(price);
                BID
            }
            b'D' => DEL,
            _ => input.number(),
        };
        operations.push(Operation { price, amount });
    }
    prices.sort_unstable();
    prices.dedup();
    let mut tree = vec![0i32; prices.len() + 1];
    let mut active = 0;
    let mut revenue = 0i64;
    for operation in operations {
        let mut index = prices.partition_point(|&value| value < operation.price);
        if operation.amount < 0 {
            let delta = if operation.amount == BID { 1 } else { -1 };
            active += delta;
            index += 1;
            while index < tree.len() {
                tree[index] += delta;
                index += index & index.wrapping_neg();
            }
        } else {
            // lower_bound counts only strictly cheaper bids, never equal-price bids.
            let mut cheaper = 0;
            while index > 0 {
                cheaper += tree[index];
                index &= index - 1;
            }
            revenue += i64::from(operation.amount.min(active - cheaper));
        }
    }
    let mut output = [0u8; OUTPUT_SIZE];
    let mut used = 0;
    write_number(
        &mut output,
        &mut used,
        (revenue / i64::from(CENTS)) as usize,
    );
    output[used] = b'.';
    used += 1;
    output[used] = b'0' + (revenue % i64::from(CENTS) / 10) as u8;
    used += 1;
    output[used] = b'0' + (revenue % 10) as u8;
    used += 1;
    output[used] = b'\n';
    used += 1;
    if write_all(&output[..used]) {
        0
    } else {
        1
    }
}
