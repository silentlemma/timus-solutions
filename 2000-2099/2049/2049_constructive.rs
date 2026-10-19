use std::io::{self, Read, Write};

const SPLIT_DIVISOR: usize = 4;

struct Answer {
    from: Vec<usize>,
    to: Vec<usize>,
}

struct State {
    volume: Vec<usize>,
    previous: Vec<usize>,
    following: Vec<usize>,
    groups: Vec<usize>,
    value_previous: Vec<usize>,
    value_following: Vec<usize>,
    odd_head: usize,
    even_head: usize,
    even_count: usize,
    answer: Answer,
}

impl State {
    fn new(size: usize, target: usize) -> Self {
        let mut state = Self {
            volume: vec![0; size + 1],
            previous: vec![0; size + 1],
            following: vec![0; size + 1],
            groups: vec![0; size + 1],
            value_previous: vec![0; size + 1],
            value_following: vec![0; size + 1],
            odd_head: 0,
            even_head: 0,
            even_count: 0,
            answer: Answer {
                from: Vec::new(),
                to: Vec::new(),
            },
        };
        state.volume[1] = target;
        state.attach(1);
        if size != target {
            state.volume[2] = size - target;
            state.attach(2);
        }
        state
    }

    fn attach(&mut self, index: usize) {
        let value = self.volume[index];
        let head;
        if value % 2 != 0 {
            head = self.groups[value];
            if head == 0 {
                self.value_previous[value] = 0;
                self.value_following[value] = self.odd_head;
                if self.odd_head != 0 {
                    self.value_previous[self.odd_head] = value;
                }
                self.odd_head = value;
            }
            self.groups[value] = index;
        } else {
            head = self.even_head;
            self.even_head = index;
            self.even_count += 1;
        }
        self.previous[index] = 0;
        self.following[index] = head;
        if head != 0 {
            self.previous[head] = index;
        }
    }

    fn detach(&mut self, index: usize) {
        let value = self.volume[index];
        if value == 0 {
            return;
        }
        let mut before = self.previous[index];
        let mut after = self.following[index];
        if before != 0 {
            self.following[before] = after;
        } else if value % 2 != 0 {
            self.groups[value] = after;
        } else {
            self.even_head = after;
        }
        if after != 0 {
            self.previous[after] = before;
        }
        if value % 2 != 0 {
            if self.groups[value] == 0 {
                before = self.value_previous[value];
                after = self.value_following[value];
                if before != 0 {
                    self.value_following[before] = after;
                } else {
                    self.odd_head = after;
                }
                if after != 0 {
                    self.value_previous[after] = before;
                }
            }
        } else {
            self.even_count -= 1;
        }
    }

    fn undo(&mut self, donor: usize, receiver: usize) {
        self.detach(donor);
        self.detach(receiver);
        let half = self.volume[receiver] / 2;
        self.volume[receiver] = half;
        self.volume[donor] += half;
        self.attach(donor);
        self.attach(receiver);
        self.answer.from.push(donor);
        self.answer.to.push(receiver);
    }
}

fn solve(n: usize, k: usize) -> Option<Answer> {
    let size = if k & (k - 1) == 0 { k } else { k + 1 + (k & 1) };
    if size > n {
        return None;
    }
    let mut state = State::new(size, k);
    let mut empty: Vec<usize> = (1..=size).filter(|&i| state.volume[i] == 0).collect();
    while state.even_count > 0 {
        let mut receiver = state.even_head;
        if state.even_count > 1 || state.volume[receiver] % SPLIT_DIVISOR == 0 {
            state.undo(empty.pop().unwrap(), receiver);
            continue;
        }
        let mut value = state.odd_head;
        if value == state.volume[receiver] / 2 {
            value = state.value_following[value];
        }
        if value == 0 {
            state.undo(empty.pop().unwrap(), receiver);
            continue;
        }
        let mut donor = state.groups[value];
        while state.volume[receiver] % SPLIT_DIVISOR != 0 {
            state.undo(donor, receiver);
            std::mem::swap(&mut donor, &mut receiver);
        }
    }
    Some(state.answer)
}

fn write_answer(answer: Option<Answer>, out: &mut impl Write) {
    if let Some(answer) = answer {
        writeln!(out, "{}", answer.from.len()).unwrap();
        for i in (0..answer.from.len()).rev() {
            writeln!(out, "{} {}", answer.from[i], answer.to[i]).unwrap();
        }
    } else {
        writeln!(out, "-1").unwrap();
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut fields = input.split_whitespace();
    let n = fields.next().unwrap().parse().unwrap();
    let k = fields.next().unwrap().parse().unwrap();
    let mut out = io::BufWriter::new(io::stdout().lock());
    write_answer(solve(n, k), &mut out);
}
