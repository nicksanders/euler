
fn main() {

    let limit = 1000000;
    let mut cache = vec![0; limit];
    cache[1] = 1;
    let mut result = [1, 1];

    for i in (1..limit) {
        let mut cnt = 0;
        let mut n = i;

        while n > limit - 1 || cache[n] == 0 {
            if n % 2 == 0 {
                n /= 2;
            } else {
                n = (n * 3) + 1;
            }
            cnt += 1;
        }

        cache[i] = cache[n] + cnt;
        if cache[i] > result[1] {
            result = [i, cache[i]];
        }

    }

    println!("{} {}", result[0], result[1]);
}
