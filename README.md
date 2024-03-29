This application is a supporting tool for a modification to the video game Warhammer 40,000 Dawn of War. The Unification Mod adds many new factions to this strategy game as well as new maps. The aging game has no way of randomizing map choice, and some players don't want to play against certain factions for one reason or another, so I created this tool.

The application lists all available factions from the original Dawn of War: Soulstorm and the plethora of new factions added by the Unification Mod, allowing the user to enable or disable factions at their whim, while also including buttons to quickly disable or enable all factions within a group. You can even set the number of players to randomize. 2, 4, or 6 are available in the current version.

The map selection pulls data off of a .csv file with a compiled list of all the maps available in the mod, the maximum amount of players allowed on the map, and the availability of specific resources. This allows the user to search for maps to their liking and have them in a pool for random selection.
The .csv file is also editable so the user can add or remove maps from the overall pool.

Error checking is included to catch any possibility of empty lists being passed through functions.

The application does not require the game to be installed and runs independently. Currently requires the user to have Python installed but will soon be made to be self-contained.
