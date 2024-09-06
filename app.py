import gradio as gr
from dotenv import load_dotenv
import openai
import os

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key="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"


def fitness_evaluation(age, height_meters, weight_kg, gender, activity_levels_1highest, free_time_daily_hours, a_pwd, additional_info):
    messages = []
    messages.append({"role": "system", "content": "A fitness AI dedicated into giving very specific fitness and very specific diet plans to people with different demographics"})
    pwd = True
    if a_pwd:
        pwd = "a pwd"
    else:
        pwd = "not a pwd"
    if additional_info:
        additional_info = additional_info
    else:
        additional_info = "nothing"
        
    message = f"Give a person with age of {age}, height of {height_meters} meters, weight of {weight_kg} kg, activity levels of {activity_levels_1highest} with 1 being the highest activity level, free time daily of {free_time_daily_hours} in hours, is {pwd},and has additional info of {additional_info}"
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    fitness_advice = reply
    return fitness_advice

demo = gr.Interface(
    fn=fitness_evaluation,
    inputs=["text", gr.Slider(0, 7), gr.Slider(0, 300), gr.Radio(["Male", "Female"]), gr.Radio(["1", "2", "3", "4", "5"]), gr.Slider(0, 24), "checkbox", "text"],
    outputs=["text"],
    title="FitnessGPT",
    description="A mini project dedicated to help people in their fitness goals.",
    
)
    
if __name__ == "__main__":
    demo.launch()   