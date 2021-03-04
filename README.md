# discord-visualizer

### How does it work?
It uses discord.py to collect the data and use a redis database on the computer to store them.  
Read <a href="https://redis.io/topics/persistence">this</a> before 
tinkering with this project.  
The `visualizer.py` file then converts all messages into a graph (that are over 50 occurrences)  
that file also has a search function to check what messages a word has been used in and how many occurrences it got  
(which is also shown in the graph)

<img src="https://raw.githubusercontent.com/iraizo/discord-visualizer/master/image.png" width="500">


 This data shows general english terms, which you can filter out, or i will add it later on.  
 You can also add in any filters you want to since the source code is easy to read
