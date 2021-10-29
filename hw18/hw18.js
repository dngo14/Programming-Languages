#!/usr/bin/node

const square = function(x) {
    return x * x;
  };
  
  console.log(square(12));

const makeNoise = function() {
    console.log("Pling!");
  };
  
  makeNoise();

const power = function(base, exponent) {
let result = 1;
for (let count = 0; count < exponent; count++) {
    result *= base;
}
return result;
};

console.log(power(2, 10));

const halve = function(n) {
    return n / 2;
  };
  
  let n = 10;
  console.log(halve(100));
  // → 50
  console.log(n);
  // → 10

const power2 = (base, exponent) => {
    let result = 1;
    for (let count = 0; count < exponent; count++) {
      result *= base;
    }
    return result;
  };

// Excercises

const min = (x, y) => {
    if (x > y) {
        return y;
    } else {
        return x
    }
};

console.log(min(0, 10));
console.log(min(0, -10));

const isEven = (x) => {
    if (x == 1) {
        return false;
    } else if (x == 0) {
        return true;
    } else if (x == -1) {
        return false
    }else if (x < 0) {
        return isEven(x+2);
    }else {
        return isEven(x-2);
    }
}

console.log(isEven(50));
console.log(isEven(75));
console.log(isEven(-1));
console.log(isEven(-10));

const countBs = (string) => {
    let count = 0;
    for (let x = 0; x < string.length; x+=1) {
        if (string[x] == "B") {
            count += 1
        }
    }
    return count
}

console.log(countBs("BBC"));

const countChar = (string, letter) => {
    let count = 0;
    for (let x = 0; x < string.length; x+=1) {
        if (string[x] == letter) {
            count += 1;
        }
    }
    return count;
}

console.log(countChar("kakkerlak", "k"));

const add3 = (list) => {
    for (let x = 0; x < list.length; x+=1) {
        list[x] += 3;
    }
    return list;
}
let list1 = [1, 2, 3];
console.log(add3(list1));

const echo = (list) => {
    let newlist = [];
    for (let x = 0; x < list.length; x+=1) {
        newlist.push(list[x]);
        newlist.push(list[x]);
    }
    return newlist
}
console.log(echo(list1));

let list2 = [[1,2], 2, [3]]
const add4 = (list) => {
    for (let x = 0; x < list.length; x+=1) {
        if (list[x].constructor.name == "Array") {
            add4(list[x]);
        } else {
            list[x] += 4;
        }
    }
    return list;
}
console.log(add4(list2));
