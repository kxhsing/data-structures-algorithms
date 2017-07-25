class Person(object):
    def __init__(self, name, adjacent=[]):
        """Create a person"""

        self.name = name
        self.adjacent = set(adjacent)

    def __repr__(self):
        return "<Person: {}>".format(self.name)


class FriendGraph(object):
    def __init__(self):
        self.people = {}

    def __repr__(self):
        return "<Friendship Graph>"

    def add_person(self, name):
        """Add a person to the graph"""

        if name not in self.people:
            self.people[name] = Person(name)

    def add_people(self, people_lst):
        """Add a list of people to the graph"""

        for person in people_lst:
            self.add_person(person)

    def get_people(self):
        """Get all people in the graph"""

        if self.people:
            return self.people.keys()

    def make_friends(self, name, friend_names):
        """Make two people friends by adding each other to adjaceny lists"""

        person = self.people[name]
        for friend_name in friend_names:
            # for each friend in friend names, find the friend in the 
            # graph and add each other to each other's adjacency lists
            friend = self.people[friend_name]

            person.adjacent.add(friend)
            friend.adjacent.add(person)


    def are_connected(self, name1, name2):
        """Are these two people connected in this graph"""

        def helper(node, name2, seen):
            """Helper function to check if name2 is friends with name1's friends 
            of friends of friends...etc."""

            if node.name == name2:
                return True

            seen.add(node)

            for friend in node.adjacent:
                if friend in seen:
                    continue #don't finish loop, check next person
                
                if helper(friend, name2, seen):
                    return True

            return False #finished checking all friends of friends, no connection

        return helper(self.people[name1], name2, set())

    def find_path(self, name1, name2, path=[]):
        """DFS search for path between two people"""

        path = path + [name1]

        if name1 == name2:
            return path

        if name1 not in self.people:
            return None

        for friend in self.people[name1].adjacent:
            if friend.name not in path:
                newpath = self.find_path(friend.name, name2, path)
                if newpath:
                    return newpath

        return None
    
    def find_all_paths(self, name1, name2, path=[]):
        """Find all paths that will lead person1 to person2"""

        path = path + [name1]
        if name1 == name2:
            return [path]

        if name1 not in self.people:
            return []

        paths = []

        for friend in self.people[name1].adjacent:
            if friend.name not in path:
                newpaths = self.find_all_paths(friend.name, name2, path)
                for newpath in newpaths:
                    paths.append(newpath)

        return paths
        

    def find_shortest_path(self, name1, name2, path=[]):
        """BFS search for shortest path between two people"""

        all_paths = self.find_all_paths("tomato", "onion")
        min_path = all_paths[0]
        min_path_len = len(all_paths[0])

        for path in all_paths[1:]:
            if len(path) < min_path_len:
                min_path = path
                min_path_len = len(min_path)

        return min_path


        # path = path + [name1]
        # if name1 == name2:
        #     return [path]

        # if name1 not in self.people:
        #     return None

        # shortest = None

        # for friend in self.people[name1].adjacent:
        #     if friend.name not in path:
        #         newpath = self.find_shortest_path(friend.name, name2, path)
        #         if newpath:
        #             if not shortest or len(newpath) < len(shortest):
        #                 shortest = newpath

        # return shortest



friendship = FriendGraph()
friendship.add_people(["apple", "berry", "cherry", "elderberry", "onion"])
friendship.make_friends("apple", ["berry", "onion"])
friendship.add_person("asparagus")
friendship.add_people(["celery", "parsnip", "avocado"])
friendship.add_person("tomato")
friendship.make_friends("tomato", ["avocado", "onion", "apple"])
friendship.make_friends("avocado", ["onion"])
friendship.make_friends("onion", ["berry", "parsnip"])

print friendship.find_path("tomato", "onion")
print friendship.find_all_paths("tomato", "onion")
print friendship.find_shortest_path("tomato", "onion")



        







