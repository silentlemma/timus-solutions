use std::io::{self, BufWriter, Read, Write};

const CUT: u32 = 1 << 31;
const BUFFER_SIZE: usize = 4096;

fn main() {
    let mut raw = String::new();
    io::stdin().read_to_string(&mut raw).unwrap();
    let mut tokens = raw.split_ascii_whitespace();
    let word = tokens.next().unwrap().as_bytes();
    let text = tokens.next().unwrap().as_bytes();
    let (size, n) = (word.len(), text.len());
    let mut prefix = vec![0u32; size];
    let mut matched = vec![0u32; n + 1];
    for i in 1..size {
        let mut k = prefix[i - 1] as usize;
        while k > 0 && word[k] != word[i] {
            k = prefix[k - 1] as usize;
        }
        if word[k] == word[i] {
            k += 1;
        }
        prefix[i] = k as u32;
    }
    let mut k = 0usize;
    for end in 1..=n {
        while k > 0 && (k == size || word[k] != text[end - 1]) {
            k = prefix[k - 1] as usize;
        }
        if word[k] == text[end - 1] {
            k += 1;
        }
        matched[end] = k as u32;
    }
    let mut end = n;
    while end > 0 {
        let length = matched[end];
        if length == 0 {
            println!("Yes");
            return;
        }
        // Matched lengths fit 17 bits, leaving the high bit for selected cuts.
        matched[end] |= CUT;
        end -= length as usize;
    }
    let stdout = io::stdout();
    let mut out = BufWriter::with_capacity(BUFFER_SIZE, stdout.lock());
    out.write_all(b"No\n").unwrap();
    let mut begin = 0;
    for end in 1..=n {
        if matched[end] & CUT != 0 {
            if begin > 0 {
                out.write_all(b" ").unwrap();
            }
            out.write_all(&text[begin..end]).unwrap();
            begin = end;
        }
    }
    out.write_all(b"\n").unwrap();
}
