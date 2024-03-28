# main.py

import tkinter as tk
from tkinter import messagebox as tkmb
import customtkinter as ctk
import factionTable as ft
import mapTable as mt
import random

# Takes a random selection from the selected values of the Faction and Map lists
def randomize_skirmish(frame,button2,button4,button6,factionList,mapList):

    # initialize lists
    selected_factions = []
    selected_maps = []

    # clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # pull out the names of those factions that have been checked
    for item in factionList:
        if item[1].get() == 1:
            selected_factions.append(item[0])

    if len(selected_factions) < 1:
        tkmb.showwarning("Empty List","You must have at least one faction selected")
        pass

    # randomly select factions and display them. Always generate 6, only use what's selected
    factions = []

    i = 0
    while i < 6:
        rdm_select = random.randrange(len(selected_factions))
        factions.append(selected_factions[rdm_select])
        i += 1

    versus_string = factions[0] + " VS " + factions[1]

    if button4.cget("fg_color") == "green":
        versus_string += "\n VS " + factions[2] + " VS " + factions[3]
    elif button6.cget("fg_color") == "green":
        versus_string += "\n VS " + factions[2] + " VS " + factions[3]
        versus_string += "\n VS " + factions[4] + " VS " + factions[5]

    label = ctk.CTkLabel(frame, text=versus_string).pack()

    # pull out the names of those maps that have been checked
    for item in mapList:
        if item[1].get() == 1:
            selected_maps.append(item[0])

    if len(selected_maps) < 1:
        tkmb.showwarning("Empty List", "You must have at least one map selected")
        pass

    # randomly select one map and display it
    rdm_select = random.randrange(len(selected_maps))
    label2 = ctk.CTkLabel(frame, text="ON").pack()
    label3 = ctk.CTkLabel(frame, text=selected_maps[rdm_select]).pack()

def select_players(selection, check2, check4, check6, check8, button2, button4, button6,refresh_button):

    if selection == 2:
        check2.select()
        check2.configure(state=tk.NORMAL)
        check4.configure(state=tk.NORMAL)
        check6.configure(state=tk.NORMAL)
        check8.configure(state=tk.NORMAL)
        button2.configure(fg_color="green")
        button4.configure(fg_color="dodgerblue4")
        button6.configure(fg_color="dodgerblue4")
    elif selection == 4:
        check2.deselect()
        check2.configure(state=tk.DISABLED)
        check4.select()
        check4.configure(state=tk.NORMAL)
        check6.configure(state=tk.NORMAL)
        check8.configure(state=tk.NORMAL)
        button2.configure(fg_color="dodgerblue4")
        button4.configure(fg_color="green")
        button6.configure(fg_color="dodgerblue4")

    elif selection == 6:
        check2.deselect()
        check2.configure(state=tk.DISABLED)
        check4.deselect()
        check4.configure(state=tk.DISABLED)
        check6.select()
        check6.configure(state=tk.NORMAL)
        check8.configure(state=tk.NORMAL)
        battle2.configure(fg_color="dodgerblue4")
        battle4.configure(fg_color="dodgerblue4")
        battle6.configure(fg_color="green")

    refresh_button.invoke()


# #######################BEGIN MAIN##########################
# set up tkinter and main frame
root = ctk.CTk()
root.geometry("1000x800")

# top_frame holds the main button and labels
top_frame = ctk.CTkFrame(root)
top_frame.pack()

# rs_frame holds the generated skirmish text
rs_frame = ctk.CTkFrame(root)
rs_frame.pack()
rs_label = ctk.CTkLabel(rs_frame, text="").pack()

# set up left and right frames
faction_frame = ctk.CTkFrame(root)
faction_frame.pack(fill=tk.Y, side=tk.LEFT)

map_frame = ctk.CTkFrame(root)
map_frame.pack(fill=tk.Y, side=tk.RIGHT)

# set up sub-frames for factions
imp_frame = ctk.CTkFrame(faction_frame)
imp_frame.grid(row=1, column=0, sticky=tk.NW, pady=1)

sm_frame = ctk.CTkFrame(faction_frame)
sm_frame.grid(row=2, column=0, sticky=tk.NW, pady=1)

ch_frame = ctk.CTkFrame(faction_frame)
ch_frame.grid(row=1, column=1, sticky=tk.NW, pady=1)

x_frame = ctk.CTkFrame(faction_frame)
x_frame.grid(row=2, column=1, sticky=tk.NW, pady=1)

# label and option buttons for maps
labelMap = ctk.CTkLabel(map_frame, text="Select Maps")
labelMap.pack()

# defaults to 2 player maps only and Relic and Critical available
players_list = [tk.IntVar(value=1), tk.IntVar(value=0), tk.IntVar(value=0), tk.IntVar(value=0)]
points_list = [tk.IntVar(value=1), tk.IntVar(value=1), tk.IntVar(value=0)]

refresh_maps_button = ctk.CTkButton(map_frame, text="Refresh Map List",
                                    command=lambda: mt.generateMapTable(map_list_frame, players_list, points_list, mapValues))
refresh_maps_button.pack()

player_buttons_frame = ctk.CTkFrame(map_frame)
player_buttons_frame.pack()

point_buttons_frame = ctk.CTkFrame(map_frame)
point_buttons_frame.pack()

map_list_frame = ctk.CTkScrollableFrame(map_frame)
map_list_frame.pack(expand=1,fill=tk.Y)

players_label = ctk.CTkLabel(player_buttons_frame, text="Map Player Size")
players2_check = ctk.CTkCheckBox(player_buttons_frame, text="2", variable=players_list[0])
players4_check = ctk.CTkCheckBox(player_buttons_frame, text="4", variable=players_list[1])
players6_check = ctk.CTkCheckBox(player_buttons_frame, text="6", variable=players_list[2])
players8_check = ctk.CTkCheckBox(player_buttons_frame, text="8", variable=players_list[3])

players_label.grid(row=0, column=0, columnspan=4)
players2_check.grid(row=1,column=0)
players4_check.grid(row=1, column=1)
players6_check.grid(row=1, column=2)
players8_check.grid(row=1, column=3)

points_label = ctk.CTkLabel(point_buttons_frame, text="Special Point Availability")
relic_button = ctk.CTkCheckBox(point_buttons_frame, text="Relic", variable=points_list[0])
critical_button = ctk.CTkCheckBox(point_buttons_frame, text="Critical", variable=points_list[1])
slag_button = ctk.CTkCheckBox(point_buttons_frame, text="Slag", variable=points_list[2])

points_label.grid(row=2, column=0, columnspan=3)
relic_button.grid(row=3, column=0)
critical_button.grid(row=3, column=1)
slag_button.grid(row=3, column=2)

# Set up title labels
creditLabel = ctk.CTkLabel(top_frame, text="made by DavionStar")
creditLabel.pack()

versionLabel = ctk.CTkLabel(top_frame, text="v0.01 for Unification 7.0")
versionLabel.pack()

labelFac = ctk.CTkLabel(faction_frame, text="Select Factions")
labelFac.grid(row=0, column=0, columnspan=2)

# generate faction tables, all initially set to checked
impValues = ft.generateImpTable(imp_frame)
smValues = ft.generateSMTable(sm_frame)
chaosValues = ft.generateChaosTable(ch_frame)
xenosValues = ft.generateXenosTable(x_frame)

# combine all tables into one for randomizeSkirmish
factionValues = smValues + impValues + chaosValues + xenosValues

# generate map table, all initially set to checked
mapValues = []
mt.generateMapTable(map_list_frame, players_list, points_list, mapValues)

# setup enable/disable all buttons
# Imperium of Man
impDisableAll = ctk.CTkButton(imp_frame, text="Pick None", width=100, fg_color="firebrick4",
                              command=lambda: ft.uncheckAll(impValues))
impDisableAll.grid(row=1, column=0)

impEnableAll = ctk.CTkButton(imp_frame, text="Pick All", width=100, fg_color="firebrick4",
                             command=lambda: ft.checkAll(impValues))
impEnableAll.grid(row=1, column=1)

# Adeptus Astartes
smDisableAll = ctk.CTkButton(sm_frame, text="Pick None", width=100, fg_color="blue",
                             command=lambda: ft.uncheckAll(smValues))
smDisableAll.grid(row=1, column=0)

smEnableAll = ctk.CTkButton(sm_frame, text="Pick All", width=100, fg_color="blue",
                            command=lambda: ft.checkAll(smValues))
smEnableAll.grid(row=1, column=1)

# Forces of Chaos
chDisableAll = ctk.CTkButton(ch_frame, text="Pick None", width=100, fg_color="purple",
                             command=lambda: ft.uncheckAll(chaosValues))
chDisableAll.grid(row=1, column=0)

chEnableAll = ctk.CTkButton(ch_frame, text="Pick All", width=100, fg_color="purple",
                            command=lambda: ft.checkAll(chaosValues))
chEnableAll.grid(row=1, column=1)

# Xenos
xDisableAll = ctk.CTkButton(x_frame, text="Pick None", width=100, fg_color="green4",
                            command=lambda: ft.uncheckAll(xenosValues))
xDisableAll.grid(row=1, column=0)

xEnableAll = ctk.CTkButton(x_frame, text="Pick All", width=100, fg_color="green4",
                           command=lambda: ft.checkAll(xenosValues))
xEnableAll.grid(row=1, column=1)

# set up the Player buttons to pick the amount of players/ai that will be fighting
battle_frame = ctk.CTkFrame(top_frame)
battle_frame.pack()

battle_label = ctk.CTkLabel(battle_frame, text="Number of Players")
battle2 = ctk.CTkButton(battle_frame, text="2", fg_color="green",
                        command=lambda: select_players(2,players2_check,players4_check,players6_check,players8_check,battle2,battle4,battle6,refresh_maps_button))
battle4 = ctk.CTkButton(battle_frame, text="4", fg_color="dodgerblue4",
                        command=lambda: select_players(4,players2_check,players4_check,players6_check,players8_check,battle2,battle4,battle6,refresh_maps_button))
battle6 = ctk.CTkButton(battle_frame, text="6", fg_color="dodgerblue4",
                        command=lambda: select_players(6,players2_check,players4_check,players6_check,players8_check,battle2,battle4,battle6,refresh_maps_button))

battle2.grid(row=1, column=0)
battle4.grid(row=1, column=1)
battle6.grid(row=1, column=2)
battle_label.grid(row=0, column=0, columnspan=3)

# setup the Generate Skirmish button which will randomly select factions and a map
randoBttn = ctk.CTkButton(top_frame, text="Generate Skirmish", command=lambda: randomize_skirmish(rs_frame,battle2,battle4,battle6,factionValues,mapValues)).pack()

# set title and run
root.title("Unification Random Selector")
root.mainloop()
