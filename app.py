from flask import Flask, session, render_template, Response, request, request, url_for, flash, redirect
from generate_content import *
import re

api_key = "your-key-here"

app = Flask(__name__)

app.config['SECRET_KEY'] = '2D78D94C49A787ECC0FEEEFB'
appName = "PitchPerfect"


slides = [['Professional slide decks difficult to create', 'Time-consuming and tedious process', 'Requires strong design skills'], ['Automated slide deck creation', 'Professional-looking presentations', 'Time-saving app'], ['App built with HTML, CSS, JavaScript', 'Backend language: Python, Ruby, Java', 'Hosted on web server'], ['Target: business professionals', 'Includes: entrepreneurs, marketers, etc', 'Need: engaging presentations quickly'], ['Research market, plan SlideSmart differentiation', 'Design and develop app to meet market needs', 'Test app for functionality and quality', 'Launch app, promote via social, email, ads; monitor and adjust'], ['Create comprehensive marketing plan', 'Develop a prototype of app', 'Partner with organizations and influencers']]

script = ['Slide', 'Maker', 'Say goodbye to tedious slide deck creation - SlideMaker does it for you!', 'Creating professional-looking slide decks quickly and easily is a big problem because it requires a lot of time and effort to design a well-crafted presentation. It also requires knowledge of design principles, an understanding of the target audience, and an ability to effectively communicate the desired message. Additionally, creating a professional-looking slide deck requires knowledge of the latest software and tools available, which can be difficult to keep up with. All of these factors make it challenging to create a professional-looking slide deck quickly and easily.', 'SlideMaker solves the problem of creating professional-looking slide decks quickly and easily. It allows users to quickly create a well-structured, visually appealing presentation without needing to have any design or technical skills. It also allows users to collaborate on the same presentation, making it easy to share ideas and get feedback.', 'The technical implementation for this start-up would likely involve a combination of web technologies and programming languages. On the web side, the app could be built using HTML, CSS, and JavaScript for the user interface. For the back-end, the app could be built using a server-side language such as PHP or Python, which would handle data storage and retrieval. Additionally, a database such as MySQL or MongoDB could be used for data storage. Finally, a library such as Reveal.js or Slides.js could be used to create the slide decks.', 'The target market for SlideMaker would be anyone who needs to create a professional-looking presentation, such as business professionals, educators, and students. It could also be used by marketers, entrepreneurs, and other professionals who need to create visually appealing presentations.', '1. Pre-Launch Preparation: Before you launch your app, it’s important to do research and create a plan for your product. This includes identifying target markets, understanding customer needs and wants, and developing a unique value proposition. Additionally, you should create a marketing plan, develop a pricing strategy, and create a website and other marketing materials.\n2. Launch: Once you’ve done your research and created a plan, it’s time to launch your app. This includes launching it on the app store, creating a website, and announcing it on social media. Additionally, you should create a landing page, build an email list, and create an online presence.\n3. Promotion: After launching your app, it’s important to promote it. This includes creating content such as blog posts, videos, and webinars to explain', '1. Establish a budget for marketing and advertising the app. This could include creating a website, running online ads, and utilizing social media platforms to reach potential users.\n2. Develop a user testing plan to identify any usability issues and improve the overall user experience. This could involve conducting interviews with potential users and soliciting feedback from existing users.\n3. Create a customer support system to ensure users can get help with any issues or questions they may have. This could include setting up an online help center, providing an email address or phone number for customer support, and offering live chat support.', 'Thanks']

long_script = """Slide 1:
 Introducing SlickDeck
Creating presentations has never been easier!

Slide 2:
Creating slide decks for presentations is a big problem because it can be time consuming and complex. It requires a lot of effort to create a visually appealing and informative slide deck that will engage the audience. It also requires a good understanding of design principles and the ability to create a logical flow of information. Additionally, it can be difficult to keep the presentation interesting and ensure that it is not too long or too short. Furthermore, the presentation needs to be tailored to the audience and their interests.Creating a slide deck also requires the presenter to be organized and have a good understanding of the material. This can be a challenge when the presenter is not familiar with the topic or has limited time to prepare. Additionally, the presenter needs to be able to create visuals that will capture the audience’s attention and make the presentation memorable.An app that solves the problem of creating slide decks for presentations can help save time and make the process easier. It can provide templates and guides to help the presenter create an effective and visually appealing presentation. Additionally, the app can provide tips and tricks to help the presenter create a compelling presentation and make sure it is tailored to the audience. This can help reduce the time and effort needed to create a successful

Slide 3:
SlickDeck is an app that solves the problem of creating slide decks for presentations. It makes the process of creating slide decks easier and quicker by providing users with a library of professionally designed slide templates. With these templates, users can quickly create a presentation without having to worry about the design of the slides. The app also provides users with the ability to customize the templates to meet their individual needs. Additionally, users can add their own images and text to the slides, as well as add animations and transitions. This makes the process of creating a presentation much more efficient and effective. SlickDeck also allows users to collaborate with others to create a presentation, as well as share their work with others. This makes it easier for teams to work together on a presentation and to make sure that everyone is on the same page. Overall, SlickDeck is a great tool for creating slide decks for presentations quickly and efficiently.

Slide 4:
The technical implementation for a start-up whose product is an app that makes slide decks for you would involve a combination of web technologies. Firstly, the app would be built using a client-side language like HTML, CSS, and JavaScript. This will ensure that the app is dynamic, interactive, and responsive. Additionally, the app would require a server-side scripting language like PHP or Ruby to handle the data processing and storage. A database such as MySQL or MongoDB would be used to store the user-generated content and data. Lastly, an API would be used to connect the app to other services and platforms.
The app would also require a cloud-based hosting solution like Amazon Web Services (AWS) to ensure scalability and reliability. AWS also provides a range of features such as security, analytics, and machine learning. Additionally, the app would be tested and deployed on a continuous integration platform such as Jenkins or Travis CI. This will ensure that the app is regularly updated and that any bugs or issues are quickly identified and addressed.

Slide 5:
 The target market for SlickDeck is professionals and students who need to create presentations but don't have the time or design skills to do so. SlickDeck is ideal for business owners, entrepreneurs, teachers, and students who want to create professional, visually appealing presentations quickly and easily. This app is also perfect for those who want to make a great impression with their audience by producing high-quality slides. SlickDeck is designed to be user-friendly and intuitive, so even those with no prior design experience can create stunning presentations. The app also offers an array of customization options, allowing users

Slide 6:
1. Pre-Launch Preparation: Before launching SlickDeck, it is important to conduct market research to understand the competitive landscape. Additionally, create a marketing plan that outlines the target market, key messaging, and distribution channels. This will help ensure a successful launch.
2. Launch: Once the market research and marketing plan are complete, it is time to launch SlickDeck. This could be done through a press release, social media posts, or even a paid advertising campaign.
3. Post-Launch Promotion: After the initial launch, it is important to continue promoting SlickDeck. This could include running ads, hosting webinars, or even creating a referral program.
4. Measure and Optimize: Finally, it is important to measure the success of SlickDeck and make adjustments as needed. This could include A/B testing different features, optimizing pricing, or refining the marketing message.

Slide 7:
1. Create a comprehensive marketing plan that outlines the target audience and key messages for the app.
2. Develop a prototype of the app to test the user experience and usability.
3. Reach out to potential partners, investors, and influencers to increase visibility and build relationships.

Slide 8:
Thank you for your time and attention during our presentation."""

img_url = "https://pbs.twimg.com/profile_images/1268196215587397634/sgD5ZWuO_400x400.png"

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        logo = request.form['logo']
        length = request.form['length']

        if not prompt:
            flash('Prompt is required!')
        elif not logo:
            flash('Logo is required!')
        elif not length:
            flash('Time is required!')
        else:
            length = int(re.search(r'\d+', length).group())
            length = (length - 2) * 40

            script = make_script(prompt, length, api_key)
            slides = get_slide_points(script, api_key)
            long_script = write_script_to_single_page(script)
            img_url = generate_logo(logo, api_key)
            print("Processing")
            return render_template('product.html', appName=appName, slides=slides, script=script, long_script=long_script, img_url=img_url)

    elif request.method == 'GET':
        return render_template('index.html', appName=appName)

    return render_template('index.html')

@app.route('/product/', methods=('GET', 'POST'))
def product():

    return render_template('product.html', appName=appName, slides=slides, script=script, long_script=long_script, img_url=img_url)

if __name__ == "__main__":
  app.run(debug=True)
