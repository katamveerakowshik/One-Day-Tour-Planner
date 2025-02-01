from openai import  OpenAI
from Agents.passwrds import openai_api

client = OpenAI(api_key = openai_api)
def generate_itinerary(city, start_time, end_time, interests, budget, starting_point):
    # Define your OpenAI API key securely (replace "your-api-key" with your actual key)

    # Construct the prompt
    prompt = f"""Create a detailed one-day trip itinerary with the following details:
    - City: {city}
    - Start Time: {start_time}
    - End Time: {end_time}
    - Interests: {', '.join(interests)}
    - Budget: {budget}
    - Starting Point: {starting_point}

    Please include:
    1. Recommended attractions and activities
    2. Estimated time at each location
    3. Transportation options between locations
    4. Dining recommendations (budget-friendly options)
    5. Any special tips or considerations

    Format your response as a structured itinerary."""

    # Call OpenAI API
    try:
        response = client.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages = [
                {"role": "Travel Guide"},
                {"content": prompt}
            ],
            temperature=0.7
        )
        return response["choices"][0]["text"].strip()
    except Exception as e:
        return f'Error generating itinerary: {e}'



