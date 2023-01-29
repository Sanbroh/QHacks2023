#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 11:00:18 2023

@author: thomastesselaar
"""

import openai
import json
import base64

def create_product_intro(idea:str, api_key:str):
    openai.api_key = api_key
    
    # Use the OpenAI API to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"Give me a product name and catchphrase for this idea: {idea}"),
        temperature=0.5,
        max_tokens=100,
        
    )
    
    # Returns the summarized text
    r = response["choices"][0]["text"]
    r = r.replace("\n", "")
    r = r.replace("Product Name: ", "")
    r = r.replace("Catchphrase: ", "|||")
    h = r.split("|||")
    h[1] = h[1].replace("\"", '')
    return h


def create_problem_def(problem:str, length:int, api_key:str):
    openai.api_key = api_key
    problem = problem.split(' ', 2)[2]
    
    # Use the OpenAI API to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"Why is {problem} a big problem in about {length} words"),
        temperature=0.5,
        max_tokens=250,
        
    )
    
    # Returns the summarized text
    r = response["choices"][0]["text"]
    if ("?" in r[:5]):
        r = r.split("?", 1)[1]
    r = r.replace("\n", "")
    return r
   
def create_problem_solution(idea:str, name:str, length:int, api_key:str):
    openai.api_key = api_key
    
    # Use the OpenAI API to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"What problem does a product named {name} \
                whose idea is {idea} solve? Answer in about {length} words"),
        temperature=0.5,
        max_tokens=250,
        
    )
    
    # Returns the summarized text
    r = response["choices"][0]["text"]
    
    r = r.replace("\n", "")
    return r 

def get_target_market(idea:str, name:str, length:int, api_key:str):
    openai.api_key = api_key
    
    # Use the OpenAI API to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"Tell me the target market for {name}, {idea}, in {length/2} words?"),
        temperature=0.5,
        max_tokens=125,
        
    )
    
    # Returns the summarized text
    r = response["choices"][0]["text"]
    
    r = r.replace("\n", "")
    return r 

def get_market_strat(idea:str, name:str, api_key:str):
    openai.api_key = api_key
    
    # Use the OpenAI API to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"What is the four step go to market strategy for {name}, {idea}?"),
        temperature=0.5,
        max_tokens=240,
        
    )
    
    # Returns the summarized text
    r = response["choices"][0]["text"]
    
    r = r.replace("\n\n", "\n")
    r = r.strip()
    return r 

def get_implementation(idea:str, length:int, api_key:str):
    openai.api_key = api_key
    
    # Use the OpenAI API to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"Describe the technical implementation be for a start-up whose \
                product is {idea}, including programming language, in about {length} words"),
        temperature=0.5,
        max_tokens=250,
        
    )
    
    # Returns the summarized text
    r = response["choices"][0]["text"]
    
    r = r.replace("\n\n", "\n")
    r = r.strip()
    return r 

def get_next_steps(idea:str, api_key:str):
    openai.api_key = api_key
    
    # Use the OpenAI API to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"What would three next steps be for a start-up whose product is {idea}?"),
        temperature=0.5,
        max_tokens=150,
        
    )
    
    # Returns the summarized text
    r = response["choices"][0]["text"]
    
    r = r.replace("\n\n", "\n")
    r = r.strip()
    return r 

def get_thank_you(name:str, api_key:str):
    openai.api_key = api_key
    
    # Use the OpenAI API to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=("Write a one line thank you for listening to our presentation"),
        temperature=0.5,
        max_tokens=80,
        
    )
    r = response["choices"][0]["text"].strip()
    return r
    
    

def make_script(idea:str, length:int, api_key:str):
    # Holds the script
    # Ends in the following format [name, hook, problem def, solution, tehcnical
    # implementation, target market, go to market strat, next steps]
    script = []
    
    intro = create_product_intro(idea, api_key)
    name = intro[0]
    script.append(name[:int(len(name)/2)])
    script.append(name[int(len(name)/2):])
    hook = intro[1]
    script.append(hook)
    
    solution = create_problem_solution(idea, name, length, api_key)
    problem = solution.split(".")[0]
    problem_def = create_problem_def(problem, length, api_key)
    script.append(problem_def)
    script.append(solution)
    
    script.append(get_implementation(idea, length, api_key))
    script.append(get_target_market(idea, name, length, api_key))
    script.append(get_market_strat(idea, name, api_key))
    script.append(get_next_steps(idea, api_key))
    script.append(get_thank_you(idea, api_key))
    
    return script

def summ_to_points(text:str, num_pts:int, api_key:str):
    openai.api_key = api_key
    
    # Use the OpenAI API to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"Summareize this text to {num_pts} under fifteen word bullet points: {text}"),
        temperature=0.5,
        max_tokens=75,
        
    )
    
    # Returns the summarized text
    r = response["choices"][0]["text"]
    
    r = r.replace("\n", "")
    if("•" in r):
        pts = r.split("•")
        pts = pts[1:]
    elif("1. " in r):
        r = r.replace("1. ", '')
        r = r.replace("2", '')
        r = r.replace("3", '')
        pts = r.split(". ")
    elif(r.count('-') > 2):
        r = r.replace("-", ' ')
        pts = r.split(".")
    else:
        pts = r.split("  ")
        
        
    for i in range(len(pts)):
        pts[i] = pts[i].lstrip(' ')
        pts[i] = pts[i].rstrip(' .,')
    
    return pts

def summ_as_points(text:str, num_pts:int, api_key:str):
    openai.api_key = api_key
    
    text = text.replace("1. ", '')
    text = text.replace("2. ", '|||')
    text = text.replace("3. ", '|||')
    if (num_pts >= 4):
        text = text.replace("4. ", '|||')
    pts = text.split("|||")
    
    summ_pts = []
    for pt in pts:
    
        # Use the OpenAI API to summarize the text
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=(f"Summareize this text to less than ten words: {pt}"),
            temperature=0.5,
            max_tokens=40,
            
        )
        
        # Returns the summarized text
        r = response["choices"][0]["text"]
        r = r.lstrip(' \n')
        r = r.rstrip(' .,\n')
        
        summ_pts.append(r)
    
    return summ_pts

def get_slide_points(script:list[str], api_key:str):
    
    
    pd_pts = summ_to_points(script[3], 3, api_key)
    sol_pts = summ_to_points(script[4], 3, api_key)
    tech_pts = summ_to_points(script[5], 3, api_key)
    # if len(tech_pts) <3:
    #     tech_pts = tech_pts[0].split('  ')
        
    tm_pts = summ_to_points(script[6], 3, api_key)
    gtm_pts = summ_as_points(script[7], 4, api_key)
    next_pts = summ_as_points(script[8], 3, api_key)
    
    slide_pts = [pd_pts, sol_pts, tech_pts, tm_pts, gtm_pts, next_pts]
    
    return slide_pts


# Returns a url to view the image, could also be switched to put image directly
# on your device
def generate_logo(prompt:str, api_key:str):
    openai.api_key = api_key
    
    # use the OpenAI API to generate the image
    response = openai.Image.create(
        prompt=f"A cartoon of {prompt} on a white background",
        # model="image-alpha-001",
    )
    
    # save the image
    
    # with open("image.json", mode="w", encoding="utf-8") as file:
    #     json.dump(response, file)
    
    # with open("image.jpg", "wb") as f:
    #     f.write(response.content)
    
    # with open(title + ".jpg", "wb") as f:
    #     f.write(response["data"][0]["url"])
    
    # print("Image saved as image.jpg")
    
    # with open("image.jpg", "wb") as f:
    #     f.write(base64.b64decode(response["data"][0]["b64_json"][:50]))
    
    return response["data"][0]["url"]
    
    # with open("image.json", mode="r", encoding="utf-8") as file:
    #     response = json.load(file)
    
    # return

def write_script_to_single_page(script):
    long_script = f"Slide 1:\nIntroducing {script[0]}{script[1]}.\n"
    long_script += f"{script[2]}\n\n"
    long_script += "Slide 2:\n"
    long_script += f"{script[3]}\n\n"
    long_script += "Slide 3:\n"
    long_script += f"{script[4]}\n\n"
    long_script += "Slide 4:\n"
    long_script += f"{script[5]}\n\n"
    long_script += "Slide 5:\n"
    long_script += f"{script[6]}\n\n"
    long_script += "Slide 6:\n"
    long_script += f"{script[7]}\n\n"
    long_script += "Slide 7:\n"
    long_script += f"{script[8]}\n\n"
    long_script += "Slide 8:\n"
    long_script += f"{script[9]}\n\n"
    
    return long_script
    
def get_tip(api_key):
    openai.api_key = api_key
    
    # Use the OpenAI API to summarize the text
    response = openai.Completion.create(
        engine="text-babbage-001",
        prompt=("Give me a quick tip for presenting well"),
        temperature=0.5,
        max_tokens=80,
        
    )
    r = response["choices"][0]["text"].strip()
    return r

def get_languages(tech:str):
    tech = tech.lower()
    possible_languages = ["python", "php", "js", "javascript", 'html', 'css', 'c++', 'c',
                 "sql", "mongodb", "ruby", "aws"]
    languages = []
    
    for l in possible_languages:
        if l in tech:
            languages.append(l)
    
    return languages


# script = ['SlideMaker', '"Say goodbye to tedious slide deck creation - SlideMaker does it for you!"', 'Creating professional-looking slide decks quickly and easily is a big problem because it requires a lot of time and effort to design a well-crafted presentation. It also requires knowledge of design principles, an understanding of the target audience, and an ability to effectively communicate the desired message. Additionally, creating a professional-looking slide deck requires knowledge of the latest software and tools available, which can be difficult to keep up with. All of these factors make it challenging to create a professional-looking slide deck quickly and easily.', 'SlideMaker solves the problem of creating professional-looking slide decks quickly and easily. It allows users to quickly create a well-structured, visually appealing presentation without needing to have any design or technical skills. It also allows users to collaborate on the same presentation, making it easy to share ideas and get feedback.', 'The technical implementation for this start-up would likely involve a combination of web technologies and programming languages. On the web side, the app could be built using HTML, CSS, and JavaScript for the user interface. For the back-end, the app could be built using a server-side language such as PHP or Python, which would handle data storage and retrieval. Additionally, a database such as MySQL or MongoDB could be used for data storage. Finally, a library such as Reveal.js or Slides.js could be used to create the slide decks.', 'The target market for SlideMaker would be anyone who needs to create a professional-looking presentation, such as business professionals, educators, and students. It could also be used by marketers, entrepreneurs, and other professionals who need to create visually appealing presentations.', '1. Pre-Launch Preparation: Before you launch your app, it’s important to do research and create a plan for your product. This includes identifying target markets, understanding customer needs and wants, and developing a unique value proposition. Additionally, you should create a marketing plan, develop a pricing strategy, and create a website and other marketing materials.\n2. Launch: Once you’ve done your research and created a plan, it’s time to launch your app. This includes launching it on the app store, creating a website, and announcing it on social media. Additionally, you should create a landing page, build an email list, and create an online presence.\n3. Promotion: After launching your app, it’s important to promote it. This includes creating content such as blog posts, videos, and webinars to explain', '1. Establish a budget for marketing and advertising the app. This could include creating a website, running online ads, and utilizing social media platforms to reach potential users.\n2. Develop a user testing plan to identify any usability issues and improve the overall user experience. This could involve conducting interviews with potential users and soliciting feedback from existing users.\n3. Create a customer support system to ensure users can get help with any issues or questions they may have. This could include setting up an online help center, providing an email address or phone number for customer support, and offering live chat support.']
# slides = [['Professional slide decks difficult to create', 'Requires strong design skills', 'App can help save time and money'], ['Automated slide deck creation', 'Professional-looking presentations', 'Time-saving app'], ['App built with HTML, CSS, JavaScript', 'Backend language: Python, Ruby, Java', 'Hosted on web server'], ['Target: business professionals', 'Includes: entrepreneurs, marketers, etc', 'Need: engaging presentations quickly'], ['Research market, plan SlideSmart differentiation', 'Design and develop app to meet market needs', 'Test app for functionality and quality', 'Launch app, promote via social, email, ads; monitor and adjust'], ['Create comprehensive marketing plan', 'Develop a prototype of app', 'Partner with organizations and influencers']]

