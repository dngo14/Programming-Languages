#!/usr/bin/node

let doh = "Doh";
console.log(typeof doh.toUpperCase);
console.log(doh.toUpperCase());
let sequence = [1, 2, 3];
sequence.push(4);
sequence.push(5);
console.log(sequence);
let day1 = {
    squirrel: false,
    events: ["work", "touched tree", "pizza", "running"]
  };
  console.log(day1.squirrel);
  let descriptions = {
    work: "Went to work",
    "touched tree": "Touched a tree"
  };

  let journal = [];

function addEntry(events, squirrel) {
  journal.push({events, squirrel});
}
addEntry(["work", "touched tree", "pizza", "running",
          "television"], false);
addEntry(["work", "ice cream", "cauliflower", "lasagna",
          "touched tree", "brushed teeth"], false);
addEntry(["weekend", "cycling", "break", "peanuts",
          "beer"], true);

          function journalEvents(journal) {
            let events = [];
            for (let entry of journal) {
              for (let event of entry.events) {
                if (!events.includes(event)) {
                  events.push(event);
                }
              }
            }
            return events;
          }
          
          //console.log(journalEvents(JOURNAL));
// Excercises

// Excercise One The sum of a range
function range(start, end, increment) {
    var array = [];
    var current = start;

    increment = increment || 1;
    if (increment > 0) {
        while (current <= end) {
            array.push(current);
            current += increment;
        }
    } else {
        while (current >= end) {
            array.push(current);
            current += increment;
        }
    }
    return array;
};

const sum = (list) => {
    let count = 0;
    for (item in list) {
        count += item;
    }
    return count;
};

console.log(range(1, 10));
console.log(range(5, 2, -1));

// Excercise 2 Reversing an array

function reverseArray(list) {
    let newlist = [];
    for (let x = list.length - 1; x >= 0; x -= 1) {
        newlist.push(list[x])
    }
    return newlist
};

function reverseArrayInPlace(array) {
    var i = 0,
      n = array.length,
      middle = Math.floor(n / 2),
      temp = null;

  for (; i < middle; i += 1) {
     temp = array[i];
     array[i] = array[n - 1 - i];
     array[n - 1 - i] = temp;
  }
}
console.log(reverseArray(["A", "B", "C"]));
// → ["C", "B", "A"];
let arrayValue = [1, 2, 3, 4, 5];
reverseArrayInPlace(arrayValue);
console.log(arrayValue);
// → [5, 4, 3, 2, 1]

// Excercise 3 A List
function arrayToList(arr) {
    var list = {};

 for (var i = 0; i < arr.length; i++) {
    list.value = arr.splice(0, 1)[0];
    list.rest = (arr.length > 0) ? arrayToList(arr) : null;
 }

 return list;
}

function listToArray(list) {
    var array = [];
    var item = list;
    while (item) {
        array.push(item.value);
        item = item.rest;
    }
    return array;
}

function prepend(element, list) {
    return {
      value: element,
      rest: list
    };
  }

  function nth(list, number) {
    if (number === 0) {
      return list.value;
    } else if (list.rest === null) {
      return undefined;
    } else {
      return nth(list.rest, number-1);
    }
  }

  console.log(arrayToList([10, 20]));
// → {value: 10, rest: {value: 20, rest: null}}
console.log(listToArray(arrayToList([10, 20, 30])));
// → [10, 20, 30]
console.log(prepend(10, prepend(20, null)));
// → {value: 10, rest: {value: 20, rest: null}}
console.log(nth(arrayToList([10, 20, 30]), 1));
// → 20

//Excercise 4 Deep comparison
function deepEqual(a, b) {
    if (a === b) {
      return true;
    } else if (typeof a === 'object' && a !== null && typeof b === 'object' && b !== null) {
      let keys = Object.keys(a).concat(Object.keys(b));
      keys = keys.filter(
        function (value, index, self) { 
          return self.indexOf(value) === index;
        }
      );
      for (p of keys) {
        if (typeof a[p] === 'object' && typeof b[p] === 'object') {
          if (deepEqual(a[p], b[p]) === false) {
            return false;
          }
        } else if (a[p] !== b[p]) {
          return false;
        }
      }
      return true;
    } else {
     return false; 
    }
  }

  let obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj));
// → true
console.log(deepEqual(obj, {here: 1, object: 2}));
// → false
console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));
// → true