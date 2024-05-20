"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name, country):
        self.last_name = last_name
        self.country = country
        # Example list of members
        self._members = []

    def __repr__(self):
        return '< Esta representa a la familia: %r >' % self.last_name

    def add_member(self, member):
        """
        Description: Add a member to the self._members list
        :param member: dict {first_name: string,
                             age: int,
                             sports: list}
        :return: list of members
        """
        # Fill this method and update the return
        member["id"] = randint(0, 99999999)
        member["last_name"] = self.last_name
        member["country"] = self.country
        self._members.append(member)
        return self._members

    def delete_member(self, member_id):
        """
        Delete a member from the self._members list
        :param member_id:
        :return: list of members
        """
        # Opción 1: Standard
        # members = []
        # for member in self._members:
        #     if member["id"] != member_id:
        #         members.append(member)
        # Opción 2: lambda function
        # members = list(filter(lambda member: member["id"] != member_id, self._members))
        # Opción 3: list comprehension
        # result for item in list   if condition
        members = [member for member in self._members if member["id"] != member_id]
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

    def get_country(self):
        return self.country
    # TODO: update a member from the self._members list


jackson_family = FamilyStructure("Jackson", "US")
torres_family = FamilyStructure("Torres", "Spain")
print(jackson_family)
# print(jackson_family.get_all_members())
# print(torres_family.get_all_members())
print(torres_family.get_country())
# print(jackson_family.get_member(1234))
new_member = {'first_name': 'Ann',
              'age': 9,
              "sports": ["climbing", "yoga"]}
print("Jackson", jackson_family.add_member(new_member))
print("Torres", torres_family.get_all_members())
# print(jackson_family.delete_member(123))
# print(jackson_family.delete_member(456))

# print(torres_family.add_member(new_member))
