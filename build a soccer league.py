#Divide 18 children into three even teams
#Dragons, Sharks, and Raptors
#Assign players so the experience level is the same on team
#Iterate through all three teams to generate a personalized letter to the guardians
#which team the child is on and when is their first practice
#Dragon March 17th 1 pm
#Shark Marth 17th 3 pm
#Raptors March 18th 1 pm
#Should create 18 letters

import csv


League = [{'Dragons':[]}, {'Sharks':[]}, {'Raptors':[]}]
dates = {"Dragons": "March 17, 1pm", "Sharks": "March 17, 3pm", "Raptors": "March 18, 1pm"}
experience = []
non_experience = []


#Take data from csv file and convert the date to be used

with open('soccer_players.csv', newline='') as csvfile:
    soccer_player_data = csv.DictReader(csvfile)
    data_rows_soccer_player = list(soccer_player_data)

#remove the row['Name'] later

def splitting_by_experience(data):
    for row in data_rows_soccer_player:
        if row['Soccer Experience'] == 'YES':
            experience.append(row)
        else:
            non_experience.append(row)

#Make sure to have the same number of experience players on each team

def team_list(experienced, non_experienced):
    count_exp= 0
    while count_exp < len(experience):
        for team in League:
            for key, value in team.items():
                team[key].append(experience[count_exp])
                count_exp += 1
    count_non_exp = 0
    while count_non_exp < len(non_experience):
        for team in League:
            for key, value in team.items():
                team[key].append(non_experience[count_non_exp])
                count_non_exp += 1
    return League

def write_letter():   
    for team in League:
        for key, value in team.items():
            for player in value:
                file = open("{}.txt".format(player['Name'].lower()), 'w')
                file.write("""Dear {}, \n
                Your child {} has been selected to play on team {}. \n
                 The first practice will be on {}. Please arrive on time! \n

                                             Sincerely, 
                                             League Soccer Commissioner""".format(player['Guardian Name(s)'], player['Name'], key, dates[key]))
                        

if __name__ == "__main__":
    splitting_by_experience(data_rows_soccer_player)
    team_list(experience, non_experience)
    write_letter()
                
