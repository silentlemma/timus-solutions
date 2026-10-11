use std::io::{self, Read, Write};

const LIMIT: usize = 1_000_000;

struct Templates {
    text: Vec<Vec<u8>>,
    size: Vec<usize>,
    state: Vec<u8>,
}

impl Templates {
    // the fully expanded length, capped above the limit; state 1 marks
    // templates being expanded, so meeting one again is a cycle
    fn measure(&mut self, i: usize) -> bool {
        self.state[i] = 1;
        let mut k = 0;
        while k < self.text[i].len() {
            if self.text[i][k] != b'*' {
                self.size[i] = (self.size[i] + 1).min(LIMIT + 1);
            } else {
                k += 1;
                let j = (self.text[i][k] - b'0') as usize;
                if self.state[j] == 1 || (self.state[j] == 0 && !self.measure(j)) {
                    return false;
                }
                self.size[i] = (self.size[i] + self.size[j]).min(LIMIT + 1);
            }
            k += 1;
        }
        self.state[i] = 2;
        true
    }

    fn write(&self, i: usize, out: &mut Vec<u8>) {
        let mut k = 0;
        while k < self.text[i].len() {
            if self.text[i][k] == b'*' {
                k += 1;
                self.write((self.text[i][k] - b'0') as usize, out);
            } else {
                out.push(self.text[i][k]);
            }
            k += 1;
        }
    }
}

fn main() {
    let mut raw = Vec::new();
    io::stdin().read_to_end(&mut raw).unwrap();
    let data: Vec<u8> = raw.into_iter().filter(|&c| c != b'\r').collect();
    let line = data.iter().position(|&c| c == b'\n').unwrap();
    let n: usize = std::str::from_utf8(&data[..line])
        .unwrap()
        .trim()
        .parse()
        .unwrap();
    // a template runs from the start of a line to its '#'
    let mut text = vec![Vec::new()];
    let mut pos = line + 1;
    for _ in 0..n {
        let end = pos + data[pos..].iter().position(|&c| c == b'#').unwrap();
        text.push(data[pos..end].to_vec());
        pos = end + 1;
        if pos < data.len() && data[pos] == b'\n' {
            pos += 1;
        }
    }
    let mut t = Templates {
        text,
        size: vec![0; n + 1],
        state: vec![0; n + 1],
    };
    let mut out = Vec::new();
    if !t.measure(1) || t.size[1] > LIMIT {
        out.extend_from_slice(b"#\n");
    } else {
        t.write(1, &mut out);
        out.push(b'\n');
    }
    io::stdout().write_all(&out).unwrap();
}
