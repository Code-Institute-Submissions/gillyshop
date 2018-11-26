[![Build Status](https://travis-ci.org/oheag2/gillyshop.svg?branch=master)](https://travis-ci.org/oheag2/gillyshop)

# Stream Three Project - Millennial Pink

Millennial Pink is a humourous and ironic online store that sells artworks/photographs aimed at millennials, with items that appeal to millennials such as cactii, galaxies, palm trees etc. 

My idea originally began as a vintage clothing store called Starry Starry Night. It then evolved into a jewellery store before eventually becoming an online art/photography store. The biggest challenge for an online art store was actually finding royalty free images that were of a high enough quality to use so the site evolved over time because of this. Ideally, it would contain art, illustrations and more typical millennial items like avocados, unicorns and llamas but finding images was a real challenge so I had to keep it more simple.

## UX

Starting off:

Most of my ideas begin as a visual representation in my head which is how Starry Starry Night began. I could see the exact type of font I wanted and so built the initial homepage around that in my head. When it evolved into Millennial Pink, I kept the visual framework the same and just adjusted the font to something more 'millennial'. My early drawings which can be found in the mockups section. I knew I wanted to keep the site layout clean and simple with a focus on some of the key art pieces to create a really nice visual entrance to the site. I made some wireframes to get an idea of how I wanted it to look and then began building the site.

Building the site:

The site was built using the lessons provided by Code Institute. While much of the code is my own, I also used the code from the lessons to build the site. 



## UX

I wanted to keep the layout for the dashboard quite simple but I also wanted to show how ridiculous Home and Away can be sometimes and really show the ways in which people have died, the fact that some people are always getting injured or having heart attacks and I wanted it to be a comical dashboard for users to enjoy. Therefore, some of the graphs are quite large and do contain a lot of information. I thought about scaling this back but it wouldn't have really conveyed what I wanted to show and I wanted to highlight stuff like the amount of people who get shot or die in car crashes which wouldn't be the same if I scaled back the data. 

I tried to incorporate some sort of beachy themed colour scheme but it ended up being too overbearing so I decided to just create rainbow coloured graphs, using the hex codes of Crayola crayons. I also made sure to include the Home and Away font so it felt more authentic. 

I drew some rough drawings on pen and paper to show how I wanted the dashboard to look. These can be found in the mockups section. 

Because of the sheer scale of some graphs, I removed the labels from some as they were overlapping too much and instead used legends to allow users interact with the graphs. 

I wanted users to enter the site and in the first graph to get a good idea of how many people have actually died in the last 23 years, and of course who faked their own death! The graphs move along to then show how people died, what the big storyline was and then further down, to show who these people were, where they lived and who they left behind. My main emphasis though was to show the ways in which people died so these graphs were kept to the start of the site. 


## Features

The site is simply laid out with a tour button to guide people through it in a comical way. I used a bright colour scheme with numerous colours to make the legend easier to navigate if labels weren't present. 

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