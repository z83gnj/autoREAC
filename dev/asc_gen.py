#open text file
text_file = open("data.txt", "w")

torque = 1200
#write string to file
first_line = "Python Tutorial by TutorialKart.\n"
second_line = "This is a new line"
third_line = "Torque: "+ str(torque)

text_file.write(first_line + second_line + third_line)
 
#close file
text_file.close()