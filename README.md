[![Build Status](https://travis-ci.org/oheag2/gillyshop.svg?branch=master)](https://travis-ci.org/oheag2/gillyshop)

# Stream Three Project - Millennial Pink

Millennial Pink is a humourous and ironic online store that sells artworks/photographs aimed at millennials, with items that appeal to millennials such as cactii, galaxies, palm trees etc.
My idea originally began as a vintage clothing store called Starry Starry Night. It then evolved into a jewellery store before eventually becoming an online art/photography store. The biggest challenge for an online art store was actually finding royalty free images that were of a high enough quality to use so the site evolved over time because of this. Ideally, it would contain art, illustrations and more typical millennial items like avocados, unicorns and llamas but finding images was a real challenge so I had to keep it simple. Over time, Millennial Pink would evolve to include illustrations, tote bags, mugs, and other kitschy millennial orientated items. 


## UX

Millennial Pink is a one stop shop for Irish shoppers to find everything for the millennials in their life. It is intended to be a destination where people can find very specific items rather than a broader website like Society 6. Millennials are blamed for ruining so many things and this site celebrates their unique interests and looks at what might appeal to them in ironic ways, like avocado toast Christmas ornaments and llamas wearing hats. 
User stories:
User A – A student
This student wants to find some artwork to decorate his college room. The homepage allows them a quick overview of some of the pictures available and allows them to click straight through to those sections.
The student clicks on the deer picture and is brought to the deer section where he picks a deer picture and adds it to his cart. This redirects him to the cart where he checks out straight away

User B – A mother
This mother wants to buy something for her daughter. She knows she likes pink and shes hoping to find something on the site for her daughter. She’s not much of an internet user so when she goes onto the site she goes to the products tab and sees that the products are arranged into helpful categories, including a pink one. Shes browses the pink products and adds one to the cart. She goes back to look for more and clicks on the pastel tag which brings her to other similarly coloured images. Here she finds something else that might appeal to her daughter also, she adds it to cart and checks out. 
Most of my ideas begin as a visual representation in my head which is how Starry Starry Night began. I could see the exact type of font I wanted and so built the initial homepage around that in my head. When it evolved into Millennial Pink, I kept the visual framework the same and just adjusted the font to something more 'millennial'. My early drawings which can be found in the mockups section. I knew I wanted to keep the site layout clean and simple with a focus on some of the key art pieces to create a really nice visual entrance to the site. I made some wireframes to get an idea of how I wanted it to look and then began building the site.
I wanted to somehow make the website pink but also be user friendly and not garish so I found a very light pink that wouldn’t be too overpowering. The font and look of thr website were very important to me so I spent a lot of time choosing correct fonts and eventually found one online for the header as well as picking a Google font for the main body. While I kept the main body a very light pink, I brought in other slightly brighter shades of pink for extra elements like buttons and navigation elements, as well as light grey and white. 




## Features

Homepage:
I wanted visitors to Millennial Pink to be greeted by a large full screen image on entering the site that would be visually impactful so I chose to use 4 of the images available for sale to create this impact.  I also wanted these images to be practical so clicking on them brings you straight to that section of the website. My mentor suggested I add some text somewhere to explain what the site is/does so I chose to layer this over the images so it was clear straight away what the site is/does. 
New in page:
This page allows users to immediately see what is new in perhaps since their last visit and to then go directly to those sections to shop whats new.

Products page:
The products page displays all the products together so users can shop everything at once.
Individual product category pages:
The products are then categorised into a few sections to allow shoppers only browse what theyre interested in, ie palm tree, pink products etc.
Product detail page:
The product detail page gives the user more info on what they’re buying – the type of the paper, the size, and it also allows users to see what the picture might look like on their wall in the frame mockup
Tag page:
This allows users to filter products by ‘tag’, for example blue products, purple products etc. It allows users another level of categorising products
Search page:
The search page allows user to search for items, searching through titles and product descriptions. I would have added tags to this too if I had more time. 
About us:
The about page tells the user what the ethos of Millennial Pink is and where they plan to go in the future. I didn’t want the page to feel and look stuffy so I used the header font to make it more visually appealing. 



Features left to implement:

- Responsive:

If I had more time, I would like to make the site more responsive

- Sizing issues

I think some of the graphs could be resized slightly to allow the labels to display a bit better and so that the legend isnt right on top of them/beside them.

## Technologies Used

- HTML - for the basic site layout
- CSS - to style the site
- [MongoDb](https://www.mongodb.com/) - I collected all the data I wanted from various sites and then created a database in MongoDb
- [Python](https://www.python.org/) - for the backend of the dashboard
- [Flask](https://www.fullstackpython.com/flask.html) - for the backend
- [Bootstrap](https://getbootstrap.com/) - to style the site and make it more responsive
- [D3](https://d3js.org/) - to create charts
- [DC](http://dc-js.github.io/dc.js/) - to make an interactive dashboard
- [Intro.js](https://introjs.com/) - to allow for a tour of the site
- [Crossfilter](https://github.com/square/crossfilter) - to allow data interaction
- [Javascript](https://www.javascript.com/) - to create graphs
- [Gunicorn](https://gunicorn.org/) - to help run the app
- [Pymongo](https://api.mongodb.com/python/current/) - to work with MongoDb
- [mLab](https://mlab.com/) - to host the database
- [Heroku](http://www.heroku.com) - to host the website
- [Google Fonts](https://fonts.google.com/) - for easy font integration
- [Pycharm](https://www.jetbrains.com/pycharm/) - started the dashboard here before moving it to Cloud9
- [Mongo Management Studio](http://mms.litixsoft.de/) - to update/maintain the database

## Testing

I tested the site on a number of browsers and devices to ensure it worked on all. I attempted numerous times to make the site more responsive on mobile devices but eventually realised it would take more time than I had. I added an 'overflow: auto' to the charts to allow them to overflow on mobile devices but if I had more time, I would have tried to make the graphs more responsive. However, given the scale of them, I'm not sure they would have ever worked very well on mobile devices as there were too many sections and labels. 

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