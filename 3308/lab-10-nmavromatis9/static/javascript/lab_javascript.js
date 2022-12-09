//Modified and commented by: Nicolas Mavromatis, Nima6629

//CUSTOM MODIFICATIONS:###################################################
//1. Copy (ctl+C) works as expected (couldn't get paste to work)
//2. Delete (as well as backspace) work as expected
//3.Random Challenge button added, with associated listener and function. This creates a random 6 char string to match.

//Timer function:
//The timer is hidden until the user matches the target string.
//Then, the time for each challenge level that is completed is displayed.
//The timer is reset upon starting a new challenge, starting a random challenge, or hitting restart button (that goes back to first challenge)

//The goal of this JS is to create a text typing game.
//If user text is a match, display success message and advance to next harder challenge.

//array of difficulty text to be placed in <p id=level>
//Added two of each.
const difficulties = ["Easy", "Medium", "Hard", "Fact", "Bonus", "Final"];
//array of string to match, to be placed in <p id=goal>
const goalString = ["CS 3308", 
                    "This is not a test.",
                    "42 is the answer to the Ultimate Question of Life, the Universe, and Everything.",
                    "The Javascript Lab is kinda fun!",
                    "Chicken Nuggets",
                    "Orange Sauce"
  ];


//index to keep track of which difficulty/goal the game is in
//Note that each <p> has default starting values as defined in the html for 1st challenge
var i = 0;
//bool for if random challenge is active, so it does not iterate through next challenge automatically w/out finishing it
var randC=false;
//Need to check if restart button is pressed after page loaded
//or else doesn't work at all...
window.onload=function(){
    //listener for Random Challenge:
    ran=document.getElementById("randomChallenge")
    //click on button activates function
    ran.addEventListener('click', randomChallenge)
    //start timing
    start = Date.now()
    //get restart button id element
    var re = document.getElementById("restartButton");
    //Needed to add event listener to trigger restart() upon clicking of button
    //check that object is not null
    if(re){
        re.addEventListener('click', restart);
    }
}

//The script "listens" for a keypress.
//on the event of a KeyDown, respond to the event by running function: 
//Note that keyDown must be used instead of keypress so backspace/delete are detected
//...I also could have made a separate function, but chose this way
window.addEventListener("keydown", function (event) {
    //get <p> element by id of userinput
    const textbox = document.getElementById("userinput");
    //store key press as code
    var key = event.keyCode
    //debug line
    //alert(key);
    
    //added support for backspace, del, enter key
    //backspace=8, delete=46, enter=13
    
    //This block checks for key strokes not intended to be added to string/displayed:
    
    //needs to make sure Shift==16 isn't treated as text to enter...
    //same with ctl==17
    //same with ctl+c
    //If non text key is entered, do nothing (not affecting textbox.textContent)
    if((key==16 || key==17) || ((event.ctrlKey || event.metaKey) && event.keyCode == 67)) {
        //do nothing
    }
    //Tried to Implemenet paste as Ctl+v...failed, so just does nothing
    // Ctrl+V or Cmd+V pressed?
     else if((event.ctrlKey || event.metaKey) && event.keyCode == 86) {
         /*
         // get text FROM the clipboard
        var text = navigator.clipboard.readText();
         //append onto output
        textbox.textContent = textbox.textContent + text;
        */
         //do nothing
      }
    
    //if del or backspace pressed, delete last char via substr function, making len one less
    else if(key==8 || key==46){
        textbox.textContent=textbox.textContent.substr(0, textbox.textContent.length-1);
    }
    //else if ENTER key is pressed, reset string at current level
    else if (key==13){
        textbox.textContent="";
         //after hitting enter, remove next challenge button if it is there (or else make multiple as error)
        const e = document.getElementById("nxt");
        //first check it isn't null
        if(e){
            e.remove();
        }
    }
    //else, just add that char and check if goalstring is matched
    else{  
        //add this flexible goal object so randomChallenge() works (rather than check goalstring[i])
        goal=document.getElementById("goal");
        //populate userinput textbox with current content + key pressed,
        //repeated for each new key press (until match)
      textbox.textContent = textbox.textContent + event.key;
        //check if entered text matches current goal, if so...:
      if (textbox.textContent == goal.textContent) {
          //if random challenge is active, 
          //then decrement i so it doesn't advance past next challenge without finishing it.
          //Also check that i is not less than 0 so it never falls out of range.
          //This is necessary bc i iterates after clicking next challenge. (so user could skip ahead after finishing rand. challenge)
        if(randC && !(i<0)){
            i=i-1;
        }
          //get <p> element by id, result
        const result = document.getElementById("result");
          //populate result with success text
          //Don't advance page until next challenge button pressed
        result.textContent = "You Win!";
        //create and show next button
        next = document.createElement('button')
        //set button id
        next.setAttribute("id", "nxt");
          //append in body element
        document.body.appendChild(next)
        //Append button name within new <button>
        var t = document.createTextNode("Next Challenge");
        next.appendChild(t);
         //display timer
        end = Date.now()
        diff = (end - start)/1000
        timing = document.createElement('p')
        timing.textContent = "Time to Complete Challenge: "+diff;
          //set custom id to identify later and delete
        timing.setAttribute("id", "timer");
        document.body.appendChild(timing)
        //create button click listener to trigger function
        next.addEventListener('click', nextChallenge)
          }
      }
  })

//Added restart button function
function restart() {
    //this works better to reset the timer...
    location.reload();
    //the old code works, but does not reset the timer.
    
    /*
    //after clicking button, remove next challenge button
    const e = document.getElementById("nxt");
    //first check it isn't null
    if(e){
        e.remove();
    }
    
    //remove timer element
    const timer = document.getElementById("timer");
     if(timer){
            timer.remove();
        }
    // In here set i=0 to reset state 
    //DEBUG line
    //console.log("RESTART");
    i=0;
    // find the level, result, and goal elements and reset their textContent
    result = document.getElementById("result");
    textbox = document.getElementById("userinput");
    lvl = document.getElementById("level")
    goal = document.getElementById("goal")
    
    result.textContent="Type the Following text:";
    level.textContent="Easy";
    textbox.textContent="";
    goal.textContent="CS 3308";
    */
    
}

//Next challenge button function
/*Clicking the button should start the next challenge.
Add the button dynamically so that it only appears when the user completes the challenge.
The game should dynamically display "You Win!" when you complete the challenge.
*/

function nextChallenge(){
        //start timing
        start = Date.now()
        //no longer in random challenge mode
        randC=false;
        //after clicking button, remove it
        const e = document.getElementById("nxt");
        e.remove();
        //remove timer element
        const timer = document.getElementById("timer");
        if(timer){
            timer.remove();
        }
        //get <p> element by id, result
        //reset text to original
        const result = document.getElementById("result");
        result.textContent="Type the Following text:";
        const textbox = document.getElementById("userinput");
          //reset userinput text box
        textbox.textContent = "";
          //iterate difficulty/challenge counter
        i = i+1;
        //if end of challenges is reached, restart to first challenge.
        if (i==6){
            restart()
        }
          //get <p> element by id level
        lvl = document.getElementById("level")
          //populate level text box with updated difficulty
        lvl.textContent = difficulties[i]
          //get <p> element by id goal
        goal = document.getElementById("goal")
          //populate goal text box with new goal 
        goal.textContent = goalString[i]
}

//Function for random challenge button. Creates a random 6 char string to match.
function randomChallenge(){
        //start timing
        start = Date.now()
        //flag bool for random challenge, so i doesn't iterate to next challenge yet. 
        randC=true;
        //after clicking button, remove it
        const e = document.getElementById("nxt");
        if(e){
        e.remove();
        }
    
        //remove timer element
        const timer = document.getElementById("timer");
        if(timer){
            timer.remove();
        }
        //get <p> element by id, result
        //reset text to original
        const result = document.getElementById("result");
        result.textContent="Type the Following text:";
        const textbox = document.getElementById("userinput");
          //reset userinput text box
        textbox.textContent = "";
          //get <p> element by id level
        lvl = document.getElementById("level")
          //populate level text box with updated difficulty
        lvl.textContent = "Random Challenge"
          //get <p> element by id goal
        goal = document.getElementById("goal")
        //Make random string:
        var s=Math.random().toString(20).substr(2, 6)
          //populate goal text box with new goal 
        goal.textContent = s
}