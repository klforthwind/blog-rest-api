#How I Set Up This Blog
## 05/27/2019

Before you read further, I would like you to know that I was very dumb when I decided to make a blog like this. Clearly, there was a much simpler way towards creating a blog like this, but I was thinking to myself that I could lower the work needed to show every new post in the future whenever I needed to upload another one. And I wanted to save on storage space :P 

(When reading below, keep in mind, take everything with a grain of salt)

To begin, I decided that I wanted to work on a blog, one that I could learn very useful skills that I could use in the future. In this blog, there was no need for many html files linked by a href tags, because that would be **too** simple. I came to the conclusion that I should have a PostgreSQL database, since I could hold the data there instead of inside html files. The database would hold a url, title, tags, sources, text, and a date.

To interact with the database, I decided to run with a REST api written in python, which would serve data between website and database. I was very confident that the whole blog would use the REST api since the beginning, although it had to be tweaked since the database was not being used. The only problem is that I am using port 4242, which I cannot get my boss to unblock at my old high school. :P

I then decided to drop the database, since it was very unnecessary, so I just decided to make an array of dictionaries, (I do not know python that well), in order to hold post titles, urls and dates, which worked really well

The REST api was changes such that it would grab a Markdown file, and change it into html, and then the javascript script would receive said information and make some more syntax changes

The html website would interact with the python REST api through javascript, although I ran into a couple of problems:
1. I was not quite sure how the javascript would grab a specific blog post from the REST api, which I decided to use php and the $_GET[] process in order to get a specific blog post.
2. PHP files were not able to run through nginx, so I had to change the http.conf file in order to support PHP
3. Cross-Origin Resource Sharing (CORS) was a huge problem with getting data from REST api to the webpage, which I needed to add a specific statement to the REST api return functions

Once those problems were resolved, I messed around with the css in order to make it look better

Overall, I was really happy with it, although it took longer than I wish it would've
(It was probably because I was very dumb)

:)


#####Sources:
######[Python Markdown by trentm](https://github.com/trentm/python-markdown2 "Used for converting the markdown files")
######[Running Flask Over HTTPS by Miguel Grindberg](https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https "Used to make CORS not hate me")
######[Markdown Cheatsheet by adam-p](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet "Used for the markdown files")
######[Pygment.css by richleland](https://github.com/richleland/pygments-css "Used to color code blocks")
