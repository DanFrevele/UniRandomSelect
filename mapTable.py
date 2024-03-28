import csv
import tkinter as tk
import customtkinter as ctk

def generateMapTable(frame,player_list,point_list,map_values):
    # initialize lists
    map_values.clear()

    # clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # read the map list csv file
    with (open('UniMaps.csv') as maplistcsv):
        map_list = csv.reader(maplistcsv, delimiter=',')
        # Keep track of index while adding maps
        x = 0

        # 0: Name
        # 1: Map Type
        # 2: Player Count
        # 3: Resource Availability
        for row in map_list:
            # add map if given players selected
            player2 = player_list[0].get() == 1 and row[2] == "2"
            player4 = player_list[1].get() == 1 and row[2] == "4"
            player6 = player_list[2].get() == 1 and row[2] == "6"
            player8 = player_list[3].get() == 1 and row[2] == "8"

            # add map if all of the selected points are available
            # if the point type is selected, make sure it's on the map
            # if it's not, auto-pass
            if point_list[0].get() == 1:
                if "R" in row[3]:
                    relic = 1
                else:
                    relic = 0
            else:
                relic = 1

            if point_list[1].get() == 1:
                if "C" in row[3]:
                    critical = 1
                else:
                    critical = 0
            else:
                critical = 1

            if point_list[2].get() == 1:
                if "S" in row[3]:
                    slag = 1
                else:
                    slag = 0
            else:
                slag = 1

            if (player2 or player4 or player6 or player8) and (relic and critical and slag):
                map_values.append([row[0],tk.IntVar(value=1)])
                full_map = row[0] + " " + row[2] + " " + row[3]
                button = ctk.CTkCheckBox(frame, text=full_map, variable=map_values[x][1]).pack(anchor=tk.W)
                x += 1

