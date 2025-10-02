templates = [
    """     It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body ). If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). Today I talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast. The most ( Adjective3) thing about being in the hospital is the (Silly Word ) (Noun) !""",
    """     This weekend I am going camping with ( Proper Noun (Person’s Name)). I packed my lantern, sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb (ending in ing) ). Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!""",
    """     Dear (Proper Noun (Person’s Name)), I am writing to you from a (Adjective) castle in an enchanted forest. I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! In the ( Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4). It feels as though I have lived here for (Number) ( Measure of time). I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!"""
]
indexes = []
string_with_brackets =  ""
brackets = 0
for i in range(len(templates)):
    indexes.append(str(i+1))
    print(f"{i+1}." + "\n")
    print(templates[i])
template = input("\n"+ "Choose one of these templates(Write Number):").strip()
while True:
    if len(template) > 1:
        template = input("\n" + "Choose one of these templates(Write Number):").strip()
        continue
    elif ord(template) >= ord("1") and ord(template) <= ord("3"):
        break
start_end = False
for i in range(1,len(indexes)+1):
    if indexes[i-1] == template:
        for item in templates[i-1]:
            if item == ")" and start_end == False:
                string_with_brackets += item
                string_with_brackets += "\n"
                brackets = 0
            if item ==  "(":
                start_end = True
                string_with_brackets += item
                brackets += 1
            else:
                if start_end:
                    if item ==  ")":
                        brackets -= 1
                        string_with_brackets += item
                        if brackets < 1:
                            start_end = False
                            string_with_brackets += "\n"
                            brackets = 0
                    else:
                        string_with_brackets += item
        string_with_brackets = string_with_brackets.splitlines()
        for item in string_with_brackets:
            word = input("Input " + item + ":")
            templates[i-1] = templates[i-1].replace(item,word)
        print(templates[i-1])