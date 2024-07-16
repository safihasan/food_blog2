# Food Fusion Blog


![Beige Brown Aesthetic Save The Date Editable Mockup Instagram Post (1)](https://github.com/safihasan/food_blog2/blob/main/static/images/82600DA0-9AEB-43C8-B96B-ADAE2A9F13F4.jpeg)


Welcome to Food Fusion! This is a Django-based blog application where food enthusiasts can share their culinary creations and discover new recipes. Users can submit their own food blogs, explore others' delicious posts, and engage with a community of food lovers. Whether you're a seasoned chef or a home cook, Food Fusion is the perfect platform to showcase your passion for food. Join us and start sharing your food adventures today!

The live application can be viewed here : 

https://food-fusion-6b16e48f61c5.herokuapp.com/


# Purpose and Target Audience:
 **Problem Statement:** Food enthusiasts often struggle to find a dedicated platform to share their unique recipes and food experiences. Existing social media platforms are overcrowded and lack a focused community for food blogging. There is a need for a specialized space where food lovers can easily create, share, and discover food blogs, connecting with like-minded individuals. Food Fusion addresses this gap by providing a user-friendly, Django-based application designed exclusively for food bloggers.

**Purpose:** The purpose of Food Fusion is to create a dedicated platform for food enthusiasts to share their culinary creations and experiences. This Django-based application aims to foster a community where users can easily submit their own food blogs, discover new recipes, and connect with other food lovers. By providing a specialized space for food blogging, Food Fusion encourages creativity, knowledge sharing, and community engagement among food aficionados.

**Target Audience:** Food Fusion is designed for food enthusiasts of all levels, including home cooks, professional chefs, food bloggers, and anyone passionate about cooking and sharing recipes. Our platform caters to individuals who enjoy documenting their culinary adventures, discovering new recipes, and engaging with a community of like-minded food lovers. Whether you're looking to showcase your latest kitchen creation or find inspiration from others, Food Fusion is the perfect place for you.



# Persona and User Stories:

Gordon Ramsay is a renowned chef and television personality known for his culinary expertise and vibrant personality. He enjoys sharing his recipes and cooking techniques with a broader audience and is looking for a dedicated platform to connect with food enthusiasts and fellow chefs. 

## User Stories:
* As a site user, I can view a paginated list of posts so that I can select which post I want to view.
* As a user I want to be able to view likes from readers on my blog.
* As a Site Admin, I can create or update the about page content so that it is available on the site.
* As a user I want to be able to create drafts.
* As a Potential Collaborator I can fill in a contact form so that I can submit a request for collaboration.
* As a Site Owner I can mark collaboration requests as "read" so that I can see how many I still need to process.
* As a Site Owner I can store collaboration requests in the database so that I can review them.
* As a Site User, I can click on the About link so that I can read about the site.
* As a site ownwer I  can Modify and delete comment on a post
* As a Site Admin, I can create or update the about page content so that it is available on the site.
* As a site user I want to be to comment on posts.
* As a site user I want to be able to view comments.
* As a site user I can register an account so that I can comment.

## Wireframe & Initial Design:
### Home Page
![1](https://github.com/safihasan/food_blog2/blob/main/static/wireframes/Register%20-%20Desktop.png)

### Blog view
![1](https://github.com/safihasan/food_blog2/blob/main/static/wireframes/Blog%20view%20-%20Desktop.png)

### About
![1](https://github.com/safihasan/food_blog2/blob/main/static/wireframes/About%20-%20Desktop.png)

### Register
![Add a register wireframe](https://github.com/safihasan/food_blog2/blob/main/static/wireframes/Register%20-%20Desktop.png)

### Sign in
![Add a sign in wireframe](https://github.com/safihasan/food_blog2/blob/main/static/wireframes/Sign%20in%20-%20Desktop.png)

## Agile:
This project was created using Agile principles via a projectboard on Github. This is the first time I have implemented Agile as an individual developer. However, creating user stories and identifying accepterance criteria acted as a roadmap to target the various features and functionalities of the application. It helped me stay on track and reduced distractions.

![project board](https://github.com/safihasan/food_blog2/blob/main/static/images/53B9389C-F8AD-43F6-8FE0-10F1B6B3898D.jpeg)


# Design Choices:

## Colour scheme:

#F9FAFC - Header

#188181 - Buttons

#445261 - Footer

The colours were selected with the intention of complementing the food fusion blog and the idea was to ensure the image was appreciated.

## Typography:
 The following fonts were chosen for a clean and modern look that is both readable and minimal.

Segoe UI

Times New Roman

Calibri (Body)


## Priority Features:

### Home Page:

#### Navbar:
![home](https://github.com/safihasan/food_blog2/blob/main/static/images/DBA9EF42-6351-4EB6-AF21-99EAC2A0B221.jpeg)

The landing page provides an introduction to the website with a call to action button encouraging new users to sign up. Signing up and logging in allows them access to view blogs written by other bloggers and comment on them. It also allows them to post their own food blog, once the page admin has granted them editing access. The navigation bar is valuable for users as it provides quick and easy access to important sections of the website. The navigation bar includes links to Home, blogs, sign up, Register/Logout and Sign In.

#### Blog view:

![blogs](https://github.com/safihasan/food_blog2/blob/main/static/images/382AD65C-3119-432C-BF58-DCE891A59F4E.jpeg)


#### About me:

![collaborate](https://github.com/safihasan/food_blog2/blob/main/static/images/BD6130A2-B2B6-4743-905F-16F170B531BB.jpeg)



#### Registration:

Registration allows users to view the blogs posted by them as well as by other bloggers. It allows them to add a blog as well as edit and delete their addition to ensure the food blog is updated regularly. 

![signup](https://github.com/safihasan/food_blog2/blob/main/static/images/E9282633-D116-48F2-A887-3AAA1BE2F7CD.jpeg)



#### Sign In:

![sign-in](https://github.com/safihasan/food_blog2/blob/main/static/images/8102319B-E211-4656-894C-F40471E792EE.jpeg)



# Future Features:

* User Profiles and Follow System: Allow users to create detailed profiles and follow their favorite food bloggers to stay updated with their latest posts.
* Recipe Ratings and Reviews: Implement a rating and review system for recipes, enabling users to provide feedback and share their cooking experiences.
* Interactive Cooking Classes: Offer live or recorded cooking classes hosted by professional chefs and experienced home cooks.
* Recipe Video Integration: Support for embedding videos within blog posts to provide visual cooking instructions and enhance user engagement.
* Advanced Search and Filters: Introduce advanced search functionality with filters for dietary preferences, cuisine types, cooking difficulty, and more.
* Ingredient List Management: Provide features for users to create and manage ingredient lists, including the ability to generate shopping lists from recipes.
* Mobile Application: Develop a mobile app for iOS and Android to allow users to access and interact with the platform on the go.


Database Design:

![ERD](https://github.com/safihasan/food_blog2/blob/main/static/images/DB%20Schema%20Food%20Fusion.png)


Entity Relationship Diagrams (ERD) help the developer to make connections between databases and information. Creating an ERD helped me understand how the tables relate to one another. I used LucidChart to create the diagram and the arrow represent how the data fields relate to one another.


## Data Models:


| User   |            |   |
|----------|:-------------:|------:|
| ID |  Integer | PK |
| Username |  String   |  Unique |
| Email | String | Unique  |
| password |  String | |
| first_name |  String   |    |
| last_name | String   |    |
| date_joined |  Date/Time | Auto insert current date |
| last_login |  Date/Time | Auto update on login |



| Blog  |            |   |
|----------|:-------------:|------:|
| blog_id |  Integer | PK |
| title |  String |  |
| author_id |  Integer | FK to User ID |
| created_at |  Date/Time | Auto insert current date |
| updated_at |  Date/Time | Auto update on edit |


| Comment   |            |   |
|----------|:-------------:|------:|
| comment_id |  Integer | PK  |
| blog_id |  Integer | FK to blog_id  |
| author_id |  Integer | FK to author_id  |
| created_at |  Date/Time | Auto insert current date |

## User Flow Chart:
![Food Fusion Flowchart](https://github.com/safihasan/food_blog2/blob/main/static/images/User%20flow%20chart.png)

The user flow chart for the Food Fusion website provides a clear, visual representation of the user's journey, helping to identify key features, plan a seamless user experience, and spot potential issues. It serves as an effective communication tool among stakeholders, guides the development process, aids in testing and validation, and supports user-centric design. By outlining each step of user interaction, the flow chart ensures comprehensive coverage of functionalities and assists in continuous improvement and iteration, ultimately ensuring a cohesive and user-friendly experience.

# Validation
## HTML

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](###) | ![home page validate](https://github.com/safihasan/food_blog2/blob/main/static/images/CAF0E0C4-4D1E-420B-BB55-5D742ED660A2.jpeg) | Pass: Some neglible errors |
| About me | [W3C](###) | ![validate adda book page](https://github.com/safihasan/food_blog2/blob/main/static/images/D38AB13A-B2B6-410D-AF5F-4183F8A51B18.jpeg) | Pass: Some neglible errors |
| Register| [W3C](###) | ![validate register](https://github.com/safihasan/food_blog2/blob/main/static/images/421D5066-2CC7-4FFB-9480-AC7592432F9E.jpeg) | Pass: Some neglible errors |
| Sign in | [W3C](###) | ![validate sign in](https://github.com/safihasan/food_blog2/blob/main/static/images/36AA4805-CD02-448C-9556-F3B6689E356F.jpeg) | Pass: No Errors |

 ## CSS

 I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.
 
| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](###) | ![validate css](https://github.com/safihasan/food_blog2/blob/main/static/images/6018DAAF-FF41-4EB3-9508-9322ADBE5408.jpeg) | Pass: No Errors |

## Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/safihasan/food_blog2/main/blog/models.py) | ![screenshot]![forms py](https://github.com/safihasan/food_blog2/blob/main/static/images/1FCFC449-C58F-4E5E-AE63-FFA2643FFF4A.jpeg)
 | Pass: Some neglible errors |
| settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/safihasan/food_blog2/main/food_fusion/settings.py) | ![screenshot]![settings py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/7951202c-2d55-4adb-90d6-8fef0707c82c)
 | Pass: No Errors |
| Blog views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/safihasan/food_blog2/main/blog/views.py) | ![screenshot]![views py](https://github.com/safihasan/food_blog2/blob/main/static/images/F4930AD3-E43E-4BEB-86D5-667FDC46E71B.jpeg)
 | Pass: 1 neglible error |
| Blog urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/safihasan/food_blog2/main/blog/urls.py) | ![screenshot]![urls py](https://github.com/safihasan/food_blog2/blob/main/static/images/5009FA40-7EE1-4E5F-8E52-DFFA2C07A186.jpeg)
 | Pass: No Errors |

# Responsiveness:
Development tools were used to test responsiveness on varying sized devices including laptop, mobile and tablet size.

Full testing was performed on the following devices:

Laptops:

* Macbook Air 2020 M1 13.3-inch screen
* Dell Inspiron 14

 Mobile Devices:
* Iphone 14 pro max

 * Browser Compatibility:
 
 I have tested the site using the following browsers:

* Google Chrome

![chrome](https://github.com/safihasan/food_blog2/blob/main/static/images/F98BDF95-BE30-4262-B873-6E098138C367.jpeg)


* Safari

![microsoft edge](https://github.com/safihasan/food_blog2/blob/main/static/images/74EABFE6-339A-46A1-9241-57274E73DBDE.jpeg)


I can confirm that the site is responsive and looks as expected good on different screen sizes.


Mobile devices:

![Screenshot_20231207-234024](https://github.com/safihasan/food_blog2/blob/main/static/images/2FFC08BB-BA8E-41F1-B74E-AA4270059A4B.jpeg)

![Screenshot_20231207-234033](https://github.com/safihasan/food_blog2/blob/main/static/images/4BC34382-83F6-43C5-9476-0587610232DB.jpeg)

![Screenshot_20231207-234013](https://github.com/safihasan/food_blog2/blob/main/static/images/A656BFBF-FCC9-4D9F-B0F0-FD3D0B8A6484.jpeg)


![0](https://github.com/safihasan/food_blog2/blob/main/static/images/645C900E-7468-4863-B810-BF54AA94D705.jpeg)





Tablet Devices:


![homepage](https://github.com/safihasan/food_blog2/blob/main/static/images/0691C149-6AFB-4003-8618-9DE2380DA4D6.jpeg)

![signup tablet](https://github.com/safihasan/food_blog2/blob/main/static/images/8239F6CF-150D-4384-B665-BB6B51DA2A71.jpeg)

![sign in tablet](https://github.com/safihasan/food_blog2/blob/main/static/images/DD514EC1-67A0-4C29-848C-6AF9D5A01A78.jpeg)





# Testing:

## Lighthouse Audit:

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.


* On a laptop:

Home

![homeaudit](https://github.com/safihasan/food_blog2/blob/main/static/images/FCD7DDF1-37A4-465B-85E2-FCBDB94AF9EC_4_5005_c.jpeg)

About

![auditbooks](https://github.com/safihasan/food_blog2/blob/main/static/images/43BA0444-EEA5-4B3E-AE38-10E042A615FF_4_5005_c.jpeg)


On a mobile device:

Home 
![audit home mobile ](https://github.com/safihasan/food_blog2/blob/main/static/images/FCD7DDF1-37A4-465B-85E2-FCBDB94AF9EC_4_5005_c.jpeg)

About
![auditbooks](https://github.com/safihasan/food_blog2/blob/main/static/images/43BA0444-EEA5-4B3E-AE38-10E042A615FF_4_5005_c.jpeg)

## Links

| Link | Expected Outcome | Grade |
| ------- | ---------------- | ----- |
| Logo | Navigates to the home page when clicked | Pass |
| Home | Navigates to the home page when clicked | Pass |
| Blogs | Navigates to a blogs list page when clicked | Pass |
| Register | Navigates to a registration form when clicked | Pass |
| Log in | Navigates to a screen where users can log in when clicked | Pass |
| Logout | Navigates to a page confirming for the user to log out | Pass |

## Testing 


| Feature | Expected Outcome | Grade | Screenshots |
| ------- | ---------------- | ----- | --------- |
| Modal | A message will appear informing the user of a successful action | Pass | ![modal sign out ](https://github.com/safihasan/food_blog2/blob/main/static/images/D2A5AF47-8E08-4375-9EAB-A8D6861A4D52.jpeg)
| User logged in | Text displays the user logged in with their username | Pass | ![modal sign in name](https://github.com/safihasan/food_blog2/blob/main/static/images/C0B5493F-8CCC-46D5-90F6-D385F565716C.jpeg)
| View blogs | Users can see available blogs which have been added | Pass | ![testing blogs](https://github.com/safihasan/food_blog2/blob/main/static/images/0691C149-6AFB-4003-8618-9DE2380DA4D6.jpeg)
| Add a blog | Add a blog for users to view, interact and comment. | Pass | ![addblog](https://github.com/safihasan/food_blog2/blob/main/static/images/7E62B367-6076-42F7-9079-E4AD4E04A0B6.jpeg)
| Admin has access to crud functionality of all additions | Admin can edit or delete any book addition | Pass | ![admin testing](https://github.com/safihasan/food_blog2/blob/main/static/images/6CAF2617-CEEE-413D-ACCA-29F66310593A.jpeg)
| Edit a blog | A user can edit the details on the blog that they have added. It will update their addition on the blogs page | Pass | ![edit blog ](https://github.com/safihasan/food_blog2/blob/main/static/images/D41266C9-5DB3-40C0-B74E-CAB5866BD859.jpeg)
| Delete a blog | A user who added a blog OR an admin can delete a blog. It will then be deleted from the DB | Pass | ![delete book](https://github.com/safihasan/food_blog2/blob/main/static/images/8E4D8BAF-3E18-4A07-8935-CB0FF00A1B24.jpeg)
| Registration | New users can access a registration form from the "Register" link | Pass | ![testing sign up](https://github.com/safihasan/food_blog2/blob/main/static/images/8239F6CF-150D-4384-B665-BB6B51DA2A71.jpeg)
| Log in | Users can log in using a form after clicking "Log in" | Pass | ![sign in testing ](https://github.com/safihasan/food_blog2/blob/main/static/images/8102319B-E211-4656-894C-F40471E792EE.jpeg)
| Log out | Users get logged out after clicking "Log out" | Pass | ![testing sign out](https://github.com/safihasan/food_blog2/blob/main/static/images/8918FC1C-D513-4157-A510-9138BBD02D58.jpeg)


# Tools and Technologies Used:
The technologies implemented in this application included HTML5, CSS, Bootstrap, Python and Django.

* Python used as the back-end programming language.
* Git used for version control. (git add, git commit, git push)
* GitHub used for secure online code storage.
* GitHub Pages used for hosting the deployed front-end site.
* Gitpod used as a cloud-based IDE for development.
* Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.
* Postgres used as the DB.
* Heroku used for hosting the deployed back-end site.
* Cloudinary used for online static file storage.
* Canva Utilized for collaborative design and prototyping(wireframes).

* Google and Stack Overflow utilized for general research or solving a bug, information gathering, and various online tools.


# Languages Used:
* HTML5
* CSS
* Python

# Deployment :

I used the steps used when deploying our django blog to deploy this application. The instructions for this mainly came from the follow along videos and text-steps provided on the code institute LMS.

# Bugs

All the bugs that occured during the creation of this application have been resolved. There were issues in deployment which were linked to database but these issues were timely resolved.

# Credit: 

* I used the django blog resources provided on the LMS, for design and code.

* Stack Overflow was used to solve any smaller bugs and further clarification on errors I was receiving in the terminal.

* I used chatgpt to generate a persona and created user stories.

* A special thanks to all the other indivudals in our cohort for their continuous support throughout the course.

* Gordon's photo was downloaded from the web.

* Font Awesome was used for icons and the fonts used were derived from Google Fonts.

* Wireframes, logo and flowcharts were created using Lucid charts. 
