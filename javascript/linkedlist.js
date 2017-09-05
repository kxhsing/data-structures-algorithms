function LinkedList() {
  this.head = null;
  this.tail = null;
}

function Node(value, next, prev) {
  this.value = value;
  this.next = next;
  this.prev = prev;
}

// LL functions

LinkedList.prototype.addToHead = function(value) {
  var newNode = new Node(value, this.head, null);
  if (this.head) {
    this.head.prev = newNode; //'this' is referring to LinkedList constructor since we are in the LinkedList prototype adding a function
  }
  else {
    this.tail = newNode; //if LL was empty, set tail to new node
  }
  this.head = newNode; //in either case, new node is now the head
}

LinkedList.prototype.addToTail = function(value) {
  var newNode = new Node(value, null, this.tail);
  if (this.tail) this.tail.next = newNode;
  else this.head = newNode;
  this.tail = newNode;
}

LinkedList.prototype.removeHead = function() {
  if (!this.head) return null;
  var val = this.head.value; //saving the current head's value
  this.head = this.head.next;
  if (this.head) this.head.prev = null;
  else this.tail = null; //if we removed the only node in ll
  return val;
}

LinkedList.prototype.removeTail = function() {
  if (!this.tail) return null;
  var val = this.tail.value;
  this.tail = this.tail.prev;
  if (this.tail) this.tail.next = null;
  else this.head = null; // if we deleted only node in ll
  return val;
}

LinkedList.prototype.search = function(searchVal) {
  var currentNode = this.head;
  while (currentNode) {
    if (currentNode.value === searchVal) return currentNode.value;
    currentNode = currentNode.next;
  }
  return null; //if traversed LL and can't find it
}

LinkedList.prototype.indexOf = function(val) {
  var index = 0;
  var result = [];
  var currentNode = this.head;
  while (currentNode) {
    if (currentNode.value === val) result.push(index);
    index++;
    currentNode = currentNode.next;
  }
  return result;
}

//Testing it out
var ll = new LinkedList();
// ll.addToTail(10);
// ll.addToTail(20);
ll.addToTail(40);
ll.addToHead(100);
ll.addToHead("hello");
ll.addToTail("world");
// ll.addToHead(200);
// ll.addToHead(300);
// ll.removeHead();
// ll.removeTail();
console.log(ll.indexOf("world"));