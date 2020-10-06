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
 8) Add login after signup
 9) Mailgun - Sending emails & django-anymail
 10) Add terms and and conditions
 
 Today's Objectives
 1) Payment Paypal
  - 1) Make sure the aprroval is secure - Api call to paypal + SubID + billing amt is zero ( for pending payments)
  - 2) Unsubscribe from our website - Delete Student model + Call to Paypal that the user has unsubed
  - 3) Unsubscribe from Paypal Interface - django Cron job
  - 4) Subscribed Date + Unsub after 30 days
  - 5) We need to do it for live instead of Sandbox
  
 2) Comments/Discussion
 
 
 Production Tasks:
 1) Do static files for production
 https://docs.djangoproject.com/en/3.1/howto/static-files/deployment/



 