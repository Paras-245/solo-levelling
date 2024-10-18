import os
import json
from groq import Groq
import json
import re
from django.conf import settings
from pydantic import BaseModel,Field
client = Groq(
    api_key=settings.GROQ_API_KEY,
)


quests_data = [
    {
        "day": 1,
        "quests": [
            {
                "title": "Quest 1: The First Step",
                "objective": "Get started with your gym routine.",
                "tasks": [
                    "Sign up for a gym membership.",
                    "Attend your first gym session.",
                    "Meet with a personal trainer for a fitness assessment."
                ]
            },
            {
                "title": "Quest 2: Gym Tour",
                "objective": "Familiarize yourself with the gym.",
                "tasks": [
                    "Take a tour of the gym facilities.",
                    "Learn about different equipment and their usage.",
                    "Identify the best times to visit the gym."
                ]
            },
            {
                "title": "Quest 3: Setting Goals",
                "objective": "Set your fitness goals.",
                "tasks": [
                    "Define short-term and long-term fitness goals.",
                    "Discuss your goals with a personal trainer.",
                    "Write down your goals in a fitness journal."
                ]
            }
        ]
    },
    {
        "day": 2,
        "quests": [
            {
                "title": "Quest 1: Building Foundation",
                "objective": "Establish a regular workout schedule.",
                "tasks": [
                    "Create a weekly workout plan.",
                    "Complete at least three gym sessions in one week.",
                    "Track your workouts in a journal or app."
                ]
            },
            {
                "title": "Quest 2: Warm-Up Routine",
                "objective": "Learn and practice a proper warm-up routine.",
                "tasks": [
                    "Research different warm-up exercises.",
                    "Incorporate a 10-minute warm-up into your routine.",
                    "Perform dynamic stretches before your workout."
                ]
            },
            {
                "title": "Quest 3: Cardio Introduction",
                "objective": "Start with basic cardio exercises.",
                "tasks": [
                    "Spend 20 minutes on the treadmill or elliptical.",
                    "Try out the stationary bike for 15 minutes.",
                    "Record your cardio sessions in your journal."
                ]
            }
        ]
    },
    {
        "day": 3,
        "quests": [
            {
                "title": "Quest 1: Strength Training Basics",
                "objective": "Focus on building muscle strength.",
                "tasks": [
                    "Learn proper form for basic strength exercises (e.g., squats, deadlifts, bench press).",
                    "Incorporate strength training into your workout plan twice a week.",
                    "Increase the weight you lift by 10% over four weeks."
                ]
            },
            {
                "title": "Quest 2: Core Workout",
                "objective": "Strengthen your core muscles.",
                "tasks": [
                    "Perform planks for 3 sets of 30 seconds.",
                    "Incorporate Russian twists into your routine.",
                    "Do 3 sets of 15 crunches."
                ]
            },
            {
                "title": "Quest 3: Hydration",
                "objective": "Maintain proper hydration.",
                "tasks": [
                    "Drink at least 2 liters of water throughout the day.",
                    "Carry a water bottle with you to the gym.",
                    "Hydrate before, during, and after workouts."
                ]
            }
        ]
    },
    {
        "day": 4,
        "quests": [
            {
                "title": "Quest 1: Upper Body Workout",
                "objective": "Focus on upper body strength.",
                "tasks": [
                    "Perform 3 sets of push-ups.",
                    "Incorporate dumbbell shoulder presses into your routine.",
                    "Do 3 sets of bicep curls."
                ]
            },
            {
                "title": "Quest 2: Flexibility Training",
                "objective": "Improve your flexibility.",
                "tasks": [
                    "Spend 15 minutes stretching after your workout.",
                    "Try out a beginner yoga class.",
                    "Incorporate static stretching into your routine."
                ]
            },
            {
                "title": "Quest 3: Nutrition",
                "objective": "Focus on proper nutrition.",
                "tasks": [
                    "Plan and prepare healthy meals for the week.",
                    "Include protein in each meal.",
                    "Avoid processed foods and sugary drinks."
                ]
            }
        ]
    },
    {
        "day": 5,
        "quests": [
            {
                "title": "Quest 1: Lower Body Workout",
                "objective": "Focus on lower body strength.",
                "tasks": [
                    "Perform 3 sets of squats.",
                    "Incorporate lunges into your routine.",
                    "Do 3 sets of calf raises."
                ]
            },
            {
                "title": "Quest 2: Tracking Progress",
                "objective": "Monitor your fitness progress.",
                "tasks": [
                    "Take measurements of your body.",
                    "Record your weight and body fat percentage.",
                    "Take progress photos once a week."
                ]
            },
            {
                "title": "Quest 3: Sleep and Recovery",
                "objective": "Ensure proper rest and recovery.",
                "tasks": [
                    "Aim for 7-8 hours of sleep each night.",
                    "Incorporate rest days into your workout plan.",
                    "Practice relaxation techniques before bed."
                ]
            }
        ]
    },
    {
        "day": 6,
        "quests": [
            {
                "title": "Quest 1: HIIT Workout",
                "objective": "Incorporate high-intensity interval training (HIIT).",
                "tasks": [
                    "Perform a 20-minute HIIT workout.",
                    "Include burpees, jump squats, and mountain climbers.",
                    "Track your heart rate during the workout."
                ]
            },
            {
                "title": "Quest 2: Workout with a Partner",
                "objective": "Exercise with a gym buddy.",
                "tasks": [
                    "Find a workout partner.",
                    "Complete a workout session together.",
                    "Motivate each other to push harder."
                ]
            },
            {
                "title": "Quest 3: Learning New Exercises",
                "objective": "Expand your exercise knowledge.",
                "tasks": [
                    "Research new exercises to add to your routine.",
                    "Incorporate at least one new exercise into your workout.",
                    "Focus on proper form and technique."
                ]
            }
        ]
    },
    {
        "day": 7,
        "quests": [
            {
                "title": "Quest 1: Endurance Training",
                "objective": "Improve your endurance.",
                "tasks": [
                    "Run or jog for 30 minutes.",
                    "Try out a spin class at the gym.",
                    "Incorporate interval training into your cardio sessions."
                ]
            },
            {
                "title": "Quest 2: Balance Training",
                "objective": "Enhance your balance and stability.",
                "tasks": [
                    "Perform single-leg stands for 3 sets of 30 seconds.",
                    "Incorporate balance exercises using a stability ball.",
                    "Try out a balance-focused class (e.g., Pilates)."
                ]
            },
            {
                "title": "Quest 3: Active Recovery",
                "objective": "Incorporate active recovery into your routine.",
                "tasks": [
                    "Engage in a low-intensity activity like walking or swimming.",
                    "Spend 15 minutes foam rolling.",
                    "Do a gentle yoga or stretching session."
                ]
            }
        ]
    },
    {
        "day": 8,
        "quests": [
            {
                "title": "Quest 1: Advanced Strength Training",
                "objective": "Challenge your strength training routine.",
                "tasks": [
                    "Incorporate compound exercises like deadlifts and bench presses.",
                    "Increase the weight and intensity of your workouts.",
                    "Focus on progressive overload."
                ]
            },
            {
                "title": "Quest 2: Speed Training",
                "objective": "Improve your speed and agility.",
                "tasks": [
                    "Perform sprints for 10 sets of 30 seconds.",
                    "Incorporate agility drills like ladder drills and cone drills.",
                    "Track your sprint times and aim to improve."
                ]
            },
            {
                "title": "Quest 3: Mind-Body Connection",
                "objective": "Enhance your mind-body connection.",
                "tasks": [
                    "Practice mindful breathing during workouts.",
                    "Incorporate meditation into your daily routine.",
                    "Focus on proper form and technique for each exercise."
                ]
            }
        ]
    },
    {
        "day": 9,
        "quests": [
            {
                "title": "Quest 1: Full-Body Workout",
                "objective": "Engage in a full-body workout.",
                "tasks": [
                    "Perform exercises that target all major muscle groups.",
                    "Include compound movements like squats, deadlifts, and push-ups.",
                    "Complete 3 sets of each exercise."
                ]
            },
            {
                "title": "Quest 2: Flexibility and Mobility",
                "objective": "Improve your flexibility and mobility.",
                "tasks": [
                    "Spend 20 minutes stretching after your workout.",
                    "Incorporate foam rolling into your routine.",
                    "Try out a mobility class at the gym."
                ]
            },
            {
                "title": "Quest 3: Recovery Strategies",
                "objective": "Implement recovery strategies.",
                "tasks": [
                    "Use a foam roller to massage sore muscles.",
                    "Take an Epsom salt bath to relax your muscles.",
                    "Get a sports massage to aid in recovery."
                ]
            }
        ]
    }]

def load(goal,progress,day):
    chat_completion = client.chat.completions.create(
     messages=[
            {
                "role": "system",
                "content":"""
                Generate a series of 3 quests per day from day {0} to day {1} for a player whose goal is "{2}" and currently their progress is "{3}". Each day should have a JSON object with the following format and strict structure:
                [
                    {{
                        "day": day number,
                        "quests": [
                            {{
                                "title": "Quest 1: Quest Title",
                                "objective": "Objective description",
                                "tasks": [
                                    "Task 1",
                                    "Task 2",
                                    "Task 3"
                                ]
                            }},
                            {{
                                "title": "Quest 2: Quest Title",
                                "objective": "Objective description",
                                "tasks": [
                                    "Task 1",
                                    "Task 2",
                                    "Task 3"
                                ]
                            }},
                            {{
                                "title": "Quest 3: Quest Title",
                                "objective": "Objective description",
                                "tasks": [
                                    "Task 1",
                                    "Task 2",
                                    "Task 3"
                                ]
                            }}
                        ]
                    }}
                ]
                """.format(day, day+9, goal, progress),
            },
            
        ],
    
    model="llama3-8b-8192",
)
    response_string = chat_completion.choices[0].message.content
    match = re.search(r'(\[\s*{.*}\s*\])', response_string, re.DOTALL)
    if match:
        json_string = match.group(1)
        # Load the cleaned JSON string
        data = json.loads(json_string)
        # Print or use the JSON data
        # for day_data in data:
        #         print(day_data)
        return data
    else:
        return None  
load("lose weight","10kg",1) 