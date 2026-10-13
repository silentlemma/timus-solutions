use std::fmt::Write as _;
use std::io::{self, Read, Write};

const NONE: i64 = -1; // no term starts here
const BASE: i64 = 10;

struct Parser<'a> {
    s: &'a [u8],
    pos: usize,
}

impl Parser<'_> {
    fn accept(&mut self, c: u8) -> bool {
        if self.pos < self.s.len() && self.s[self.pos] == c {
            self.pos += 1;
            return true;
        }
        false
    }

    fn digit_at(&self, i: usize) -> bool {
        i < self.s.len() && self.s[i].is_ascii_digit()
    }

    // a number, an operation with its arguments, or a bracket
    fn term(&mut self) -> i64 {
        if self.digit_at(self.pos) {
            let mut v: i64 = 0;
            while self.digit_at(self.pos) {
                v = v.wrapping_mul(BASE) + i64::from(self.s[self.pos] - b'0');
                self.pos += 1;
            }
            return v;
        }
        for sign in [b'+', b'*', b'/'] {
            if self.accept(sign) {
                return self.fold(sign);
            }
        }
        if self.accept(b'(') {
            let x = self.glue(false);
            self.accept(b')');
            return x;
        }
        NONE
    }

    // the arguments of an operation are glued terms split by ';'
    fn fold(&mut self, sign: u8) -> i64 {
        let mut a = self.glue(true);
        while self.accept(b';') {
            let b = self.glue(true);
            a = match sign {
                b'+' => a.wrapping_add(b),
                b'*' => a.wrapping_mul(b),
                _ if b == 0 => 0,
                _ => a / b,
            };
        }
        a
    }

    // terms one after another are glued as decimal strings; inside an
    // operation ';' ends the argument, elsewhere it glues the whole rest,
    // and a missing term counts as 1
    fn glue(&mut self, inside: bool) -> i64 {
        let mut parts = Vec::new();
        let mut x = self.term();
        while x != NONE || parts.is_empty() {
            parts.push(x);
            if self.pos < self.s.len() && self.s[self.pos] == b';' {
                if inside {
                    break;
                }
                self.pos += 1;
                let rest = self.glue(false);
                parts.push(rest);
            }
            x = self.term();
        }
        let text: String = parts.iter().map(|x| x.unsigned_abs().to_string()).collect();
        // a glued number that does not fit is cut to the largest one
        text.parse().unwrap_or(i64::MAX)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut out = String::new();
    for (i, line) in input.lines().enumerate() {
        let mut p = Parser {
            s: line.as_bytes(),
            pos: 0,
        };
        let value = p.glue(false);
        writeln!(out, "Expression {} evaluates to: {}", i + 1, value).unwrap();
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
