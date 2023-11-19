def get_user_input():
    # Ask the user some questions
    age = input("How old are you? ")
    exercise_level = input("What's your exercise level? ")
    skincare_routine = input("What's your skincare routine? ")
    health_conditions = input("Do you have any pre-existing health conditions? ")
    sunscreen_use = input("Do you use any sunscreen? ")
    limitations_injuries = input("Do you have any physical limitations or skin injuries? (If not, leave it blank) ")

    # Process the input and provide a response (replace this with your actual AI logic)
    response = f"Based on your input:\nAge: {age}\nExercise Level: {exercise_level}\nSkincare Routine: {skincare_routine}\n" \
               f"Health Conditions: {health_conditions}\nSunscreen Use: {sunscreen_use}\nLimitations or Injuries: {limitations_injuries}"

    return response

if __name__ == "__main__":
    # Get user input
    user_response = get_user_input()

    # Display the AI response
    print("\nAI Response:")
    print(user_response)
