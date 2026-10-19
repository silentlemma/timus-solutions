use std::collections::HashMap;
use std::fmt::Write;
use std::io::{self, Read};

const CALL_PREFIX: usize = 3;

fn words(line: &str) -> Vec<&str> {
    line.split(|letter: char| !letter.is_ascii_alphabetic())
        .filter(|word| !word.is_empty())
        .collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let function_count: usize = lines.next().unwrap().parse().unwrap();
    let mut functions = HashMap::new();
    for _ in 0..function_count {
        let tokens = words(lines.next().unwrap());
        let argument_types: Vec<_> = tokens[1..tokens.len() - 1]
            .iter()
            .map(|value| value.to_string())
            .collect();
        functions.insert(
            (tokens[0].to_owned(), argument_types),
            tokens.last().unwrap().to_string(),
        );
    }
    let line_count: usize = lines.next().unwrap().parse().unwrap();
    let mut variables: HashMap<String, String> = HashMap::new();
    let mut inferred = String::new();
    for number in 1..=line_count {
        let tokens = words(lines.next().unwrap());
        let (declared, name, function) = (tokens[0], tokens[1], tokens[2]);
        let mut error = "";
        let mut argument_types = Vec::new();
        if variables.contains_key(name) {
            error = "Double declaration";
        } else {
            for argument in &tokens[CALL_PREFIX..] {
                if let Some(value_type) = variables.get(*argument) {
                    argument_types.push(value_type.clone());
                } else {
                    error = "Unknown variable";
                    break;
                }
            }
        }
        if error.is_empty() {
            if let Some(result) = functions.get(&(function.to_owned(), argument_types)) {
                if declared != "auto" && declared != result {
                    error = "Invalid initialization";
                } else {
                    variables.insert(name.to_owned(), result.clone());
                    if declared == "auto" {
                        writeln!(inferred, "{name} : {result}").unwrap();
                    }
                }
            } else {
                error = "No such function";
            }
        }
        if !error.is_empty() {
            println!("Error on line {number}: {error}");
            return;
        }
    }
    print!("{inferred}");
}
