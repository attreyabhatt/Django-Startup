Homepage 
- Section for Introduction
- Navbar
    - Icon buildwithpython - homepage
    - Courses
    - Login + Logout -> Popup ( Modal )
    - Signup -> Popup ( Modal ) -> Name + Email + PWD + Country
    - Blog (extra)
    - Pricing
    
- Current Courses
    Course Model - Title, Subtitle, Description, Thumbnail, type
    
- Testimonials

- Bottombar 
    - Social links
    - Privacy Policy
    - Copyright
    
- OptinPage
 Form - enter of screen
 Name, Country, Email
 
- Lesson Page
 Title, Video URL, course (foreign key to Course)
 
 Course -> Section -> Lessons
 
 TODO:
 1) Make the thankyou page better
 2) h-100 in cards on courses page
 3) We are going make our accordion better
 4) Add an icon or email confirm thingy in footer
 5) Footer getting broken on phone
 6) Accordion on course & lesson detail page should have a list
 7) Add a discussion on the lesson_detail page 
 8) Make the signup page look better
  - Handle form validation thingy {% if form.errors %} {{form.errors}} and use the render
 9) Login          ​
 
 
 Production Tasks:
 1) Do static files for production
 https://docs.djangoproject.com/en/3.1/howto/static-files/deployment/



 