#!/usr/bin/node

let total = 0, count = 1;
while (count <= 10) {
  total += count;
  count += 1;
}
console.log(total);

function repeatLog(n) {
    for (let i = 0; i < n; i++) {
      console.log(i);
    }
  }
  /* function repeat(n, action) {
    for (let i = 0; i < n; i++) {
      action(i);
    }
  } 
  
  repeat(3, console.log);
*/
  //let labels = [];
//repeat(5, i => {
 // labels.push(`Unit ${i + 1}`);
//});
//console.log(labels);
function greaterThan(n) {
    return m => m > n;
  }
  let greaterThan10 = greaterThan(10);
  console.log(greaterThan10(11));

  function noisy(f) {
    return (...args) => {
      console.log("calling with", args);
      let result = f(...args);
      console.log("called with", args, ", returned", result);
      return result;
    };
  }
  noisy(Math.min)(3, 2, 1);

  function unless(test, then) {
    if (!test) then();
  }
  
  //repeat(3, n => {
   // unless(n % 2 == 1, () => {
   //   console.log(n, "is even");
   // });
 // });
  function filter(array, test) {
    let passed = [];
    for (let element of array) {
      if (test(element)) {
        passed.push(element);
      }
    }
    return passed;
  }
  function map(array, transform) {
    let mapped = [];
    for (let element of array) {
      mapped.push(transform(element));
    }
    return mapped;
  }
  
  //console.log(filter(SCRIPTS, script => script.living));
  function reduce(array, combine, start) {
    let current = start;
    for (let element of array) {
      current = combine(current, element);
    }
    return current;
  }
  
  console.log(reduce([1, 2, 3, 4], (a, b) => a + b, 0));
  function characterCount(script) {
    return script.ranges.reduce((count, [from, to]) => {
      return count + (to - from);
    }, 0);
  }
  
  //console.log(SCRIPTS.reduce((a, b) => {
    //return characterCount(a) < characterCount(b) ? b : a;
  //}));
  function countBy(items, groupName) {
    let counts = [];
    for (let item of items) {
      let name = groupName(item);
      let known = counts.findIndex(c => c.name == name);
      if (known == -1) {
        counts.push({name, count: 1});
      } else {
        counts[known].count++;
      }
    }
    return counts;
  }
  
  console.log(countBy([1, 2, 3, 4, 5], n => n > 2));
  //function textScripts(text) {
   // let scripts = countBy(text, char => {
   //   let script = characterScript(char.codePointAt(0));
   //   return script ? script.name : "none";
  //  }).filter(({name}) => name != "none");
  
   // let total = scripts.reduce((n, {count}) => n + count, 0);
  //  if (total == 0) return "No scripts found";
  
  //  return scripts.map(({name, count}) => {
  //    return `${Math.round(count * 100 / total)}% ${name}`;
  //  }).join(", ");
 // }
  
 // console.log(textScripts('英国的狗说"woof", 俄罗斯的狗说"тяв"'));

  // excercise one: flattening
  let arrays = [[1, 2, 3], [4, 5], [6]];

  let flattened = [].concat.apply([], arrays);

console.log(flattened)
const reduced = arrays.reduce((result,array) => result.concat(array),[]);

console.log(reduced);

// excercise two: your own loop
function loop(start, test, update, body) {
    for (let value = start; test(value); value = update(value)) {
      body(value);
    }
  }
 
  loop(3, n => n > 0, n => n - 1, console.log);

// excercise three: everything
function every(array, test) {
    for (let element of array) {
      if (test(element) === false) {
        return false;
      }
    }
    return true;
  }
console.log(every([1, 3, 5], n => n < 10));

console.log(every([2, 4, 16], n => n < 10));

console.log(every([], n => n < 10));
 // excercise four: Dominant writing direction

 function characterScript(code) {
    for (let script of SCRIPTS) {
      if (script.ranges.some(([from, to]) => {
        return code >= from && code < to;
      })) {
        return script;
      }
    }
    return null;
  }
  
  
  function countBy(items, groupName) {
    let counts = [];
    for (let item of items) {
      let name = groupName(item);
      let known = counts.findIndex(c => c.name == name);
      if (known == -1) {
        counts.push({name, count: 1});
      } else {
        counts[known].count++;
      }
    }
    return counts;
  }

 function dominantDirection(text) {
    const scripts = countBy(text, (char) => {
        const script = characterScript(char.codePointAt(0));
      
        return (script
          ? script.direction
          : "none"
        );
      })
        .filter(({name}) => name !== "none");
   
    if(scripts.length === 0){
      return "ltr";
    }
    
    console.log(scripts); 
    
    return scripts.reduce((a, b) => (a.count > b.count
      ? a
      : b)); 
  }
  var SCRIPTS = [
    {
      name: "Coptic",
      ranges: [[994, 1008], [11392, 11508], [11513, 11520]],
      direction: "ltr",
      year: -200,
      living: false,
      link: "https://en.wikipedia.org/wiki/Coptic_alphabet"
    }, 
    {
    name: "Arabic",
    ranges: [[1536, 1541], [1542, 1548], [1549, 1563], [1564, 1565], [1566, 1567], [1568, 1600], [1601, 1611], [1622, 1648], [1649, 1757], [1758, 1792], [1872, 1920], [2208, 2229], [2230, 2238], [2260, 2274], [2275, 2304], [64336, 64450], [64467, 64830], [64848, 64912], [64914, 64968], [65008, 65022], [65136, 65141], [65142, 65277], [69216, 69247], [126464, 126468], [126469, 126496], [126497, 126499], [126500, 126501], [126503, 126504], [126505, 126515], [126516, 126520], [126521, 126522], [126523, 126524], [126530, 126531], [126535, 126536], [126537, 126538], [126539, 126540], [126541, 126544], [126545, 126547], [126548, 126549], [126551, 126552], [126553, 126554], [126555, 126556], [126557, 126558], [126559, 126560], [126561, 126563], [126564, 126565], [126567, 126571], [126572, 126579], [126580, 126584], [126585, 126589], [126590, 126591], [126592, 126602], [126603, 126620], [126625, 126628], [126629, 126634], [126635, 126652], [126704, 126706]],
    direction: "rtl",
    year: 400,
    living: true,
    link: "https://en.wikipedia.org/wiki/Arabic_script"
      },
  ]
  console.log(dominantDirection("Hello!"));
// → ltr
console.log(dominantDirection("Hey, مساء الخير"));
// → rtl

// GRAPH
let  nodes = {
    'A': {'x': 100, 'y': 200},
    'B': {'x': 200, 'y': 100},
    'C': {'x': 200, 'y': 300},
  }
let adj_list = {
    'A': {'B': {'value': 1},
          'C': {'value': 2},
         },
    'C': {'B': {'value': 3},
         },
  }
let is_directed = true

const num_edges = (list) => {
    let count = 0;
    for (let x in list) {
        for (let y in list[x]) {
            count += 1
        }
    }
    return count
}
console.log(num_edges(adj_list))

const has_edge = (v1, v2) => {
    let list = adj_list
    for (let x in list) {
        if (v1 == x) {
            for (let y in list[x]) {
                if (v2 == y) {
                    return true;
                }
            }
        }
    } return false
}

console.log(has_edge('A', 'B'))

const print = () => {
    let string = "is_directed = " + is_directed + "\n"
    for (let node in nodes) {
        string += node + " "
        let x = nodes[node]['x']
        let y = nodes[node]['y']
        string+= "fx " + x + " fy " + y + "\n"
    }
    for (let node in adj_list) {
        for (let neighbor in adj_list[node]) {
            string+=node+neighbor + " value " + adj_list[node][neighbor]['value'] + "\n"
        }
    }
    console.log(string)
}
print()


  