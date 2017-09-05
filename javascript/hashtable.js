function HashTable(size) {
  this.buckets = Array(size);
  this.numBuckets = this.buckets.length;
}

function HashNode(key, value, next) {
  this.key = key;
  this.value = value;
  this.next = next || null; //need to know next in case of collision
}

HashTable.prototype.hash = function(key) {
  var total = 0;
  for (var i=0; i < key.length; i++) {
    total += key.charCodeAt(i);
  }
  var bucket = total % this.numBuckets;
  return bucket;
};

HashTable.prototype.insert = function(key, value) {
  var index = this.hash(key);
  if (!this.buckets[index]) {
    this.buckets[index] = new HashNode(key, value);
  }
  else if (this.buckets[index].key === key) {
    this.buckets[index].value = value;
    // if we are updating a friend and that friend is the first node at this index. if not, proceed below
  }
  else {
    // if index is taken, use chaining (like a LL) in same index 
    var currentNode = this.buckets[index];
    while (currentNode.next) {
      if (currentNode.next.key === key) {
        //found friend we want to update
        currentNode.next.value = value;
        return; //after updating value, return so we break out of function and don't end up creating a new node below
      }
      currentNode = currentNode.next;
    }
    currentNode.next = new HashNode(key, value); 
    //once we've gotten out of while loop (meaning we've reached end of the chain and currentNode = last node in chain, we create a new hash node at the end of chain at this index)
  }
};

HashTable.prototype.get = function(key) {
  var index = this.hash(key);
  if (!this.buckets[index]) return null;
  else {
    var currentNode = this.buckets[index];
    while (currentNode) {
      // we aren't concerned about currentNode.next because we aren't trying to insert and need to find last one in chain; we are just searching thru existing nodes
      if (currentNode.key === key) return currentNode.value;
      currentNode = currentNode.next;
    }
    return null;
  }
};

HashTable.prototype.retrieveAll = function() {
  var allNodes = [];
  for (var i=0; i < this.numBuckets; i++) {
    var currentNode = this.buckets[i];
    while (currentNode) {
      allNodes.push(currentNode);
      currentNode = currentNode.next;
    }
  }
  return allNodes;
};


// Testing
var myHT = new HashTable(30);
myHT.insert('Karen', 'karen@domain.com');
myHT.insert('Jesse', 'jesse@domain.com');
myHT.insert('Nerak', 'nerak@domain.com'); //collision

//test updating emails
myHT.insert('Karen', 'karen@gmail.com');
myHT.insert('Nerak', 'nerak@gmail.com');
myHT.insert('Jesse', 'jesse@gmail.com');
myHT.insert('Push', 'pusheen@gmail.com');
myHT.insert('Cora', 'cora@gmail.com');

// console.log(myHT.hash("hello!"));
// console.log(myHT.buckets);
// console.log(myHT.get('Karen'));
console.log(myHT.retrieveAll());
// console.log("hello".charCodeAt(4)); //charCodeAt JS method gives unicode value (numerical) of letters