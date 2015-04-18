
use std::io::Read;
use std::fs::File;

fn word_score(word: &str) -> usize {
    word.bytes().map(|x: u8| x - 64).fold(0, |acc, x| acc + (x as usize))
}

fn main() {

    let mut total = 0;

    let mut f = File::open("../data/p022.txt").unwrap();
    let mut s = String::new();
    let _ = f.read_to_string(&mut s);

    let chars_to_trim: &[char] = &['\t', '\n', '\r', '"'];
    let mut words = s.trim_matches(chars_to_trim).split("\",\"").collect::<Vec<&str>>();
    words.sort();

    for (i, word) in words.iter().enumerate() {
        total += (i + 1) * word_score(word);
    }

    println!("{}", total);

}
