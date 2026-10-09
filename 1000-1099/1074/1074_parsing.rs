use std::io::{self, Read, Write};

// exponents beyond this either give zero or an answer longer than allowed
const EXP_LIMIT: i64 = 1000;
const FAIL: &str = "Not a floating point number";

fn run(s: &[u8], pos: &mut usize) -> Vec<u8> {
    let start = *pos;
    while *pos < s.len() && s[*pos].is_ascii_digit() {
        *pos += 1;
    }
    s[start..*pos].to_vec()
}

fn convert(s: &[u8], n: i64) -> String {
    let mut pos = 0;
    let at = |pos: usize, chars: &[u8]| pos < s.len() && chars.contains(&s[pos]);
    let mut negative = false;
    if at(pos, b"+-") {
        negative = s[pos] == b'-';
        pos += 1;
    }
    let whole = run(s, &mut pos);
    let mut frac = Vec::new();
    if at(pos, b".") {
        pos += 1;
        frac = run(s, &mut pos);
        if frac.is_empty() {
            return FAIL.to_string();
        }
    } else if whole.is_empty() {
        return FAIL.to_string();
    }
    let mut exp: i64 = 0;
    if at(pos, b"eE") {
        pos += 1;
        let mut sign = 1;
        if at(pos, b"+-") {
            sign = if s[pos] == b'-' { -1 } else { 1 };
            pos += 1;
        }
        let power = run(s, &mut pos);
        if power.is_empty() {
            return FAIL.to_string();
        }
        for c in power {
            exp = (exp * 10 + (c - b'0') as i64).min(EXP_LIMIT);
        }
        exp *= sign;
    }
    if pos != s.len() {
        return FAIL.to_string();
    }
    // the digits of the number with the decimal point after `point` of them
    let mantissa = [whole.as_slice(), frac.as_slice()].concat();
    let mut point = whole.len() as i64 + exp;
    if mantissa.iter().all(|&c| c == b'0') {
        point = 0;
    }
    let digit = |i: i64| -> u8 {
        if i >= 0 && (i as usize) < mantissa.len() {
            mantissa[i as usize]
        } else {
            b'0'
        }
    };
    let mut head: Vec<u8> = (0..point.max(0))
        .map(digit)
        .skip_while(|&c| c == b'0')
        .collect();
    if head.is_empty() {
        head.push(b'0');
    }
    let tail: Vec<u8> = (point..point + n).map(digit).collect();
    let nonzero = head.iter().chain(tail.iter()).any(|&c| c != b'0');
    let mut out = String::new();
    if negative && nonzero {
        out.push('-');
    }
    out.push_str(std::str::from_utf8(&head).unwrap());
    if n > 0 {
        out.push('.');
        out.push_str(std::str::from_utf8(&tail).unwrap());
    }
    out
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let lines: Vec<&[u8]> = data.split(|&c| c == b'\n').collect();
    let mut out = String::new();
    let mut i = 0;
    while i + 1 < lines.len() {
        let s = lines[i].strip_suffix(b"\r").unwrap_or(lines[i]);
        if s == b"#" {
            break;
        }
        let n: i64 = String::from_utf8_lossy(lines[i + 1])
            .trim()
            .parse()
            .unwrap();
        out.push_str(&convert(s, n));
        out.push('\n');
        i += 2;
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
