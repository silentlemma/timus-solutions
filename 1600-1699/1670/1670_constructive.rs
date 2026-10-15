use std::io::{self, Read};

#[derive(Clone, Copy, PartialEq)]
enum Kind {
    Leaf,
    Direct,
    Skew,
}

struct Tree {
    kinds: Vec<Kind>,
    lefts: Vec<usize>,
    rights: Vec<usize>,
    values: Vec<usize>,
}

enum Item {
    Text(char),
    Expr(usize),
    Seq(usize),
}

impl Tree {
    fn add(&mut self, kind: Kind, left: usize, right: usize, value: usize) -> usize {
        self.kinds.push(kind);
        self.lefts.push(left);
        self.rights.push(right);
        self.values.push(value);
        self.kinds.len() - 1
    }

    /// The children of the maximal run of nodes of the same kind below and
    /// including node, in order of position (both joins are associative).
    fn parts(&self, node: usize) -> Vec<usize> {
        let (mut out, mut todo) = (Vec::new(), vec![node]);
        while let Some(cur) = todo.pop() {
            if self.kinds[cur] == self.kinds[node] {
                todo.push(self.rights[cur]);
                todo.push(self.lefts[cur]);
            } else {
                out.push(cur);
            }
        }
        out
    }

    /// A direct node is a sequence of its parts; a skew node is its parts
    /// joined by stars from the smallest values up; no recursion, as the
    /// tree can be 10^4 levels deep.
    fn show(&self, root: usize) -> String {
        let mut out = String::new();
        let mut work = vec![Item::Expr(root)];
        while let Some(item) = work.pop() {
            match item {
                Item::Text(c) => out.push(c),
                Item::Expr(node) | Item::Seq(node) if self.kinds[node] == Kind::Leaf => {
                    let number = self.values[node].to_string();
                    if let Item::Expr(_) = item {
                        out.push_str(&number);
                    } else {
                        out.push_str(&format!("({})", number));
                    }
                }
                Item::Expr(node) | Item::Seq(node) if self.kinds[node] == Kind::Skew => {
                    // pushed in reverse: the largest values come out first as text
                    for (i, child) in self.parts(node).into_iter().enumerate() {
                        if i > 0 {
                            work.push(Item::Text('*'));
                        }
                        work.push(Item::Seq(child));
                    }
                }
                Item::Expr(node) | Item::Seq(node) => {
                    let children = self.parts(node);
                    work.push(Item::Text(')'));
                    for i in (0..children.len()).rev() {
                        work.push(Item::Expr(children[i]));
                        work.push(Item::Text(if i > 0 { ',' } else { '(' }));
                    }
                }
            }
        }
        // a lone number at the top must still be a sequence
        if self.kinds[root] == Kind::Leaf {
            format!("({})", out)
        } else {
            out
        }
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<usize> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let n = v[0];
    let mut tree = Tree { kinds: vec![], lefts: vec![], rights: vec![], values: vec![] };
    // blocks of consecutive positions holding consecutive values, as
    // (lowest value, highest value, tree); two neighbours whose value
    // ranges touch join into one block
    let mut stack: Vec<(usize, usize, usize)> = Vec::new();
    for &x in &v[1..=n] {
        let (mut lo, mut hi, mut node) = (x, x, tree.add(Kind::Leaf, 0, 0, x));
        while let Some(&(plo, phi, prev)) = stack.last() {
            if phi + 1 == lo {
                node = tree.add(Kind::Direct, prev, node, 0);
            } else if hi + 1 == plo {
                node = tree.add(Kind::Skew, prev, node, 0);
            } else {
                break;
            }
            stack.pop();
            lo = lo.min(plo);
            hi = hi.max(phi);
        }
        stack.push((lo, hi, node));
    }
    if stack.len() == 1 {
        println!("{}", tree.show(stack[0].2));
    } else {
        println!("IMPOSSIBLE");
    }
}
