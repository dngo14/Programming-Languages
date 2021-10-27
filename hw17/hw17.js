#!/usr/bin/node

function main() {
    console.log("hello!");
    let caught = 5 * 5;
    console.log(caught);
    let ten = 10;
    console.log(ten * ten);
    let mood = "light";
    console.log(mood);
    let luigisDebt = 140;
    luigisDebt = luigisDebt - 35;
    console.log(luigisDebt);
    let one = 1, two = 2;
    console.log(one + two);
    var name = "Ayda";
    const greeting = "Hello ";
    console.log(greeting + name);
    let x = 30;
    console.log("the value of x is", x);
    console.log(Math.max(2, 4));
    console.log(Math.min(2, 4) + 100);
    /*let theNumber = Number(prompt("Pick a number"));
if (!Number.isNaN(theNumber)) {
  console.log("Your number is the square root of " +
              theNumber * theNumber);
} */
if (1 + 1 == 2) console.log("It's true");
let number = 0;
while (number <= 12) {
  console.log(number);
  number = number + 2;
}
let result = 1;
let counter = 0;
while (counter < 10) {
  result = result * 2;
  counter = counter + 1;
}
console.log(result);
if (false != true) {
    console.log("That makes sense.");
    if (1 < 2) {
      console.log("No surprise there.");
    }
  }
  for (let number = 0; number <= 12; number = number + 2) {
    console.log(number);
  }
  /*let result = 1;
for (let counter = 0; counter < 10; counter = counter + 1) {
  result = result * 2;
}
console.log(result);
for (let current = 20; ; current = current + 1) {
    if (current % 7 == 0) {
      console.log(current);
      break;
    }
  }
  switch (prompt("What is the weather like?")) {
    case "rainy":
      console.log("Remember to bring an umbrella.");
      break;
    case "sunny":
      console.log("Dress lightly.");
    case "cloudy":
      console.log("Go outside.");
      break;
    default:
      console.log("Unknown weather type!");
      break;
  }*/
  }
  
  main()