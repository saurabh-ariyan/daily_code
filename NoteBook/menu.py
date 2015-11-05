import sys
from notebook import Note, Notebook

class Menu(object):
	"""Displya a menu and respond to choices when run"""
	def __init__(self):
		self.notebook = Notebook()
		self.choices = {
		"1": self.show_notes,
		"2": self.search_notes,
		"3": self.add_note,
		"4": self.modfiy_note,
		"5": self.quit

		}

	def display_menu(self):
		print("""
			Notebook Menu
			1. Show all notes 
			2. Search notes
			3. Add note
			4. Modify note
			5. Quit """
			)

	def run(self):
		'''Display the menu and respond to choices'''
		while True:
			self.display_menu()
			choice = input("Enter an option: ")
			action = self.choices.get(choice)
			if action:
				action()
			else:
				print ("{0} is not a valid choice.format(choice)")

	def show_notes(self):
		if not notes:
			notes = self.notebook.notes
		for note in notes:
			print ("{0}: in {1} \n {2}".format(note_id, note_tags, note.memo))

	