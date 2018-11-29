[![Build Status](https://travis-ci.org/oheag2/gillyshop.svg?branch=master)](https://travis-ci.org/oheag2/gillyshop)

# Stream Three Project - Millennial Pink

Millennial Pink is a humourous and ironic online store that sells artworks/photographs aimed at millennials, with items that appeal to millennials such as cactii, galaxies, palm trees etc.
My idea originally began as a vintage clothing store called Starry Starry Night. It then evolved into a jewellery store before eventually becoming an online art/photography store. The biggest challenge for an online art store was actually finding royalty free images that were of a high enough quality to use so the site evolved over time because of this. Ideally, it would contain art, illustrations and more typical millennial items like avocados, unicorns and llamas but finding images was a real challenge so I had to keep it simple. Over time, Millennial Pink would evolve to include illustrations, tote bags, mugs, and other kitschy millennial orientated items. 

## UX

Millennial Pink is a one stop shop for Irish shoppers to find everything for the millennials in their life. It is intended to be a destination where people can find very specific items rather than a broader website like Society 6. Millennials are blamed for ruining so many things and this site celebrates their unique interests and looks at what might appeal to them in ironic ways, like avocado toast Christmas ornaments and llamas wearing hats. 

Most of my ideas begin as a visual representation in my head which is how Starry Starry Night began. I could see the exact type of font I wanted and so built the initial homepage around that in my head. When it evolved into Millennial Pink, I kept the visual framework the same and just adjusted the font to something more 'millennial'. My early drawings which can be found in the mockups section. I knew I wanted to keep the site layout clean and simple with a focus on some of the key art pieces to create a really nice visual entrance to the site. I made some wireframes to get an idea of how I wanted it to look and then began building the site.

I wanted to somehow make the website pink but also be user friendly and not garish so I found a very light pink that wouldn’t be too overpowering. The font and look of thr website were very important to me so I spent a lot of time choosing correct fonts and eventually found one online for the header as well as picking a Google font for the main body. While I kept the main body a very light pink, I brought in other slightly brighter shades of pink for extra elements like buttons and navigation elements, as well as light grey and white. 

### User stories:
#### User A – A student

This student wants to find some artwork to decorate his college room. The homepage allows them a quick overview of some of the pictures available and allows them to click straight through to those sections. The student clicks on the deer picture and is brought to the deer section where he picks a deer picture and adds it to his cart. This redirects him to the cart where he checks out straight away
#### User B – A mother

This mother wants to buy something for her daughter. She knows she likes pink and shes hoping to find something on the site for her daughter. She’s not much of an internet user so when she goes onto the site she goes to the products tab and sees that the products are arranged into helpful categories, including a pink one. Shes browses the pink products and adds one to the cart. She goes back to look for more and clicks on the pastel tag which brings her to other similarly coloured images. Here she finds something else that might appeal to her daughter also, she adds it to cart and checks out. 

## Features

### Homepage:

I wanted visitors to Millennial Pink to be greeted by a large full screen image on entering the site that would be visually impactful so I chose to use 4 of the images available for sale to create this impact.  I also wanted these images to be practical so clicking on them brings you straight to that section of the website. My mentor suggested I add some text somewhere to explain what the site is/does so I chose to layer this over the images so it was clear straight away what the site is/does. 

### New in page:

This page allows users to immediately see what is new in perhaps since their last visit and to then go directly to those sections to shop whats new.

### Products page:

The products page displays all the products together so users can shop everything at once.
Individual product category pages:
The products are then categorised into a few sections to allow shoppers only browse what theyre interested in, ie palm tree, pink products etc.

### Product detail page:

The product detail page gives the user more info on what they’re buying – the type of the paper, the size, and it also allows users to see what the picture might look like on their wall in the frame mockup

### Tag page:

This allows users to filter products by ‘tag’, for example blue products, purple products etc. It allows users another level of categorising products

### Search page:

The search page allows user to search for items, searching through titles and product descriptions. I would have added tags to this too if I had more time. 

### About us:

The about page tells the user what the ethos of Millennial Pink is and where they plan to go in the future. I didn’t want the page to feel and look stuffy so I used the header font to make it more visually appealing. 

### Cart page:

The cart page gives a simple layout of what the user is buying, the name, description and info as well as the price per item and total price

### Checkout:

The checkout is a simple form for users to fill in to pay. Once paid, it redirects them to the paid page

### Paid:

This is a simple page to inform users that they have paid and when to expect their item. It allows users the option to go to products to start shopping again

### Profile:

This gives the user a brief overview of their account. It includes their account email address, and some links to start/continue shopping, change their password or view their cart.

### Login/Register:

These are simple forms that allow existing users to login or new users to register.

### Password change:

This allows users to reset their password if they have forgotten it or just want to change it.

### Shipping/returns/stockists:

These pages give basic info on shipping details, returns and stockists

### Contact us:

This gives users the details needed to contact Millennial Pink as well as a contact form that allows users to submit questions, complaints and or feedback

## Features left to implement:

#### Search function

If I had more time, I would have improved the search functionality to return something when it doesnt find anything

#### Tag cloud/filter list

I had hoped to add a menu/list to filter by tag but ran out of time

#### Credit card integration

I tried lots of different credit cart plugins to allow for better formatting of my credit card form but could never get them to work properly/look right so I eventually reverted to my original layout.This is something I would have really like to have integrated.

#### Shipping costs

I would have liked to have integrated shipping costs in the checkout based on what the person was buying but again, I ran out of time. 

## Technologies Used

- HTML - for the basic site layout
- CSS - to style the site
- [Django Framework](https://www.djangoproject.com/) - to build the site
- [Python](https://www.python.org/) - for the backend 
- [Bootstrap](https://getbootstrap.com/) - to style the site and make it more responsive
- [Javascript](https://www.javascript.com/) - to create extra functionality
- [Django Taggit](https://github.com/alex/django-taggit) - to add tags
- [Amazon AWS](https://aws.amazon.com/) - to host my images and static files
- [Stripe](https://stripe.com) - to take payments
- [Gunicorn](https://gunicorn.org/) - to help run the app
- [Heroku](http://www.heroku.com) - to host the website
- [Google Fonts](https://fonts.google.com/) - for easy font integration
- [Font Awesome](https://fontawesome.com/) - for easy icons


## Testing

I tested the site on a variety of browsers and devices to ensure it worked correctly and used Chrome developer tools to make sure it worked responsively and looked nice on a number of screen sizes. 

I did a number of tests on the site to ensure all functionality was working properly:

### Homepage tests:

#### Test 1:

- Check the image carousel loads properly and that each image is a link and goes to the right section of the products.
- Check all links go to the correct place
- Check the back to top link works. 

Result - all checked and working correctly

#### Test 2: 

- Check the mailing list signup works and doesn't submit if email address is not valid/input is empty, alerts users that form submission was successful. 

Result - test passed. Popup appears if form submit is clicked when form is empty to say 'please fill out this field' and another popup appears if email address is not valid 'Please include @ in address'. Pop up informs users that it was succesfully submitted. 

### New In/About Us/Shipping/Returns/Stockists page tests:

### Test 1:

- Check all links work correctly and go where they're meant to 
- Check map loads correctly on Stockists page

Result - test passed, all links working correctly, map loading correctly. 

### Contact Page tests:

#### Test 1:

- Check that the form will not submit on clicking submit with empty form
- Check that the form will not submit when not all fields are filled in
- Check that the form gives an error if the email is not in the correct format
- Check that the form correctly submits when it is fully filled out and the user is made aware of this

Result - all tests passed. Form does not submit unless fully filled out, with all fields filled in the correct format. A pop up appears to inform users that it has been submitted. 

### Product Page tests:

- Ensure all titles and descriptions are correct
- Make sure all products are categorised correctly
- Make sure all products have appropriate tags and secondary images in product detail page
- Make sure add to cart button works for all products

Result - all tests passed. All product info is correct, all tags and secondary images work and add to cart works for all products from product page and product detail page. 

### Cart Page Tests:

- Check that products appear correctly in cart
- Check that cart items are amendable by quantity - amend up and items increase, amend to 0 and item is removed
- Check that cart total amends when items are added or removed
- Check links to return to products and proceed to checkout work correctly

Result - all tests passed. All product info is correct. Item quantities can be increased or decreased to add or remove items from cart. Cart total increases or decreases when items are added or removed. All links working fine. 

### Checkout tests:

- If not logged in, proceeding to checkout forces you to login
- Check that form will not submit when empty
- Check that the form will prompt you to fill in all your address details and will not submit unless these and payment details are filled in (except for Postcode which is not required)
- Check that the form gives you an error if you leave the credit card section blank
- Check that the form will submit when all details are entered correctly
- Check that checkout redirects to 'paid' when payment is successful

Result -all test passed. Proceeding to check out redirects you to the login page if you are not logged in. The form gives popup errors for fields not filled in correctly and stripe errors for any payment issues. The page redirects to paid.html if payment is successful. 

### Profile page tests:

- Check that if you are not logged in, clicking on profile redirects you to the registration page/option to signin if registered
- If you are logged in, check that profile icon goes to your profile page
- Check that if your cart is empty, your profile says 'start shopping'
- Check if cart has items in it, profile says 'continue shopping and 'go to cart'
- Check side panel displays user email address and username

Result - all tests passed. Profile options change depending on whether you are logged in or not. Side panel displays your email address and username

### Login Page tests:

- Check form doesnt submit if empty or if one field is empty
- Check for error if password or username are wrong
- Check form submits correctly and redirects to profile page

Result - all tests passed. Form submits correctly when filled in correctly and pops up errors if password or username is incorrect

### Registration page tests:

### Logout test:

- Check 'logout' logs users out of account. 

Result - test passed. User is logged out and redirected to homepage, profile icon changes to not logged in status



PSD mockups.images etc
use scans/mockups/tests to show stuff
 

Deployment
I initially started the Dashboard on Pycharm and after a lot of work, got it working locally. However I eventually ran out of a licence so spoke to Student Care who sorted me out with a new licence. However I was worried this would expire before I finished the dashboard so I spoke to Nakita who recommended I switch to Cloud9. This caused even more head scratching as I had to move everything and figure out how to get it work again from Cloud9 but after a lot of back and forth, I finally got everything working properly on Cloud9. This allowed me to then deploy to Heroku. I used mLab to host the database and again after a lot of confusion, I finally got Heroku to host the page. Looking back, I'm not sure why I struggled so much but when I took my time and read over everything clearly, it all made sense. However since moving to the new LMS for Stream 3, I think having videos of every step is a huge help so maybe that might have helped me at the time. My main struggle was getting the database hosted instead of having it locally which I struggled to really get a grasp on intially but finally got my head around after a while. I also didnt back up my project as much as I should because genuinely I forgot to so although I did eventually back up to Github, it was months after I first started the project and probably only when I moved the project to Cloud9.
Credits

Code used:
Written by me: about, contact, homepage, returns, stockists, shipping, cart, paid, products urls (mostly me) products views and tag view, static upload, password reset email actually sending (sorta)

Half me/half lessons: profile, checkout forms (to a degree), products model, search view, password reset

adapted from lessons: registration/reg form, login/login form, register/login/logout views/user profile view, password reset urls, checkout, cart urls/views, checkout models, checkout views, settings db, aws settings etc. 

Content
all social media links are not owned by me!!!
All content for this site was created by me. Using numerous Home and Away fan websites, Wikipedia and my own memories, I created a rough database in Excel as the framework for how I would create the database in MongoDB.
The sites I used were:
Back to the Bay
Home and Away Wiki
Your Gym Wiki
Wikipedia
Imagery
All images were found on Unsplash.com
Colour scheme
I used the hex codes for Crayola crayons to create a rainbow colour scheme. I kept the background white and simple and used the official Home and Away font to bring it all together.
Crayola Hex Codes
Home and Away font
Code Snippets
All code was written by me and/or adapted from the LMS lessons.
I also received great help on the Tutoring page from Nakita, Haley & Niel
/solution to tagging problem// https://www.youtube.com/watch?v=srHZoj3ASmk





## Deployment

I initially started the Dashboard on Pycharm and after a lot of work, got it working locally. However I eventually ran out of a licence so spoke to Student Care who sorted me out with a new licence. However I was worried this would expire before I finished the dashboard so I spoke to Nakita who recommended I switch to Cloud9. This caused even more head scratching as I had to move everything and figure out how to get it work again from Cloud9 but after a lot of back and forth, I finally got everything working properly on Cloud9. This allowed me to then deploy to Heroku. I used mLab to host the database and again after a lot of confusion, I finally got Heroku to host the page. Looking back, I'm not sure why I struggled so much but when I took my time and read over everything clearly, it all made sense. However since moving to the new LMS for Stream 3, I think having videos of every step is a huge help so maybe that might have helped me at the time. My main struggle was getting the database hosted instead of having it locally which I struggled to really get a grasp on intially but finally got my head around after a while. I also didnt back up my project as much as I should because genuinely I forgot to so although I did eventually back up to Github, it was months after I first started the project and probably only when I moved the project to Cloud9. 

## Credits

## Content
- All content for this site was created by me. Using numerous Home and Away fan websites, Wikipedia and my own memories, I created a rough database in Excel as the framework for how I would create the database in MongoDB. 

The sites I used were:

- [Back to the Bay](https://www.backtothebay.net)
- [Home and Away Wiki](https://homeandaway.fandom.com/wiki/Home_and_Away_Wiki) 
- [Your Gym Wiki](http://yourgymwiki.blogspot.com/2017/12/summer-bay_16.html)
- [Wikipedia](https://en.wikipedia.org/wiki/List_of_births,_marriages_and_deaths_in_Home_and_Away)

## Imagery

- I created the HA favicon in Photoshop

## Colour scheme

- I used the hex codes for Crayola crayons to create a rainbow colour scheme. I kept the background white and simple and used the official Home and Away font to bring it all together.
- [Crayola Hex Codes](http://www.colourlovers.com/web/blog/2008/04/22/all-120-crayon-names-color-codes-and-fun-facts)
- [Home and Away font](https://www.wfonts.com/font/reporter-two)

## Code Snippets

- All code was written by me and/or adapted from the LMS lessons.
- I also received great help on the Tutoring page from Nakita, Haley & Niel








/solution to tagging problem//
https://www.youtube.com/watch?v=srHZoj3ASmk

/solution to return nothing for no search items
https://stackoverflow.com/questions/38006125/how-to-implement-search-function-in-django