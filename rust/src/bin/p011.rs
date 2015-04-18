
use std::io::Read;
use std::fs::File;

fn main() {

    let mut s = String::new();
    let mut f = File::open("../data/p011.txt").unwrap();
    let _ = f.read_to_string(&mut s);

    let mut nums: Vec<Vec<usize>> = vec![];

    for l in s.trim_matches('\n').split("\n") {
        nums.push(l.split(" ").map(|x| x.parse::<usize>().unwrap()).collect());
    }

    let mut max_prod = 0;

    for y in (0..20) {
        for x in (0..20) {
            if x <= 16 {
                let prod = nums[y][x .. x + 4].iter().fold(1, |mul, x| mul * x);
                if prod > max_prod {
                    max_prod = prod
                }
            }
            if y <= 16 {
                let prod = [nums[y][x], nums[y + 1][x], nums[y + 2][x], nums[y + 3][x]].iter().fold(1, |mul, x| mul * x);
                if prod > max_prod {
                    max_prod = prod
                }
            }
            if x <= 16 && y <= 16 {
                let prod = [nums[y][x], nums[y + 1][x + 1], nums[y + 2][x + 2], nums[y + 3][x + 3]].iter().fold(1, |mul, x| mul * x);
                if prod > max_prod {
                    max_prod = prod
                }
            }
            if x <= 16 && y >= 4 {
                let prod = [nums[y][x], nums[y - 1][x + 1], nums[y - 2][x + 2], nums[y - 3][x + 3]].iter().fold(1, |mul, x| mul * x);
                if prod > max_prod {
                    max_prod = prod
                }
            }
        }
    }

    println!("{}", max_prod);
}
