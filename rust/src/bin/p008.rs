
use std::io::Read;
use std::fs::File;

fn main() {

    let mut num = String::new();
    let mut f = File::open("../data/p008.txt").unwrap();
    let _ = f.read_to_string(&mut num);
    num = num.replace("\n", "");

    let mut max_prod = 0;

    for i in (0..num.len() - 12) {
        let prod = num[i .. i + 13].chars().map(|x| x.to_string().parse::<usize>().unwrap()).fold(1, |mul, x| mul * x);
        if prod > max_prod {
            max_prod = prod;
        }
    }

    println!("{}", max_prod);
}
