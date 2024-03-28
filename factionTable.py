import tkinter as tk
import customtkinter as ctk

def generateSMTable(fname):
    spaceMarineValue = []

    smLabel = ctk.CTkLabel(fname, text = "Adeptus Astartes", pady=10).grid(row=0, column=0, columnspan=2)

    spaceMarineValue.append(["13th Company",tk.IntVar(value=1)])
    spaceMarineValue.append(["Black Templars",tk.IntVar(value=1)])
    spaceMarineValue.append(["Blood Angels",tk.IntVar(value=1)])
    spaceMarineValue.append(["Dark Angels",tk.IntVar(value=1)])
    spaceMarineValue.append(["Daemon Hunters",tk.IntVar(value=1)])
    spaceMarineValue.append(["Imperial Fists",tk.IntVar(value=1)])
    spaceMarineValue.append(["Legion of the Damned",tk.IntVar(value=1)])
    spaceMarineValue.append(["Salamanders",tk.IntVar(value=1)])
    spaceMarineValue.append(["Space Marines",tk.IntVar(value=1)])

    i = 2
    for x in spaceMarineValue:
        button = ctk.CTkCheckBox(fname, text=x[0], variable=x[1], fg_color="blue")
        button.grid(row=i, column=0, columnspan=2, sticky=tk.W)
        i += 1

    return spaceMarineValue

def generateImpTable(fname):
    imperiumValue = []

    impLabel = ctk.CTkLabel(fname, text="Imperium of Man", pady=10).grid(row=0, column=0, columnspan=2)

    imperiumValue.append(["Adeptus Mechanicus", tk.IntVar(value=1)])
    imperiumValue.append(["Death Korps of Krieg", tk.IntVar(value=1)])
    imperiumValue.append(["Imperial Guard", tk.IntVar(value=1)])
    imperiumValue.append(["Praetorian Guard", tk.IntVar(value=1)])
    imperiumValue.append(["Sisters of Battle", tk.IntVar(value=1)])
    imperiumValue.append(["Steel Legion", tk.IntVar(value=1)])
    imperiumValue.append(["Vostroyan Firstborn", tk.IntVar(value=1)])
    imperiumValue.append(["Witch Hunters", tk.IntVar(value=1)])

    i = 2
    for x in imperiumValue:
        button = ctk.CTkCheckBox(fname, text=x[0], variable=x[1], fg_color="firebrick4")
        button.grid(row=i, column=0, columnspan=2, sticky=tk.W)
        i += 1

    return imperiumValue

def generateChaosTable(fname):
    chaosValue = []

    cLabel = ctk.CTkLabel(fname, text="Forces of Chaos", pady=10).grid(row=0, column=0, columnspan=2)

    chaosValue.append(["Chaos Daemons", tk.IntVar(value=1)])
    chaosValue.append(["Chaos Marines", tk.IntVar(value=1)])
    chaosValue.append(["Death Guard", tk.IntVar(value=1)])
    chaosValue.append(["Emperor's Children", tk.IntVar(value=1)])
    chaosValue.append(["Fallen Angels", tk.IntVar(value=1)])
    chaosValue.append(["Night Lords", tk.IntVar(value=1)])
    chaosValue.append(["Renegade Guard", tk.IntVar(value=1)])
    chaosValue.append(["Thousand Sons", tk.IntVar(value=1)])
    chaosValue.append(["World Eaters", tk.IntVar(value=1)])

    i = 2
    for x in chaosValue:
        button = ctk.CTkCheckBox(fname, text=x[0], variable=x[1], fg_color="purple")
        button.grid(row=i,column=0,columnspan=2,sticky=tk.W)
        i += 1

    return chaosValue

def generateXenosTable(fname):
    xenosValue = []

    xLabel = ctk.CTkLabel(fname, text="Xenos", pady=10).grid(row=0,column=0,columnspan=2)

    xenosValue.append(["Dark Eldar", tk.IntVar(value=1)])
    xenosValue.append(["Eldar", tk.IntVar(value=1)])
    xenosValue.append(["Farsight Enclaves", tk.IntVar(value=1)])
    xenosValue.append(["Harlequins", tk.IntVar(value=1)])
    xenosValue.append(["Necrons", tk.IntVar(value=1)])
    xenosValue.append(["Orks", tk.IntVar(value=1)])
    xenosValue.append(["Tau Empire", tk.IntVar(value=1)])
    xenosValue.append(["Tyranids", tk.IntVar(value=1)])
    xenosValue.append(["Ynnari", tk.IntVar(value=1)])

    i = 2
    for x in xenosValue:
        button = ctk.CTkCheckBox(fname, text=x[0], variable=x[1], fg_color="green4")
        button.grid(row=i,column=0,columnspan=2,sticky=tk.W)
        i += 1

    return xenosValue

# Uncheck all boxes for a given faction set
def uncheckAll(tableValues):
    for x in tableValues:
        x[1].set(0)

# Check all boxes for a given faction set
def checkAll(tableValues):
    for x in tableValues:
        x[1].set(1)

