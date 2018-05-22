# MyTube
This project is my own derivation from YouTube, which improves the flexibility when searching and makes it much easier for user to obtain the resources. This repo is only for demo purposes, I never and will never run it as a public service


## Structure
Using vuejs as front-end, python flask server, elasticsearch and mongoDB as search kernel, youtube-dl as download kernel.

## Usage
* Input a search pattern (keyword)

![](https://i.imgur.com/Ppl7klg.png)
* Input a range query format in the way like "year:year:options:number"
  * supported options
    * cview: According to count of views
    * clike: According to count of likes
    * chate: According to count of hates
    * subscribe: According to count of subscribes
    * rand: Randomly return

![](https://i.imgur.com/FfC8tQd.png)

  For example, the query "2015:2018:cview:100" will return the top 100 music with the highest views within the year 2015 to 2018.

![](https://i.imgur.com/LrFHg9W.png)

  You can hit the EXPLORE button to open a new blank towards the original sites, this project only aims for providing more flexible searching methods with users.
