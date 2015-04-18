
use std::collections::HashMap;

fn sum_proper_divisors(n: usize) -> usize {
    let mut s = 1;
    let end = (n as f64).sqrt() as usize;
    for i in (2..end + 1) {
        if n % i == 0 {
            s += i;
            if i != n / i {s += n / i;}
        }
    }
    s
}

fn main() {

    let mut total = 0;
    let mut cache: HashMap<usize, usize> = HashMap::new();

    for i in (1..10000) {
        let n = sum_proper_divisors(i);
        if cache.contains_key(&i) && *cache.get(&i).unwrap() == n {
            total += i + n;
        } else {
            cache.insert(n, i);
        }
    }

    println!("{}", total);

}
