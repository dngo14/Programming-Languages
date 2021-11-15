#!/usr/bin/node

let rabbit = {};
rabbit.speak = function(line) {
  console.log(`The rabbit says '${line}'`);
};

rabbit.speak("I'm alive.");

function speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  }
  let whiteRabbit = {type: "white", speak};
  let hungryRabbit = {type: "hungry", speak};
  
  whiteRabbit.speak("Oh my ears and whiskers, " +
                    "how late it's getting!");
hungryRabbit.speak("I could use a carrot right now.");

let protoRabbit = {
    speak(line) {
      console.log(`The ${this.type} rabbit says '${line}'`);
    }
  };
  let killerRabbit = Object.create(protoRabbit);
  killerRabbit.type = "killer";
  killerRabbit.speak("SKREEEE!");

  function makeRabbit(type) {
    let rabbit = Object.create(protoRabbit);
    rabbit.type = type;
    return rabbit;
  }

  function Rabbit(type) {
    this.type = type;
  }

  Rabbit.prototype.speak = function(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  };
  
  let weirdRabbit = new Rabbit("weird");

  let blackRabbit = new Rabbit("black");

const toStringSymbol = Symbol("toString");
Array.prototype[toStringSymbol] = function() {
  return `${this.length} cm of blue yarn`;
};

console.log([1, 2].toString());

class Matrix {
    constructor(width, height, element = (x, y) => undefined) {
      this.width = width;
      this.height = height;
      this.content = [];
  
      for (let y = 0; y < height; y++) {
        for (let x = 0; x < width; x++) {
          this.content[y * width + x] = element(x, y);
        }
      }
    }
  
    get(x, y) {
      return this.content[y * this.width + x];
    }
    set(x, y, value) {
      this.content[y * this.width + x] = value;
    }
  }

  class MatrixIterator {
    constructor(matrix) {
      this.x = 0;
      this.y = 0;
      this.matrix = matrix;
    }
  
    next() {
      if (this.y == this.matrix.height) return {done: true};
  
      let value = {x: this.x,
                   y: this.y,
                   value: this.matrix.get(this.x, this.y)};
      this.x++;
      if (this.x == this.matrix.width) {
        this.x = 0;
        this.y++;
      }
      return {value, done: false};
    }
  }

  class Temperature {
    constructor(celsius) {
      this.celsius = celsius;
    }
    get fahrenheit() {
      return this.celsius * 1.8 + 32;
    }
    set fahrenheit(value) {
      this.celsius = (value - 32) / 1.8;
    }
  
    static fromFahrenheit(value) {
      return new Temperature((value - 32) / 1.8);
    }
  }
  
  let temp = new Temperature(22);
  console.log(temp.fahrenheit);

  class SymmetricMatrix extends Matrix {
    constructor(size, element = (x, y) => undefined) {
      super(size, size, (x, y) => {
        if (x < y) return element(y, x);
        else return element(x, y);
      });
    }
  
    set(x, y, value) {
      super.set(x, y, value);
      if (x != y) {
        super.set(y, x, value);
      }
    }
  }
  
  let matrix = new SymmetricMatrix(5, (x, y) => `${x},${y}`);
  console.log(matrix.get(2, 3));

  // Excercise One A Vector Type
  class Vec {
    constructor (x, y) {
      this.x = x;
      this.y = y;
    }
    plus(v) {
      return new Vec(this.x + v.x, this.y + v.y);
    }
    minus(v) {
      return new Vec(this.x - v.x, this.y - v.y);
    }
    get length() {
      return Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2));
    }
  }
  console.log(new Vec(1, 2).plus(new Vec(2, 3)));
  // → Vec{x: 3, y: 5}
  console.log(new Vec(1, 2).minus(new Vec(2, 3)));
  // → Vec{x: -1, y: -1}
  console.log(new Vec(3, 4).length);
  // → 5

// Excercise Two Groups
class Group {
    constructor() {
      this.group = [];
    }
    add(item) {
      if (!this.group.includes(item)) {
        this.group.push(item);
      }
    }
    delete(item) {
      let index = this.group.indexOf(item);
      if (index !== -1) {
        this.group.splice(index, 1);
      }
    }
    has(item) {
      return this.group.includes(item);
    }
    static from(a) {
      let g = new Group();
      for (let item of a) {
        g.add(item);
      }
      return g;
    }
  }
  
  let group = Group.from([10, 20]);
  console.log(group.has(10));
  console.log(group.has(30));
  group.add(10);
  group.delete(10);
  console.log(group.has(10));

// Excercise Three
class Group2 {
    constructor() {
      this.group = [];
    }
    add(item) {
      if (!this.group.includes(item)) {
        this.group.push(item);
      }
    }
    delete(item) {
      let index = this.group.indexOf(item);
      if (index !== -1) {
        this.group.splice(index, 1);
      }
    }
    has(item) {
      return this.group.includes(item);
    }
    static from(a) {
      let g = new Group2();
      for (let item of a) {
        g.add(item);
      }
      return g;
    }
    [Symbol.iterator]() {
      return new GroupIterator(this);
    };
  }
  
  class GroupIterator {
    constructor(o) {
      this.i = 0;
      this.group = o.group;
    }
  
    next() {
      if (this.i == this.group.length || this.i > 10) return {done: true};
  
      let value = this.group[this.i];
      this.i++;
      return {value, done: false};
    }
  }
  
  for (let value of Group2.from(["a", "b", "c"])) {
    console.log(value);
  }

  // Excercise 4 Borrwoing A Method
  let map = {one: true, two: true, hasOwnProperty: true};
  console.log(hasOwnProperty.call(map, 'one'));