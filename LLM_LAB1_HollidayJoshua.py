# Joshua Holliday
# July 6, 2026
# llm_lab1.py
# Practice working with an AI language model to generate a Python script based on specific functional requirements.

# -----------------------------------------
# Display a welcome message for the quiz game.
# Ask the user to enter their favorite hobby.
# Ask how long they have been doing the hobby.
# Ask how the hobby has influenced their personal or professional life.
# Display a summary of the user's answers.
# Thank the user for playing the game.
# -----------------------------------------

# Hobby Ice Breaker Quiz Game

# -----------------------------------------
# PSEUDOCODE
# -----------------------------------------
# Display a welcome message for the quiz game.
# Ask the user to enter their favorite hobby.
# Ask how long they have been doing the hobby.
# Ask how the hobby has influenced their personal or professional life.
# Ask how often they enjoy their hobby.
# Ask what they enjoy most about their hobby.
# Ask what advice they would give to someone who wants to start the hobby.
# Display a summary of the user's answers.
# Thank the user for playing the game.
# -----------------------------------------

# Hobby Ice Breaker Quiz Game

print("===================================")
print("      Hobby Ice Breaker Quiz")
print("===================================")
print("Let's get to know each other!")
print()

# Question 1
hobby = input("1. What is your favorite hobby? ")

# Question 2
years = input(f"\n2. How long have you been enjoying {hobby}? ")

# Question 3
influence = input(f"\n3. Has {hobby} influenced your personal or professional life? How? ")

# Question 4
frequency = input(f"\n4. How often do you spend time on {hobby}? ")

# Question 5
favorite_part = input(f"\n5. What do you enjoy most about {hobby}? ")

# Question 6
advice = input(f"\n6. What advice would you give someone who wants to start {hobby}? ")

# Display Results
print("\n===================================")
print("        Your Hobby Snapshot")
print("===================================")

print(f"Favorite Hobby : {hobby}")
print(f"Experience     : {years}")
print(f"Life Impact    : {influence}")
print(f"How Often      : {frequency}")
print(f"Favorite Part  : {favorite_part}")
print(f"Best Advice    : {advice}")

print("\n===================================")
print("Thanks for playing!")
print("Here's what we learned about you:")
print(f"- Your favorite hobby is: {hobby}")
print(f"- You've been doing it for how long: {years}")
print(f"- You enjoy it because: {favorite_part}")
print(f"- How often do you play: {frequency}")
print(f"- How has it influenced your life: {influence}")
print(f"- Your advice to beginners: {advice}")
print("\nGreat conversations often begin with learning about each other's interests!")
print("===================================")

"""
Reflect on experience:

The generated code was correct and complete on the first attempt. I believe I provided enough context and clear instructions for the AI to understand the requirements. 
The code is well-structured, with clear prompts for user input and a summary of the responses. The use of formatted strings makes the output easy to read and understand. 
Overall, I am satisfied with the result and would consider using this approach for future coding tasks.
I did have to fix the summary by adding colons and improving the language so it presents the results more clearly. Also had to clean up some punctuation. But, the AI 
successfully created a functional and user-friendly quiz game that captures the user's favorite hobby and its impact on their life. 
This code could be repurposed for other similar applications, such as icebreaker activities or personal interest surveys, but overall I think the results are good. I could 
maybe have the code structured to rotate the 2nd and 3rd questions to make it more dynamic. Actually, I did make changes to the code so that it did improve it overall. 
The benefits are exponential, as it saves time and effort in coding, especially for repetitive tasks or when generating boilerplate code. It also allows for quick prototyping 
and testing of ideas. Some of the risks include the AI generating code that may not be optimal or may contain errors, but with proper review and testing, these risks can be 
mitigated. Overall, I am impressed with the capabilities of AI in assisting with coding tasks and look forward to exploring its potential further.
"""