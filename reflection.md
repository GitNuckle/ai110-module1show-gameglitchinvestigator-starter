# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

There was a difficulty mismatch between Normal and Hard mode; Normal mode has 100 numbers while Hard has 50 numbers. Clearly Hard mode is easier than Normal mode in this case. There is an "attempts" mismatch in Easy and Medium modes. Easy has 6 attempts and Medium has 8 attempts, this is wrong since difficulty should increase from Easy to Medium, and 8 attempts in Medium is easier to get than Easy. Finally there is a logic issue, for example, my secret number is 63, my input is 50, and the hint is telling me to go lower, witch is incorrect it should tell me to go higher since 63 is higher than 50.

---

## 2. How did you use AI as a teammate?

- I used Claude using the Claude extension and connected it to my Claude account.
- I asked for Claude to swap the attempt numbers between Easy and Medium mode along with swapping the range of numbers between medium and hard, and I verified the result by asking it why it was doing it and its rationale all in the same prompt.
- The AI made a mistake with moving the check_guess block of code that was moved into the logic_utils.py file with all UI strings (With Copilot Agent Mode). I verified the result by checking the logic and use of "strings" such as "Go higher!" of "Congrats!", i then asked Claude to double check that specific code block for this  check_guess function that was in logic_utils.py with #FIXME and it was able to help me clean things up and undo and implement the fixed code correctly. 

---

## 3. Debugging and testing your fixes

- I checked the syntax and approved of new edits.
- I used pytest to check the check_guess function that i fixed, it showed that the code was finally operating correctly and accurately.
- Yes AI helped me design these tests and understand how and why their used regarding commands and syntax.

---

## 4. What did you learn about Streamlit and state?

- The secret number kept changing because Streamlit reran the whole app every time the user interacted with the program, so a new random number was created each time.
- Streamlit reruns mean that the my script will start again on every interaction, and session state is what lets the app remember values between those reruns.
- The secret number was fixed once a harcoded range of 0,100 was fixed to low,high according to the mode.

---

## 5. Looking ahead: your developer habits

- Most likely when im using Claude and Copilot being able to ask questions with precision and context with #file and #FIXME comands.
- I would open VSCode and have claude on my side to stress test different strategies with pytest for different anamolies i find during running said program.
- I was able to have a less confused workflow on where to find UI and logic code making going through this codebase a lot easier. Another thing I see that AI can be useful with is that as long as there is someone approving these changes and addition there is an extreme benefit in efficiency where the developer can focus more on creativity and features.
