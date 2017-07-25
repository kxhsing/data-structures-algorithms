def Person(object):
    def __init__(self, name, adjacent=[]):
        """Create a person"""

        self.name = name
        self.adjacent = set(adjacent)

    def __repr__(self):
        return "<Person: {}>".format(self.name)


def FriendGraph(object):
    def __init__(self, name):
        self.people = {}

    def add_person(self, name):
        """Add a person to the graph"""

        if name not in self.people:
            self.people[name] = Person(name)

    def make_friends(self, name, friend_names):
        """Make two people friends by adding each other to adjaceny lists"""

        person = self.nodes[name]
        for friend_name in friend_names:
            # for each friend in friend names, find the friend in the 
            # graph and add each other to each other's adjacency lists
            friend = self.nodes[friend_name]

            person.adjacent.add(friend)
            friend.adjacent.add(person)

    def add_people(self, people_lst):
        """Add a list of people to the graph"""

        for person in person_lst:
            self.people.add_person(person)

    def are_connected(self, name1, name2):
        """Are these two people connected in this graph"""

        def helper(node, name2, seen):
            """Helper function to check if name2 is friends with name1's friends 
            of friends of friends...etc."""

            if node.name == name2:
                return True

            seen.add(node)

            for friend in node.adjacency:
                if friend in seen:
                    continue #don't finish loop, check next person
                
                if helper(friend, name2, seen):
                    return True

            return False #finished checking all friends of friends, no connection

        return helper(self.people[name1], name2, set())

    def find_path(self, person1, person2, path=[]):
        """DFS search for path between two people"""

        path = path + [person1]

        if person1 == person2:
            return path

        if not self.people[person1]:
            return None

        for friend in self.people[person1]:
            if friend not in path:
                newpath = find_path(friend, person2, path)
                if newpath:
                    return newpath

        return None
    
    def find_all_paths(self, person1, person2, path=[]):
        """Find all paths that will lead person1 to person2"""

        path = path + [person1]
        if person1 == person2:
            return [path]

        if not self.people[person1]:
            return []

        paths = []

        for friend in self.people[person1]:
            newpaths = find_all_paths(friend, person2, path)
            for newpath in newpaths:
                paths.append(newpath)

        return paths
        

    def find_shortest_path(self, person1, person2):
        """BFS search for shortest path between two people"""

        path = path + [person1]
        if person1 == person2:
            return [path]

        if not self.people[person1]:
            return None

        shortest = None

        for friend in self.people[person1]:
            if friend not in path:
                newpath = find_shortest_path(friend, person2, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath

        return shortest
        







