//function to roll the dice
function rollDice() {
    console.log("Welcome to the Dice Rolling Simulator!");
    //while loop to run the dice rolling features
    while (true) {
        //asking the user to press Enter to roll the dice
        prompt("Press Enter to roll the dice...");
        // Using Math.random() to randomly choose a number between 1 and 6
        const diceRoll = Math.floor(Math.random() * 6) + 1;
        console.log(`You rolled a ${diceRoll}`);

        let playAgain;
        //while loop to ask the user to play again or close the application
        while (true) {
            //taking input from the user and converting it to lower case
            playAgain = prompt("Would you like to roll again? (yes/no)");

            if (playAgain.toLowerCase() === "yes" || playAgain.toLowerCase() === "no") {
                break;
            } else {
                console.log("Please enter a valid option (yes/no)");
            }
        }
        if (playAgain.toLowerCase() === "no") {
            console.log("Thanks for playing!");
            break;
        }
    }
}
//calling the rollDice function
rollDice();
