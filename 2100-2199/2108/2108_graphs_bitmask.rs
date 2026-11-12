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

const WORD_BITS: usize = 64;
const OUTPUT_SIZE: usize = 1001;

impl Input {
    fn digit(&mut self) -> bool {
        let mut c = self.byte();
        while c != 0 && c <= b' ' {
            c = self.byte();
        }
        c == b'1'
    }
}

struct Closure {
    added: Vec<u64>,
    owned: Vec<u64>,
    queue: Vec<u16>,
    words: usize,
}

impl Closure {
    fn give(&mut self, word: usize, figures: u64) {
        let mut fresh = figures & !self.owned[word];
        self.owned[word] |= figures;
        while fresh != 0 {
            self.queue
                .push((word * WORD_BITS + fresh.trailing_zeros() as usize) as u16);
            fresh &= fresh - 1;
        }
    }
    fn fire(&mut self, rule: usize) {
        for word in 0..self.words {
            self.give(word, self.added[rule * self.words + word]);
        }
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input::new();
    let n = input.number() as usize;
    let m = input.number() as usize;
    let words = (n + WORD_BITS - 1) / WORD_BITS;
    let rule_words = (m + WORD_BITS - 1) / WORD_BITS;
    let mut needs = vec![0_u64; n * rule_words];
    let mut remaining = vec![0_u16; m];
    let mut closure = Closure {
        added: vec![0; m * words],
        owned: vec![0; words],
        queue: Vec::with_capacity(n),
        words,
    };
    for rule in 0..m {
        for figure in 0..n {
            if input.digit() {
                needs[figure * rule_words + rule / WORD_BITS] |= 1_u64 << (rule % WORD_BITS);
                remaining[rule] += 1;
            }
        }
        for figure in 0..n {
            if input.digit() {
                closure.added[rule * words + figure / WORD_BITS] |= 1_u64 << (figure % WORD_BITS);
            }
        }
    }
    for figure in 0..n {
        if input.digit() {
            closure.give(figure / WORD_BITS, 1_u64 << (figure % WORD_BITS));
        }
    }
    for (rule, &count) in remaining.iter().enumerate() {
        if count == 0 {
            closure.fire(rule);
        }
    }
    let mut head = 0;
    while head < closure.queue.len() {
        let figure = closure.queue[head] as usize;
        head += 1;
        for word in 0..rule_words {
            let mut rules = needs[figure * rule_words + word];
            while rules != 0 {
                let rule = word * WORD_BITS + rules.trailing_zeros() as usize;
                remaining[rule] -= 1;
                if remaining[rule] == 0 {
                    closure.fire(rule);
                }
                rules &= rules - 1;
            }
        }
    }
    let mut output = [0_u8; OUTPUT_SIZE];
    for (figure, byte) in output[..n].iter_mut().enumerate() {
        *byte = b'0' + ((closure.owned[figure / WORD_BITS] >> (figure % WORD_BITS)) & 1) as u8;
    }
    output[n] = b'\n';
    if write_all(&output[..n + 1]) {
        0
    } else {
        1
    }
}
