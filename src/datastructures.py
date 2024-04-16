
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
from flask import jsonify

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if member["last_name"] != self.last_name:

            return jsonify({"error":"Member last name is not {}".format(self.last_name)}),404

        self._members.append(member)  

        print(self._members)

        return jsonify({"lucky_numbers":member["lucky_numbers"],"age":int(member["age"]),"first_name":member["first_name"]}),200

        

    def delete_member(self, id):
        for  member in self._members:

            if member["id"] == id:
                self._members.remove(member)
                return jsonify({"message":"User Deleted Successfully"}),200

        return jsonify({"Error":"Member not Found"}),404

    def get_member(self, id):
        # fill this method and update the return

        for member in self._members:

            if member["id"] == id:
                return jsonify(member),200

        return jsonify({"Error":"Member not Found"}),404



    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
