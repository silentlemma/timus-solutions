use std::io::{self, Read, Write};

// fixed arrays and small buffers only: the memory limit is half a megabyte
const MAXN: usize = 1000;
const BUFFER: usize = 1 << 12;
const DIGITS: usize = 20;
const BASE: u64 = 10;

struct Input {
    buf: [u8; BUFFER],
    len: usize,
    pos: usize,
}

impl Input {
    // the next byte, or 0 at the end of the input
    fn byte(&mut self) -> u8 {
        if self.pos == self.len {
            self.len = io::stdin().lock().read(&mut self.buf).unwrap_or(0);
            self.pos = 0;
            if self.len == 0 {
                return 0;
            }
        }
        self.pos += 1;
        self.buf[self.pos - 1]
    }

    fn number(&mut self) -> i64 {
        let mut c = self.byte();
        while !c.is_ascii_digit() {
            c = self.byte();
        }
        let mut v = 0;
        while c.is_ascii_digit() {
            v = v * BASE as i64 + i64::from(c - b'0');
            c = self.byte();
        }
        v
    }
}

struct Output {
    buf: [u8; BUFFER],
    len: usize,
}

impl Output {
    fn flush(&mut self) {
        io::stdout()
            .lock()
            .write_all(&self.buf[..self.len])
            .unwrap();
        self.len = 0;
    }

    fn bytes(&mut self, s: &[u8]) {
        if self.len + s.len() > BUFFER {
            self.flush();
        }
        self.buf[self.len..self.len + s.len()].copy_from_slice(s);
        self.len += s.len();
    }

    fn number(&mut self, mut v: u64) {
        let mut digits = [0u8; DIGITS];
        let mut k = DIGITS;
        loop {
            k -= 1;
            digits[k] = b'0' + (v % BASE) as u8;
            v /= BASE;
            if v == 0 {
                break;
            }
        }
        self.bytes(&digits[k..]);
    }
}

fn main() {
    let mut input = Input {
        buf: [0; BUFFER],
        len: 0,
        pos: 0,
    };
    let mut output = Output {
        buf: [0; BUFFER],
        len: 0,
    };
    let n = input.number() as usize;
    let k = input.number() as usize;
    let f = input.number();
    let mut need = [0i64; MAXN]; // goblets each knight still has to gain (or lose)
    for x in need.iter_mut().take(n) {
        *x = f - input.number();
    }
    // signed visits to the pair (i, i + K); + brings, - takes
    let mut visits = [0i64; MAXN];
    let mut seen = [false; MAXN];
    let mut cycle = [0usize; MAXN];
    let mut sgn = [0i64; MAXN];
    let mut base = [0i64; MAXN];
    let mut cut = [0i64; MAXN];
    for s in 0..n {
        if seen[s] {
            continue;
        }
        // the knights s, s + K, s + 2K, ... form a cycle; pair e_i joins the
        // i-th and the next. With x_0 = t, the rule x_(i-1) + x_i = need of
        // the i-th knight gives x_i = sgn_i * t + base_i
        let mut len = 0;
        let mut v = s;
        while !seen[v] {
            seen[v] = true;
            cycle[len] = v;
            len += 1;
            v = (v + k) % n;
        }
        sgn[0] = 1;
        base[0] = 0;
        for i in 1..len {
            sgn[i] = -sgn[i - 1];
            base[i] = need[cycle[i]] - base[i - 1];
        }
        // the last pair and the first must give the first knight its share
        let rest = need[cycle[0]] - base[len - 1];
        let t;
        if len % 2 == 1 {
            // odd cycle: 2t = rest, a single solution
            if rest % 2 != 0 {
                output.bytes(b"-1\n");
                output.flush();
                return;
            }
            t = rest / 2;
        } else {
            // even cycle: any t works if rest is 0; the sum of |t - cut_i|
            // is least at a median
            if rest != 0 {
                output.bytes(b"-1\n");
                output.flush();
                return;
            }
            for i in 0..len {
                cut[i] = -base[i] * sgn[i];
            }
            let middle = len / 2;
            t = *cut[..len].select_nth_unstable(middle).1;
        }
        for i in 0..len {
            visits[cycle[i]] = sgn[i] * t + base[i];
        }
    }
    let total: u64 = visits[..n].iter().map(|x| x.unsigned_abs()).sum();
    output.number(total);
    output.bytes(b"\n");
    // bring everything first, so that no knight ever runs short
    for (sign, brings) in [(b'+', true), (b'-', false)] {
        for (i, &x) in visits[..n].iter().enumerate() {
            if x != 0 && (x > 0) == brings {
                for _ in 0..x.unsigned_abs() {
                    output.number(i as u64 + 1);
                    output.bytes(b" ");
                    output.number(((i + k) % n) as u64 + 1);
                    output.bytes(&[b' ', sign, b'\n']);
                }
            }
        }
    }
    output.flush();
}
