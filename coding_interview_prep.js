// Find the symmetric difference
function sym(args) {
  return args;
}

sym([1, 2, 3], [5, 2, 1, 4]);

// Inventory Update
function updateInventory(arr1, arr2) {
  return arr1;
}

// Example inventory lists
var curInv = [
  [21, "Bowling Ball"],
  [2, "Dirty Sock"],
  [1, "Hair Pin"],
  [5, "Microphone"]
];

var newInv = [
  [2, "Hair Pin"],
  [3, "Half-Eaten Apple"],
  [67, "Bowling Ball"],
  [7, "Toothpaste"]
];

updateInventory(curInv, newInv);

// No repeat please
function permAlone(str) {
  return str;
}

permAlone('aab');

// Pairwise
function pairwise(arr, arg) {
  return arg;
}

pairwise([1,4,2,3,0,5], 7);

// Perform an Intersection on Two Sets of Data
class Set {
  constructor() {
    // This will hold the set
    this.dictionary = {};
    this.length = 0;
  }
  // This method will check for the presence of an element and return true or false
  has(element) {
    return this.dictionary[element] !== undefined;
  }
  // This method will return all the values in the set
  values() {
    return Object.keys(this.dictionary);
  }
  // This method will add an element to the set
  add(element) {
    if (!this.has(element)) {
      this.dictionary[element] = true;
      this.length++;
      return true;
    }

    return false;
  }
  // This method will remove an element from a set
  remove(element) {
    if (this.has(element)) {
      delete this.dictionary[element];
      this.length--;
      return true;
    }

    return false;
  }
  // This method will return the size of the set
  size() {
    return this.length;
  }
  // This is our union method 
  union(set) {
    const newSet = new Set();
    this.values().forEach(value => {
      newSet.add(value);
    })
    set.values().forEach(value => {
      newSet.add(value);
    })

    return newSet;
  }
  // Only change code below this line
  
  // Only change code above this line
}

// Create a Priority Queue Class
function PriorityQueue () {
  this.collection = [];
  this.printCollection = function() {
    console.log(this.collection);
  };
  // Only change code below this line

  // Only change code above this line
}

// Create and Add to Sets in ES6
function checkSet() {
  var set = new Set([1, 2, 3, 3, 2, 1, 2, 3, 1]);
  // Only change code below this line

  // Only change code above this line
  console.log(Array.from(set));
  return set;
}

checkSet();

// Remove items from a set in ES6
function checkSet(){
  // Only change code below this line
  var set = null;

  // Only change code above this line
  return set;   
}

// Use .has and .size on an ES6 Set
function checkSet(arrToBeSet, checkValue){

  // Only change code below this line

  // Only change code above this line

}

// Use Spread and Notes for ES5 Set() Integration
function checkSet(set){
  // Only change code below this line

  // Only change code above this line
}

// Create a Map Data Structure
var Map = function() {
  this.collection = {};
  // Only change code below this line
  
  // Only change code above this line
};