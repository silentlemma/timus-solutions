#![no_main]

use std::collections::VecDeque;
use std::io;

const UNMATCHED: usize = usize::MAX;

struct Matcher {
    edges: Vec<Vec<u16>>,
    left: Vec<usize>,
    right: Vec<usize>,
    distance: Vec<usize>,
    cursor: Vec<usize>,
    shortest: usize,
}

impl Matcher {
    fn new(edges: Vec<Vec<u16>>) -> Self {
        let count = edges.len();
        Self {
            edges,
            left: vec![UNMATCHED; count],
            right: vec![UNMATCHED; count],
            distance: vec![UNMATCHED; count],
            cursor: vec![0; count],
            shortest: 0,
        }
    }

    fn layer(&mut self) -> bool {
        let count = self.edges.len();
        self.shortest = count + 1;
        self.distance.fill(UNMATCHED);
        self.cursor.fill(0);
        let mut queue = VecDeque::new();
        for u in 0..count {
            if self.left[u] == UNMATCHED {
                self.distance[u] = 0;
                queue.push_back(u);
            }
        }
        while let Some(u) = queue.pop_front() {
            if self.distance[u] >= self.shortest {
                continue;
            }
            for &v in &self.edges[u] {
                let v = v as usize;
                let mate = self.right[v];
                if mate == UNMATCHED {
                    self.shortest = self.distance[u] + 1;
                } else if self.distance[mate] == UNMATCHED {
                    self.distance[mate] = self.distance[u] + 1;
                    queue.push_back(mate);
                }
            }
        }
        self.shortest <= count
    }

    fn augment(&mut self, u: usize) -> bool {
        while self.cursor[u] < self.edges[u].len() {
            let v = self.edges[u][self.cursor[u]] as usize;
            self.cursor[u] += 1;
            let mate = self.right[v];
            if (mate == UNMATCHED && self.distance[u] + 1 == self.shortest)
                || (mate != UNMATCHED
                    && self.distance[mate] == self.distance[u] + 1
                    && self.augment(mate))
            {
                self.left[u] = v;
                self.right[v] = u;
                return true;
            }
        }
        self.distance[u] = UNMATCHED;
        false
    }
}

fn solve(a: i64, b: i64, records: &[(i64, i64)]) -> Option<Vec<(i64, i64)>> {
    let entries: Vec<i64> = records.iter().filter(|r| r.1 == 0).map(|r| r.0).collect();
    let exits: Vec<i64> = records.iter().filter(|r| r.1 == 1).map(|r| r.0).collect();
    if entries.len() != exits.len() {
        return None;
    }
    let count = entries.len();
    let mut edges = vec![Vec::new(); count];
    for (u, &entry) in entries.iter().enumerate() {
        for (v, &exit) in exits.iter().enumerate() {
            let duration = exit - entry;
            if duration > 0 && (duration <= b || duration >= a) {
                edges[u].push(v as u16);
            }
        }
    }
    let mut h = Matcher::new(edges);
    let mut total = 0;
    while h.layer() {
        for u in 0..count {
            if h.left[u] == UNMATCHED && h.augment(u) {
                total += 1;
            }
        }
    }
    if total != count {
        return None;
    }
    Some(
        entries
            .iter()
            .enumerate()
            .map(|(u, &entry)| (entry, exits[h.left[u]]))
            .collect(),
    )
}

fn solve_entry() {
    let input = TokenInput::new();
    let mut tokens = input.into_iter();
    let a: i64 = parse_integer(tokens.next().unwrap());
    let b: i64 = parse_integer(tokens.next().unwrap());
    let n: usize = parse_integer(tokens.next().unwrap());
    let records: Vec<(i64, i64)> = (0..n)
        .map(|_| {
            (
                parse_integer(tokens.next().unwrap()),
                parse_integer(tokens.next().unwrap()),
            )
        })
        .collect();
    match solve(a, b, &records) {
        None => println!("Liar"),
        Some(answer) => {
            let mut output = String::from("No reason\n");
            for (entry, exit) in answer {
                output.push_str(&format!("{} {}\n", entry, exit));
            }
            print!("{}", output);
        }
    }
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

const INPUT_BUFFER_BYTES: usize = 4096;

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn input_read(fd: i32, data: *mut u8, size: u32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "read"]
    fn input_read(fd: i32, data: *mut u8, size: usize) -> isize;
}

struct TokenInput {
    buffer: [u8; INPUT_BUFFER_BYTES],
    position: usize,
    length: usize,
}

impl TokenInput {
    fn new() -> Self {
        Self {
            buffer: [0; INPUT_BUFFER_BYTES],
            position: 0,
            length: 0,
        }
    }

    fn byte(&mut self) -> Option<u8> {
        if self.position == self.length {
            loop {
                // SAFETY: the live writable array is passed with its exact bounded length.
                let count = unsafe {
                    #[cfg(windows)]
                    {
                        input_read(0, self.buffer.as_mut_ptr(), INPUT_BUFFER_BYTES as u32)
                    }
                    #[cfg(not(windows))]
                    {
                        input_read(0, self.buffer.as_mut_ptr(), INPUT_BUFFER_BYTES)
                    }
                };
                if count > 0 {
                    self.position = 0;
                    self.length = count as usize;
                    break;
                }
                if count == 0 {
                    return None;
                }
                let error = io::Error::last_os_error();
                if error.kind() != io::ErrorKind::Interrupted {
                    panic!("stdin read failed: {error}");
                }
            }
        }
        let byte = self.buffer[self.position];
        self.position += 1;
        Some(byte)
    }
}

struct InputWord {
    inline: [u8; 32],
    length: usize,
    spill: Vec<u8>,
}

impl InputWord {
    #[inline]
    fn push(&mut self, byte: u8) {
        if self.length < self.inline.len() {
            self.inline[self.length] = byte;
        } else {
            if self.spill.is_empty() {
                self.spill.extend_from_slice(&self.inline);
            }
            self.spill.push(byte);
        }
        self.length += 1;
    }
}

impl AsRef<[u8]> for InputWord {
    fn as_ref(&self) -> &[u8] {
        if self.length <= self.inline.len() {
            &self.inline[..self.length]
        } else {
            &self.spill
        }
    }
}

impl std::ops::Deref for InputWord {
    type Target = str;
    fn deref(&self) -> &str {
        std::str::from_utf8(self.as_ref()).unwrap()
    }
}

impl PartialEq<&str> for InputWord {
    fn eq(&self, other: &&str) -> bool {
        self.as_ref() == other.as_bytes()
    }
}

impl Iterator for TokenInput {
    type Item = InputWord;
    #[inline]
    fn next(&mut self) -> Option<InputWord> {
        let mut first = self.byte()?;
        while first.is_ascii_whitespace() {
            first = self.byte()?;
        }
        let mut word = InputWord {
            inline: [0; 32],
            length: 0,
            spill: Vec::new(),
        };
        word.push(first);
        while let Some(byte) = self.byte() {
            if byte.is_ascii_whitespace() {
                break;
            }
            word.push(byte);
        }
        Some(word)
    }
}

// Run the algorithm directly and flush Rust's global output before returning to C.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    solve_entry();
    std::io::Write::flush(&mut std::io::stdout()).unwrap();
    0
}
