"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # Example list of members
        self._members = [{"id": 123,
                          "first_name": "John",
                          "last_name": last_name,
                          "age": 33,
                          "sports": ["rugby", "golf"]},
                         {"id": 456,
                          "first_name": "Jane",
                          "last_name": last_name,
                          "age": 35,
                          "sports": ["running", "tennis", "surf"]},
                         {"id": 789,
                          "first_name": "Jimmy",
                          "last_name": last_name,
                          "age": 5,
                          "sports": ["soccer", "paddle", "boxing"]}]

    def __repr__(self):
        return '<family: %r>' % self.last_name

    def add_member(self, member):
        """
        Add a member to the self._members list
        :param member: dict {first_name: string,
                             age: int
                             sports: list}
        :return: list of members
        """
        # Fill this method and update the return
        member["id"] = randint(0, 99999999)
        member["last_name"] = self.last_name
        self._members.append(member)
        return self._members

    def delete_member(self, member_id):
        """
        Delete a member from the self._members list
        :param member_id:
        :return: list of members
        """
        # Opción 1: Standard
        members = []
        for member in self._members:
            if member["id"] != member_id:
                members.append(member)
        # Opción 2: lambda function
        # members =list(filter(lambda member: member["id"] != member_id, self._members))
        # Opción 3: list comprehension
        # members = [member for member in self._members if member["id"] != member_id]
        self._members = members
        return self._members

    # Return a member from the self._members list
    def get_member(self, member_id):
        # Opción 1: Standard
        members = []
        for member in self._members:
            if member["id"] == member_id:
                members.append(member)
        # Opción 2: lambda function
        # members = list(filter(lambda member: member["id"] == member_id, self._members ))
        # Opción 3: list comprehension
        # members = [member for member in self._members if member["id"] == member_id]
        return members

    # Returns a list with all the family members
    def get_all_members(self):
        return self._members

    # TODO: update a member from the self._members list


jackson_family = FamilyStructure("Jackson")
print(jackson_family)
print(jackson_family.get_all_members())
print(jackson_family.get_member(1234))
print(jackson_family.delete_member(1234))

new_member = {'first_name': 'Ann',
              'age': 9,
              "sports": ["climbing", "yoga"]}
print(jackson_family.add_member(new_member))
