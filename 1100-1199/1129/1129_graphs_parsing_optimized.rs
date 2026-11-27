use std::collections::{HashMap, VecDeque};
use std::io;

fn main() {
    let input = TokenInput::new();
    let mut tok = input.into_iter().map(|t| parse_integer::<usize>(t));
    let n = tok.next().unwrap();
    let rows: Vec<Vec<usize>> = (0..n)
        .map(|_| {
            let k = tok.next().unwrap();
            (0..k).map(|_| tok.next().unwrap() - 1).collect()
        })
        .collect();
    // Pair consecutive mentions of each unordered room pair in scan order.
    // Same-room pairs are balanced G/Y loops; an odd remainder connects rooms.
    // Parallel doors are interchangeable; self-door mentions pair in their row.
    let mut ends: Vec<[(usize, usize); 2]> = Vec::new();
    let mut waiting: HashMap<(usize, usize), VecDeque<usize>> = HashMap::new();
    for u in 0..n {
        for (i, &v) in rows[u].iter().enumerate() {
            let queue = waiting.entry((u.min(v), u.max(v))).or_default();
            if let Some(e) = queue.pop_front() {
                ends[e][1] = (u, i);
            } else {
                queue.push_back(ends.len());
                ends.push([(u, i), (usize::MAX, 0)]);
            }
        }
    }
    drop(waiting);
    // a dummy room joined to every room of odd degree makes all degrees even
    let dummy = n;
    let mut edges = ends.len();
    let mut adj: Vec<Vec<(usize, usize)>> = vec![Vec::new(); n + 1];
    for (e, pair) in ends.iter().enumerate() {
        let (u, v) = (pair[0].0, pair[1].0);
        adj[u].push((v, e));
        adj[v].push((u, e));
    }
    for u in 0..n {
        if adj[u].len() % 2 == 1 {
            adj[u].push((dummy, edges));
            adj[dummy].push((u, edges));
            edges += 1;
        }
    }
    // walk Euler circuits and orient each door along the walk
    let mut used = vec![false; edges];
    let mut tail = vec![0; edges];
    let mut ptr = vec![0; n + 1];
    for start in 0..=n {
        let mut stack = vec![start];
        while let Some(&u) = stack.last() {
            while ptr[u] < adj[u].len() && used[adj[u][ptr[u]].1] {
                ptr[u] += 1;
            }
            if ptr[u] == adj[u].len() {
                stack.pop();
                continue;
            }
            let (v, e) = adj[u][ptr[u]];
            used[e] = true;
            tail[e] = u;
            stack.push(v);
        }
    }
    let mut colours: Vec<Vec<u8>> = rows.iter().map(|r| vec![b' '; r.len()]).collect();
    for (e, &[(ua, ia), (ub, ib)]) in ends.iter().enumerate() {
        // green on the side the walk leaves from, orange where it enters
        let out_first = tail[e] == ua;
        colours[ua][ia] = if out_first { b'G' } else { b'Y' };
        colours[ub][ib] = if out_first { b'Y' } else { b'G' };
    }
    let mut output = String::new();
    for row in colours {
        for (i, colour) in row.into_iter().enumerate() {
            if i != 0 {
                output.push(' ');
            }
            output.push(colour as char);
        }
        output.push('\n');
    }
    print!("{}", output);
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
