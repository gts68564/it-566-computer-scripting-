"""Implements Team Roster Operations"""
import json
import os
from datetime import date


class Roster(object):
    """Implements Team Roster Operations"""
    def __init__(self):
        # Constants
        self.NEW_ROSTER = '1'
        self.LOAD_ROSTER = '2'
        self.PRINT_ROSTER = '3'
        self.ADD_MEMBERS = '4'
        self.SAVE_ROSTER = '5'
        self.EXIT = '7'
        # Fields
        self.menu_choice = 1
        self.keep_going = True

        # input
        self.file = input("Enter the path to the file: ")
        self.data = None

    @staticmethod
    def clear_screen():
        os.system('cls')

    def new_roster(self):
        """Create new roster."""
        self.clear_screen()
        if __debug__:
            print('new_roster() method called...')
            roster_type = input("Enter the name of the new_roster: ")
            sport = input("Enter the name of the sport: ")
            country = input("Enter the country name: ")
            name = input("Enter the name of the member: ")
            age = int(input("Enter the age of the member: "))

            with open(self.file, "w") as rs:
                new = {'type': roster_type, 'date': date.today().strftime("%Y-%m-%d"), 'sport': sport,
                       'country': country, 'members': [{'name': name, 'age': age}]}
                json.dump(new, rs, indent=2)

    def load_roster(self):
        """Load roster from file."""
        self.clear_screen()
        if __debug__:
            print('load_roster() method called...')
            with open(self.file, "r") as rs:
                self.data = json.load(rs)

    def print_roster(self):
        """Print roster."""
        self.clear_screen()
        if __debug__:
            print("Print roster method is called...")
            Roster.load_roster(self)
            print(self.data)

    def save_roster(self):
        """Save roster to file."""
        self.clear_screen()
        if __debug__:
            print('save_roster() method called...')
            with open(self.file, "w") as rs:
                json.dump(self.data, rs, indent=2)

    def add_members(self):
        """Add items to roster."""
        self.clear_screen()
        if __debug__:
            print('Add members() method called...')
            name = input("Enter the name of the member:")
            age = int(input("Enter the age of the member:"))
            self.data["members"].append({'name': name, 'age': age})
