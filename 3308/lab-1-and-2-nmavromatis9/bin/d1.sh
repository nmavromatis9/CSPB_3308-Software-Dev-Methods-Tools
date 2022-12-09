#!/bin/bash

#Nicolas Mavromatis
#nima 6629

#Script to first check if 2 directories and 1 HTML file exist.
#If they do, extract the correct .txt files.

if [ -d Data/Year/"$1" ]; then
        echo ".../Year/"$1" exists"
        if [ -d Data/Year/"$1"/Game_"$2" ]; then
                echo ".../"$1"/Game_"$2" exists"
                if [ -f Data/Year/"$1"/Game_"$2"/game_"$2".html ]; then
                        echo ".../game_"$2".html exists"
			grep "clue_text" Data/Year/"$1"/Game_"$2"/game_"$2".html | sort > Data/Year/"$1"/Game_"$2"/clues.txt 
			grep "clue_text" Data/Year/"$1"/Game_"$2"/game_"$2".html | sort | grep "clue_J" | sort > Data/Year/"$1"/Game_"$2"/clues_J.txt 
			grep "clue_text" Data/Year/"$1"/Game_"$2"/game_"$2".html | sort | grep "clue_DJ" | sort > Data/Year/"$1"/Game_"$2"/clues_DJ.txt 
			grep "clue_text" Data/Year/"$1"/Game_"$2"/game_"$2".html | sort | grep "clue_FJ" | sort > Data/Year/"$1"/Game_"$2"/clues_FJ.txt 
			grep "category_name" Data/Year/"$1"/Game_"$2"/game_"$2".html | sort > Data/Year/"$1"/Game_"$2"/category.txt 
			wc -l Data/Year/"$1"/Game_"$2"/*.txt
                else
                        echo ".../game_"$2".html doesn't exist"
                fi
        else
                echo ".../"$1"/Game_"$2" doesn't exist"
        fi
else
        echo ".../Year/"$1" doesn't exist"
fi
