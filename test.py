import random

templates = [
    """It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body). If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). Today I talked to a doctor and they were wearing a (Noun3) on their (Part of the Body 2). I heard that all doctors (Verb2) (Noun4) every day for breakfast. The most (Adjective3) thing about being in the hospital is the (Silly Word) (Noun5)!""",
    # ... (other templates)
]


def create_template():
    measure_of_time = ["second", "minute", "hour", "day", "month", "year", "decade", "century"]

    # 1. Template Selection
    while True:
        try:
            choice = int(input(f"Choose Template (1-{len(templates)}): "))
            if 1 <= choice <= len(templates):
                template_idx = choice - 1
                break
            print(f"Please enter a number between 1 and {len(templates)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    current_story = templates[template_idx]

    # 2. Extract and Replace Placeholders
    while "(" in current_story:
        start = current_story.find("(")
        end = current_story.find(")") + 1
        placeholder = current_story[start:end]

        user_word = ""
        while True:
            user_word = input(f"Enter a {placeholder}: ").strip()

            # Validation Logic
            if "Number" in placeholder and not user_word.isnumeric():
                print("--> Please enter a valid number.")
            elif "Measure" in placeholder and user_word.lower() not in measure_of_time:
                print(f"--> Choose from: {', '.join(measure_of_time)}")
            elif "ending in ly" in placeholder and not user_word.lower().endswith("ly"):
                print("--> Word must end in 'ly'.")
            elif "ending in ing" in placeholder and not user_word.lower().endswith("ing"):
                print("--> Word must end in 'ing'.")
            elif not user_word.replace(" ", "").replace("-", "").isalpha():
                # Allows spaces and hyphens for names/places
                print("--> Please use letters only.")
            else:
                break  # Input is valid

        # Replace only the FIRST occurrence found
        current_story = current_story.replace(placeholder, user_word, 1)

    return current_story


print("\n--- YOUR STORY ---")
print(create_template())