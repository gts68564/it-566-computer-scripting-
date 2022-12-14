"""Implements household roster control features."""

from roster import Roster
from subprocess import call
import os


class RosterApp(Roster):
	"""Implements household roster control features."""

	def display_menu(self):
		"""Display menu."""
		print('\t\t\tTeam Roster Application')
		print()
		print('\t\t1. New Roster')
		print('\t\t2. Load Roster')
		print('\t\t3. Print Roster')
		print('\t\t4. Add Team Members to Roster')
		print('\t\t5. Save Roster')
		print('\t\t7. Exit')
		print()

	def process_menu_choice(self):
		"""Process menu choice and execute corresponding methods."""
		self.menu_choice = input('Please enter menu item number: ')
		if __debug__:
			print(f'You entered: {self.menu_choice}')
		match self.menu_choice:
			case self.NEW_ROSTER:
				self.new_roster()
			case self.LOAD_ROSTER:
				self.load_roster()
			case self.PRINT_ROSTER:
				self.print_roster()
			case self.ADD_MEMBERS:
				self.add_members()
			case self.SAVE_ROSTER:
				self.save_roster()
			case self.EXIT:
				if __debug__:
					print('Goodbye!')
				self.keep_going = False
				self.clear_screen()
			case _:
				self.clear_screen()
				print('Invalid Menu Choice!')

	def start_application(self):
		"""Start the applications."""
		# Clear Screen
		self.clear_screen()
		while self.keep_going:
			self.display_menu()
			self.process_menu_choice()
