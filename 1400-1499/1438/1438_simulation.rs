use std::collections::{BTreeMap, HashMap};
use std::io::{self, Read, Write};

const LIMIT: u64 = 10_000_000;

#[derive(Clone, Copy)]
enum Calc {
    Add,
    Sub,
    Mul,
    Div,
    Mod,
    Or,
    And,
    Xor,
}

#[derive(Clone, Copy)]
enum Test {
    Eq,
    Ne,
    Ge,
    Gt,
    Le,
    Lt,
}

const CALCS: [(&str, Calc); 8] = [
    ("+", Calc::Add),
    ("-", Calc::Sub),
    ("*", Calc::Mul),
    ("/", Calc::Div),
    ("%", Calc::Mod),
    ("or", Calc::Or),
    ("and", Calc::And),
    ("xor", Calc::Xor),
];
const TESTS: [(&str, Test); 6] = [
    ("==", Test::Eq),
    ("!=", Test::Ne),
    (">=", Test::Ge),
    (">", Test::Gt),
    ("<=", Test::Le),
    ("<", Test::Lt),
];

/// Operands are slots in one value table: variables and constants.
#[derive(Clone, Copy)]
enum Op {
    Set(usize, usize),
    Not(usize, usize),
    Calc(usize, usize, usize, Calc),
    End,
    Print(usize),
    Goto(usize),
    If(usize, usize, Test, usize),
}

fn calc(code: Calc, x: i64, y: i64) -> i64 {
    match code {
        Calc::Add => x + y,
        Calc::Sub => x - y,
        Calc::Mul => x * y,
        Calc::Div => x / y,                       // rounds towards zero
        Calc::Mod => (x % y + y.abs()) % y.abs(), // never negative
        Calc::Or => x | y,
        Calc::And => x & y,
        Calc::Xor => x ^ y,
    }
}

fn test(code: Test, x: i64, y: i64) -> bool {
    match code {
        Test::Eq => x == y,
        Test::Ne => x != y,
        Test::Ge => x >= y,
        Test::Gt => x > y,
        Test::Le => x <= y,
        Test::Lt => x < y,
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // a line is "label:", "label: command" or "command"; lines with only a label are no commands
    let mut labels: HashMap<String, usize> = HashMap::new();
    let mut commands: Vec<Vec<&str>> = Vec::new();
    for line in input.lines() {
        let mut t: Vec<&str> = line.split_whitespace().collect();
        if let Some(first) = t.first() {
            if let Some(label) = first.strip_suffix(':') {
                labels.insert(label.to_lowercase(), commands.len());
                t.remove(0);
            }
        }
        if !t.is_empty() {
            commands.push(t);
        }
    }
    let mut names: BTreeMap<String, usize> = BTreeMap::new();
    let mut values: Vec<i64> = Vec::new();
    let mut operand = |tok: &str, values: &mut Vec<i64>| -> usize {
        if let Ok(v) = tok.parse::<i64>() {
            values.push(v);
            return values.len() - 1;
        }
        if let Some(&k) = names.get(tok) {
            return k;
        }
        values.push(0);
        names.insert(tok.to_string(), values.len() - 1);
        values.len() - 1
    };
    let mut ops = Vec::with_capacity(commands.len());
    for t in &commands {
        let head = t[0].to_lowercase();
        let op = if t.len() > 1 && t[1] == "=" {
            let dst = operand(t[0], &mut values);
            // a value, "not" and a value, or a value, an operation and a value
            match &t[2..] {
                [x] => Op::Set(dst, operand(x, &mut values)),
                [_, x] => Op::Not(dst, operand(x, &mut values)),
                [x, name, y] => {
                    let a = operand(x, &mut values);
                    let b = operand(y, &mut values);
                    let lowered = name.to_lowercase();
                    let code = CALCS.iter().find(|c| c.0 == lowered).unwrap().1;
                    Op::Calc(dst, a, b, code)
                }
                _ => unreachable!(),
            }
        } else if head == "end" {
            Op::End
        } else if head == "print" {
            Op::Print(operand(t[1], &mut values))
        } else if head == "goto" {
            Op::Goto(labels[&t[1].to_lowercase()])
        } else if let [_, x, name, y, _, label] = t[..] {
            // a conditional jump: two values around a comparison, then a label
            let a = operand(x, &mut values);
            let b = operand(y, &mut values);
            let code = TESTS.iter().find(|c| c.0 == name).unwrap().1;
            Op::If(a, b, code, labels[&label.to_lowercase()])
        } else {
            unreachable!()
        };
        ops.push(op);
    }
    let mut assigned = vec![false; values.len()];
    let mut out = String::new();
    let (mut pc, size, mut executed, mut ended) = (0usize, ops.len(), 0u64, false);
    while pc < size && executed < LIMIT {
        let i = pc;
        pc += 1;
        executed += 1;
        match ops[i] {
            Op::Set(d, a) => {
                values[d] = values[a];
                assigned[d] = true;
            }
            Op::Not(d, a) => {
                values[d] = !values[a];
                assigned[d] = true;
            }
            Op::Calc(d, a, b, code) => {
                values[d] = calc(code, values[a], values[b]);
                assigned[d] = true;
            }
            Op::End => {
                ended = true;
                pc = size;
            }
            Op::Print(a) => {
                out.push_str(&values[a].to_string());
                out.push('\n');
            }
            Op::Goto(target) => pc = target,
            Op::If(a, b, code, target) => {
                if test(code, values[a], values[b]) {
                    pc = target;
                }
            }
        }
    }
    if !ended && executed == LIMIT {
        // ten million commands done and the program still runs
        out.push_str("Program terminated. Variables state:\n");
        for (name, &k) in &names {
            if assigned[k] {
                out.push_str(&format!("{}: {}\n", name, values[k]));
            }
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
