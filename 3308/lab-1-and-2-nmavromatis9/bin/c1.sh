#!/bin/bash

#Nicolas Mavromatis
#nima6629

#Script to create correct subdirectories and download HTML
#$1 is year
#$2 is game id

#check year is between 1983 and 2022
#check game_id is 3-4 digits
#if these are valid, create directories and download HTML

if [[ "$1" =~ ^1983|199[0-9]|20[01][0-9]|202[012]$ ]]; then
        echo "Year $1 is valid" 
        if [[ "$2" =~ ^[0-9]{3,4}$ ]]; then
                echo "Game $2 is valid"
                mkdir Data/Year/"$1"
                mkdir Data/Year/"$1"/Game_"$2"
		wget -O Data/Year/"$1"/Game_"$2"/game_"$2".html https://j-archive.com/showgame.php?game_id="$2"
        else
                echo "Game $2 is invalid"
        fi
else
        echo "Year $1 is invalid"
fi
