use std::collections::BTreeMap;
use std::io::{self, Read};

type Counts = BTreeMap<String, i64>;

// the number starting at s[i] (1 if there is none) and the index after it
fn number(s: &[u8], i: usize) -> (i64, usize) {
    let mut j = i;
    while j < s.len() && s[j].is_ascii_digit() {
        j += 1;
    }
    if j == i {
        return (1, j);
    }
    (std::str::from_utf8(&s[i..j]).unwrap().parse().unwrap(), j)
}

fn totals(formula: &str) -> Counts {
    let mut result = Counts::new();
    for term in formula.split('+') {
        let term = term.as_bytes();
        let (times, mut i) = number(term, 0);
        // one level per open bracket; a closing bracket multiplies its level
        // by the number after it and adds it to the level outside
        let mut stack = vec![Counts::new()];
        while i < term.len() {
            match term[i] {
                b'(' => {
                    stack.push(Counts::new());
                    i += 1;
                }
                b')' => {
                    let inner = stack.pop().unwrap();
                    let (k, end) = number(term, i + 1);
                    i = end;
                    for (name, count) in inner {
                        *stack.last_mut().unwrap().entry(name).or_insert(0) += count * k;
                    }
                }
                _ => {
                    let mut j = i + 1;
                    if j < term.len() && term[j].is_ascii_lowercase() {
                        j += 1;
                    }
                    let name = String::from_utf8(term[i..j].to_vec()).unwrap();
                    let (k, end) = number(term, j);
                    *stack.last_mut().unwrap().entry(name).or_insert(0) += k;
                    i = end;
                }
            }
        }
        for (name, count) in stack.pop().unwrap() {
            *result.entry(name).or_insert(0) += count * times;
        }
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let left = it.next().unwrap();
    let n: usize = it.next().unwrap().parse().unwrap();
    let want = totals(left);
    let mut out = String::new();
    for right in it.take(n) {
        let sign = if totals(right) == want { "==" } else { "!=" };
        out += &format!("{}{}{}\n", left, sign, right);
    }
    print!("{}", out);
}
