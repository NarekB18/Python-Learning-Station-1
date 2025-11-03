# 🧩 Mad Libs Story Generator

This is a **Mad Libs–style story generator** written in Python.
It randomly selects a story template, asks the user for different types of words (like *nouns*, *adjectives*, *verbs*, etc.), and then fills in the blanks to create a funny, customized story.

---

## 📘 How It Works

1. The program randomly selects one of three story templates.
2. Each template contains placeholders in parentheses — for example:

   ```
   (Noun), (Adjective), (Verb), (Measure of time)
   ```
3. The script prompts you to enter words for each placeholder.
4. It validates your inputs:

   * Numbers must be numeric.
   * Measures of time must be one of:
     `second, minute, hour, day, month, year, decade, century`
   * All other words must contain only letters (no numbers or symbols).
5. When all inputs are filled, it prints the completed story.

---

## 🧠 Example Run

```
Input Number: 5
Input Measure of time: years
Input Mode of Transportation: car
Input Adjective: spooky
Input Adjective2: small
Input Noun: ghosts
Input Color: green
Input Part of the Body: hands
Input Verb: knock
Input Number2: 3
Input Noun2: posters
Input Noun3: mask
Input Part of the Body 2: face
Input Verb: eat
Input Noun4: pancakes
Input Adjective3: funniest
Input Silly Word: boing
```

**Output:**

```
It was about 5 years ago when I arrived at the hospital in a car. 
The hospital is a spooky place, there are a lot of small ghosts here. 
There are nurses here who have green hands. 
If someone wants to come into my room I told them that they have to knock first. 
I’ve decorated my room with 3 posters. 
Today I talked to a doctor and they were wearing a mask on their face. 
I heard that all doctors eat pancakes every day for breakfast. 
The most funniest thing about being in the hospital is the boing ghosts!
```

---

## 🧩 Features

* 🎲 Randomly selects one of 3 unique story templates
* ✅ Validates user input for correct word types
* 🗣️ Interactive, command-line experience
* 😂 Always produces a silly and personalized story
