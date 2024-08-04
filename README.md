# kaggle_python_course
Problems requiring algorithmic resolution, implemented in python from Kaggle courses

Exercice 01:
Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed.
For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
Write an arithmetic expression below to calculate how many candies they must smash for a given haul.

Exercice 02:
We're using lists to record people who attended our party and what order they arrived in. For example, the following list represents a party with 7 guests, in which Adela showed up first and Ford was the last to arrive:
party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. However, they must not be the very last guest (that's taking it too far). In the above example, Mona and Gilbert are the only guests who were fashionably late.
From a given list of attendees, found is someone is fasionably late

Exercice 03:
A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. Write a function to help her filter her list of articles.
Your function should meet the following criteria:
    Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.”
    She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” would be included when the keyword is “closed”
    Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”. But you can assume there are no other types of punctuation.