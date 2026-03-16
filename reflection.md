# 💭 Reflection: Game Glitch Investigator

There was a difficulty mismatch between Normal and Hard mode; Normal mode has 100 numbers while Hard has 50 numbers. Clearly Hard mode is easier than Normal mode in this case. There is an "attempts" mismatch in Easy and Medium modes. Easy has 6 attempts and Medium has 8 attempts, this is wrong since difficulty should increase from Easy to Medium, and 8 attempts in Medium is easier to get than Easy. Finally there is a logic issue, for example, my secret number is 63, my input is 50, and the hint is telling me to go lower, witch is incorrect it should tell me to go higher since 63 is higher than 50.

## 1. What was broken when you started?

There was a difficulty mismatch between Normal and Hard mode; Normal mode has 100 numbers while Hard has 50 numbers. Clearly Hard mode is easier than Normal mode in this case. There is an "attempts" mismatch in Easy and Medium modes. Easy has 6 attempts and Medium has 8 attempts, this is wrong since difficulty should increase from Easy to Medium, and 8 attempts in Medium is easier to get than Easy. Finally there is a logic issue, for example, my secret number is 63, my input is 50, and the hint is telling me to go lower, witch is incorrect it should tell me to go higher since 63 is higher than 50.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
