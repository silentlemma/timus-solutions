#![no_main]

use std::io;

const INF: i32 = 1 << 30;

fn solve_entry() {
    let input = TokenInput::new();
    let mut it = input.into_iter().map(|x| parse_integer::<i64>(x));
    let (n, m) = (it.next().unwrap() as usize, it.next().unwrap() as usize);
    let mut w = vec![vec![INF; n]; n];
    let mut edges = Vec::with_capacity(m);
    for _ in 0..m {
        let a = it.next().unwrap() as usize - 1;
        let b = it.next().unwrap() as usize - 1;
        let c = it.next().unwrap() as i32;
        w[a][b] = c;
        w[b][a] = c;
        edges.push((a as u32, b as u32, c));
    }
    // Prim on the matrix; heaviest[u][v] is the heaviest tree edge between u and v
    let mut heaviest = vec![vec![0i32; n]; n];
    let mut in_tree = vec![vec![false; n]; n];
    let mut dist = w[0].clone();
    let mut parent = vec![0usize; n];
    let mut done = vec![false; n];
    done[0] = true;
    let mut order = vec![0usize];
    let mut total = 0i64;
    for _ in 1..n {
        let v = (0..n)
            .filter(|&u| !done[u])
            .min_by_key(|&u| dist[u])
            .unwrap();
        let (p, c) = (parent[v], dist[v]);
        total += i64::from(c);
        in_tree[p][v] = true;
        in_tree[v][p] = true;
        for &u in &order {
            let h = heaviest[p][u].max(c);
            heaviest[u][v] = h;
            heaviest[v][u] = h;
        }
        done[v] = true;
        order.push(v);
        for u in 0..n {
            if !done[u] && w[v][u] < dist[u] {
                dist[u] = w[v][u];
                parent[u] = v;
            }
        }
    }
    // the next tree swaps one outside edge for the heaviest edge on its tree path
    let swap = edges
        .iter()
        .filter(|&&(a, b, _)| !in_tree[a as usize][b as usize])
        .map(|&(a, b, c)| c - heaviest[a as usize][b as usize])
        .min();
    println!("Cost: {}", total);
    println!("Cost: {}", swap.map_or(-1, |s| total + i64::from(s)));
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
const INLINE_TOKEN_BYTES: usize = 32;

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
    inline: [u8; INLINE_TOKEN_BYTES],
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
            inline: [0; INLINE_TOKEN_BYTES],
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
