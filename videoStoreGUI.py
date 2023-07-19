"""
Program: videoStoreGUI.py
Author: Jaclyn 7/18/2023

GUI-Based version of the Video Store project from Chapter 2
"""

from breezypythongui import EasyFrame
from tkinter.font import Font 
# Other Imports go here

# Class Header (Application name will change project to project)
class VideoStore(EasyFrame):
	# Definition of our class constructor method 
	def __init__(self): 

		EasyFrame.__init__(self, title = "Five Star Video", width = 340, height = 280, resizable = False, background = "lightyellow")
		self.normalFont = Font(family = "Tahoma", size = 16)

		# Add the various components to the window
		self.addLabel(text = "Five Star Video", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "darkred", foreground = "lightyellow", font = Font(family = "Arial", size = 26))
		self.addLabel(text = "New Rentals: $3.00\n Old Rentals: $2.00", row = 1, column = 0, columnspan =2, sticky = "NSEW", background = "lightyellow", font = self.normalFont)
		self.addLabel(text = "# of New Rentals:", row = 2, column = 0, sticky = "NE", background = "lightyellow", font = self.normalFont)
		self.newRentals = self.addIntegerField(value = 0, row = 2, column = 1, sticky ="NW", width = 4)
		self.addLabel(text = "# of Old Rentals", row = 3, column = 0, sticky = "NE", background = "lightyellow", font = self.normalFont)
		self.oldRentals = self.addIntegerField(value = 0, row = 3, column = 1, sticky = "NW", width = 4)

		self.button = self.addButton(text = "Calculate Total", row = 4, column = 0, columnspan = 2, command = self.calculate)
		self.addLabel(text = "The total for the order is: ", row = 5, column = 0, sticky = "NE", background = "darkred", foreground = "white", font = self.normalFont)
		self.total = self.addFloatField(value = 0.0, row = 5, column = 1, sticky = "NW", precision = 2, state = "readonly", width = 10)

	# Defintion of the Calculate() Function (Needs to be part of class)
	def calculate(self): 
		# Grab the User Input from the GUI Window
		new = self.newRentals.getNumber()
		old = self.oldRentals.getNumber()

		# Processing Phase
		result = (new * 3.00) + (old * 2.00)

		# Output Phase 
		self.total.setNumber(result)

		# Definition of the calculateSalary() Function
		def calculateSalary(self):
			hourly_pay = self.hourlyPay.getNumber()
			hours_worked = self.hoursWorked.getNumber()

			# Processing Phase
			totalSalary = (hourlyPay * hoursWorked)

			# Output Phase 

# Global definition of the main() method
def main():
	#Instantiates an object from the class into the mainloop()
	VideoStore().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()

