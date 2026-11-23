use std::io::{self, Read, Write};

struct Input<'a> {
    data: &'a [u8],
    position: usize,
}

impl<'a> Input<'a> {
    fn word(&mut self) -> &'a [u8] {
        while self.position < self.data.len() && self.data[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let start = self.position;
        while self.position < self.data.len() && !self.data[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        &self.data[start..self.position]
    }

    fn number(&mut self) -> u64 {
        self.word()
            .iter()
            .fold(0, |value, &digit| value * 10 + u64::from(digit - b'0'))
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Input {
        data: &data,
        position: 0,
    };
    let first = input.number();
    let second = input.number();
    // on night k the thief tries code k on lock 1 when k is even and on
    // lock 2 when k is odd
    let answer: &[u8] = if first % 2 == 0 || second % 2 == 1 {
        b"yes\n"
    } else {
        b"no\n"
    };
    io::stdout().lock().write_all(answer).unwrap();
}
