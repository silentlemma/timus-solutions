use std::io::{self, Read, Write};

fn erase(bytes: &mut [u8]) {
    for byte in bytes {
        if *byte != b' ' {
            *byte = b'_';
        }
    }
}

fn fill(source: &mut [u8], target: &[u8]) -> bool {
    let mut prefix = Vec::<u32>::new();
    let (mut search, mut kept_until) = (0, 0);
    for word in target.split(|&byte| byte == b' ') {
        // Reuse the prefix table across words. Each index fits in 32 bits.
        prefix.resize(word.len(), 0);
        let mut matched = 0;
        for i in 1..word.len() {
            while matched > 0 && word[i] != word[matched] {
                matched = prefix[matched - 1] as usize;
            }
            if word[i] == word[matched] {
                matched += 1;
            }
            prefix[i] = matched as u32;
        }

        matched = 0;
        while search < source.len() {
            let byte = source[search];
            search += 1;
            while matched > 0 && byte != word[matched] {
                matched = prefix[matched - 1] as usize;
            }
            if byte == word[matched] {
                matched += 1;
                if matched == word.len() {
                    break;
                }
            }
        }
        if matched != word.len() {
            return false;
        }

        // Reserve one byte as a separator before the next kept word.
        erase(&mut source[kept_until..search - word.len()]);
        kept_until = search;
        search += 1;
    }
    erase(&mut source[kept_until..]);
    true
}

fn trim_cr(line: &mut [u8]) -> &mut [u8] {
    let length = line.len() - usize::from(line.last() == Some(&b'\r'));
    &mut line[..length]
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let mut lines = input.split_mut(|&byte| byte == b'\n');
    let source = trim_cr(lines.next().unwrap());
    let target = trim_cr(lines.next().unwrap());
    let mut output = io::stdout().lock();
    if fill(source, target) {
        output.write_all(source).unwrap();
        output.write_all(b"\n").unwrap();
    } else {
        output.write_all(b"I HAVE FAILED!!!\n").unwrap();
    }
}
