# Food Fusion Blog


![Beige Brown Aesthetic Save The Date Editable Mockup Instagram Post (1)](###)


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
![1](###)

### (Logged in) Blogs
![1](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/a4c56a06-3692-467d-813a-ba3797d3087c)

### Add a Blog
![Add a book wireframe](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c0379553-0906-4d77-aca6-beb8fc6834d9)

## Agile:
This project was created using Agile principles via a projectboard on Github. This is the first time I have implemented Agile as an individual developer. However, creating user stories and identifying accepterance criteria acted as a roadmap to target the various features and functionalities of the application. It helped me stay on track and reduced distractions.

![project board](https://github.com/safihasan/food_blog2/blob/main/static/images/53B9389C-F8AD-43F6-8FE0-10F1B6B3898D.jpeg)


# Design Choices:

## Colour scheme:

#fafafa - Header

Dark Green - Buttons

#809977 - Footer

The colours were selected with the intention of complementing the food fusion blog and the idea was to ensure the image was appreciated.

## Typography:
 The following fonts were chosen for a clean and modern look that is both readable and minimal.

Varta

Goudy Book Letter 1911


## Priority Features:

### Home Page:

#### Navbar:
![home](###)

The landing page provides an introduction to the website with a call to action button encouraging new users to sign up. Signing up and logging in allows them access to view blogs written by other bloggers and comment on them. It also allows them to post their own food blog. The navigation bar is valuable for users as it provides quick and easy access to important sections of the website. The navigation bar includes links to Home, blogs, sign up, Register/Logout and Sign In.


#### Registration:

Registration allows users to view the blogs posted by them as well as by other bloggers. It allows them to add a blog as well as edit and delete their addition to ensure the food blog is updated regularly. 

![signup](###)



#### Sign In:

![sign-in](###)


#### Blogs:

![books](###)


#### About me:

![add a book](###)

#### Footer:

![footer](###)

Links in the footer redirect to respective social media pages.


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
![Food Fusion Flowchart](###)

The user flow chart for the Food Fusion website provides a clear, visual representation of the user's journey, helping to identify key features, plan a seamless user experience, and spot potential issues. It serves as an effective communication tool among stakeholders, guides the development process, aids in testing and validation, and supports user-centric design. By outlining each step of user interaction, the flow chart ensures comprehensive coverage of functionalities and assists in continuous improvement and iteration, ultimately ensuring a cohesive and user-friendly experience.

# Validation
## HTML

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2F) | ![home page validate](https://github.com/safihasan/food_blog2/blob/main/static/images/2181DB5B-00B2-450B-88C0-5FB6E9341865.jpeg) | Pass: Some errors but don't apply since it's base.html |
| Books | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Fbooks%2Fbooks%2F) | ![Validate Books page](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/b7c018c4-a68a-43ee-97c5-778658bbf705) | Pass: No Errors |
| Add a Book | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Fbooks%2Fadd_book%2F) | ![validate adda book page](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/95eb01b9-22fc-43c4-93de-0ebcd1263467) | Pass: No Errors |
| Sign In| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Faccounts%2Flogin%2F) | ![validate sign in](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/872629ce-e50d-4870-845b-ed699f9178dc) | Pass: No Errors |
| Register| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Faccounts%2Fsignup%2F) | ![validate sign up](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c5e042af-b3d5-4718-bc50-ef319ba1a1c3) | unclosed elements main and div |

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

* Macbook Air 2018 13.3-inch screen
* Lenovo Thinkpad 14" screen

 Mobile Devices:
* Google Pixel 4a

 * Browser Compatibility:
 
 I have tested the site using the following browsers:

* Google Chrome

![chrome](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/545ba4e5-c7bc-4fd8-8660-1444dcb3be2a)


* Microsoft Edge

![microsoft edge](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/1570a9cd-6591-45db-840b-ecbe7f7aeb5b)


I can confirm that the site is responsive and looks as expected good on different screen sizes.


Mobile devices:

![Screenshot_20231207-234024](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0f0b0d7d-a72f-43a4-8a57-bc1cf02a1367)

![Screenshot_20231207-234033](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/4c3cc202-b8f6-4f9d-b1bd-cf57c911db65)

![Screenshot_20231207-234013](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/39989e07-4e8d-4faf-8b57-e11686792b38)


![0](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/211095bf-ffac-42ca-b1c8-2a45d8444038)

![Screenshot_20231207-234117 (1)](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e52d022b-d3fb-4f6c-8fcb-092386ce566b)

![Screenshot_20231208-000014](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0cd224f9-b46e-4db9-9260-999cc63fff90)





Tablet Devices:


![homepage](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/5e6eb5c7-4aba-434c-8ed8-8bfd56632f8a)

![signup tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c5f5a237-83ee-4ef3-b9b0-444f648ca225)

![sign in tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/9ac1d08b-d4b8-4aa5-a65b-e46040f3b60b)

![books tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/a9c42d34-a49a-48ed-97ba-660c02de3543)

![tabletadd](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/b516d61d-6e21-460a-b7f4-5b18abf41d00)

![bookdetails tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/17a0f099-ae15-4b8a-887b-254beac2dbb0)





# Testing:

## Lighthouse Audit:

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.


* On a laptop:

Home

![homeaudit](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/5fa9bac2-d4bf-47fe-bb4a-50b3b0c4938b)

Books 

![auditbooks](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/d6401b01-e4d5-4ed1-b8e9-ff6d5eeb4bd9)

Add a book 
![audit add book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e429ee62-ecbe-4b2f-8521-28da15773a46)

On a mobile device:

Home 
![audit home mobile ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/348889e3-8c4e-41d4-b1c6-2c974780e23b)

Books
![auditbooks](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/fad662af-54da-45d0-b381-c0d70955e4e4)

Add a book 
![audit addbookmobile](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/634965ca-1b9d-4aa1-bd17-bda89f9fbafe)


## Links

| Link | Expected Outcome | Grade |
| ------- | ---------------- | ----- |
| Logo | Navigates to the home page when clicked | Pass |
| Home | Navigates to the home page when clicked | Pass |
| Blogs | Navigates to a blogs list  page when clicked | Pass |
| Add a Blog | Navigates to a form to add a blog when clicked | Pass |
| Register | Navigates to a registration form when clicked | Pass |
| Log in | Navigates to a screen where users can log in when clicked | Pass |
| Logout | Navigates to a page confirming for the user to log out | Pass |

## Testing 


| Feature | Expected Outcome | Grade | Screenshots |
| ------- | ---------------- | ----- | --------- |
| Modal | A message will appear informing the user of a successful action | Pass | ![modal sign out ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/9e8658e8-f751-4cdf-be3d-ca19ad6c47b2)
| User logged in | Text displays the user logged in with their username | Pass | ![modal sign in name](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/cc4a71db-9962-49c1-b4b6-563000687ad7)
| View blogs | Users can see available books which have been added | Pass | ![testing blogs](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/01cc3a5b-db46-4742-a8e1-cf715d78c89b)
| Add a blog | Add a book to the book collection that will be available to borrow | Pass | ![addblog](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/82133f44-d43a-4f40-863a-f4e8970057aa)
| Admin has access to crud functionality of all additions | Admin can edit or delete any book addition | Pass | ![admin testing](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/72df0b87-6d4f-4659-9d4f-5e986f88e16c)
| Edit a blog | A user can edit the details on the blog that they have addded. It will update their addition on the blogs page | Pass | ![edit book ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/79f6de7e-fd14-4c34-a474-483b7cd5285f)
| Delete a blog | A user who added a blog OR an admin can delete a blog. It will then be deleted from the DB | Pass | ![delete book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/88275723-e875-404a-b96f-58bac0a4907a)
| Registration | New users can access a registration form from the "Register" link | Pass | ![testing sign up](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e9e6c4e1-c90a-4854-a11c-014a8fc80043)
| Log in | Users can log in using a form after clicking "Log in" | Pass | ![sign in testing ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/3fafee34-e6d6-4162-8989-faa78e1bf355)
| Log out | Users get logged out after clicking "Log out" | Pass | ![testing sign out](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/d7d377aa-fc2d-4025-a73e-22d2d81c622a)
| Footer | A footer displays social information | Pass | ![footer](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0879fada-18a4-4363-8257-0af0061cf79f)
| Social links work | The social links will navigate to a new page when they're clicked. They will open in a new tab | Pass | ![footer](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0879fada-18a4-4363-8257-0af0061cf79f)


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

All the bugs that occured during the creation of this application have been resolved. There is a section of the application which allows you to reset your password that needs to be implemented, however they were not within the scope of this particular project and will be addressed in the near future along with the other future features.


# Credit: 

* I used the django blog resources provided on the LMS.

* Stack Overflow was used to solve any smaller bugs and further clarification on errors I was receiving in the terminal.

* I used this site to generate a persona and created user stories: https://founderpal.ai/user-persona-generator

* A special thanks to all the other indivudals in our cohort for their continuous support throughout the course.

* Gordon's photo was downloaded from the web.

* Font Awesome was used for icons and the fonts used were derived from Google Fonts.

* Wireframes, logo and flowcharts were created using Lucid charts. 
