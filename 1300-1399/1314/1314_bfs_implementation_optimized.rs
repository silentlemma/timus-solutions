#![no_main]

use std::collections::VecDeque;
use std::io::{self, Write};

const IDS: usize = 32768; // station indices go up to 32767

struct Graph {
    head: Vec<i32>,
    target: Vec<u16>,
    next: Vec<i32>,
}

impl Graph {
    fn new() -> Self {
        Self {
            head: vec![-1; IDS],
            target: Vec::new(),
            next: Vec::new(),
        }
    }
    fn add(&mut self, from: usize, to: usize) {
        self.target.push(to as u16);
        self.next.push(self.head[from]);
        self.head[from] = self.target.len() as i32 - 1;
    }
    fn neighbours(&self, from: usize) -> impl Iterator<Item = usize> + '_ {
        let mut edge = self.head[from];
        std::iter::from_fn(move || {
            if edge < 0 {
                return None;
            }
            let target = self.target[edge as usize] as usize;
            edge = self.next[edge as usize];
            Some(target)
        })
    }
}

fn bfs(adj: &Graph, start: usize) -> Vec<i32> {
    let mut dist = vec![-1i32; IDS];
    let mut queue = VecDeque::new();
    dist[start] = 0;
    queue.push_back(start);
    while let Some(u) = queue.pop_front() {
        for v in adj.neighbours(u) {
            if dist[v] < 0 {
                dist[v] = dist[u] + 1;
                queue.push_back(v);
            }
        }
    }
    dist
}

fn solve_entry() {
    let input = TokenInput::new();
    let mut it = input.into_iter().map(|t| parse_integer::<i64>(t));
    let mut adj = Graph::new();
    let mut present = vec![false; IDS];
    let n = it.next().unwrap();
    for _ in 0..n {
        let k = it.next().unwrap();
        let line: Vec<usize> = (0..k).map(|_| it.next().unwrap() as usize).collect();
        for &s in &line {
            present[s] = true;
        }
        for pair in line.windows(2) {
            adj.add(pair[0], pair[1]);
            adj.add(pair[1], pair[0]);
        }
    }
    let m = it.next().unwrap();
    let seen: Vec<i64> = (0..m).map(|_| it.next().unwrap()).collect();
    // the stations seen must be a walk through the network ...
    for (i, &s) in seen.iter().enumerate() {
        if s < 0 || s as usize >= IDS || !present[s as usize] {
            return;
        }
        if i > 0
            && !adj
                .neighbours(seen[i - 1] as usize)
                .any(|v| v == s as usize)
        {
            return;
        }
    }
    let (start, end) = (seen[0] as usize, seen[seen.len() - 1] as usize);
    let first = bfs(&adj, start);
    // ... and a shortest one, or no target fits it
    if first[end] != (m - 1) as i32 {
        return;
    }
    let last = bfs(&adj, end);
    let mut out = io::BufWriter::new(io::stdout().lock());
    // a target fits when the walk can go on to it along a shortest path
    for t in 0..IDS {
        if first[t] >= 0 && last[t] >= 0 && first[t] == (m - 1) as i32 + last[t] {
            writeln!(out, "{}", t).unwrap();
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
