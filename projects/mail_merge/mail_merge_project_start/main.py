#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



    # def read_data(self):
    #     with open("data.txt",mode="r") as file:
    #         place_holder = file.read()
    #         self.high_score = int(place_holder)
    #
    # def update_scoreboard(self):
    #     self.clear()
    #     self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)
    #
    # def write_data(self):
    #     with open ("data.txt", mode="w") as file:
    #         place_holder2 = int(self.high_score)
    #         file.write(f"{place_holder2}")



f = open("../mail_merge_project_start/Input/Names/invited_names.txt","r")

# print(f.readlines())
list_of_names = f.readlines()


for i in list_of_names:
    with open ("../mail_merge_project_start/Input/Letters/starting_letter.txt", "r") as file_read:
        place_holder = file_read.read()

    with open (f"../mail_merge_project_start/Output/ReadyToSend/mail_to_be_send_to_{i}", "a") as file_creation:
        what_da_heli = place_holder.replace("[name]", str(i).strip())
        file_creation.write(what_da_heli)
    
    


