#Node, Npm, and Express
## 05/30/2019

So I have been putting off node and npm for a while, since I have been focusing on other things, but overall, node and npm are really really simple. Node allows javascript to be ran through the command line, while it uses npm in order to handle external packages. Npm is Node's package manager, being able to maintain all packages if the workspaces gets larger.

To create a workspace for Node, you need to make sure that you have npm.
```sh
sudo apt-get install npm
```

Afterwards you should be able to run the following in the workspace folder:
```sh
npm init
```
which will create a package.json file, looking somewhat like this:
```json
{
  "name": "test",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```
Basically the most important field in this json file is main, since that lets npm know that  index.js will be requiring certain node modules. To install a node module, you need type
```sh
npm install ____
```
Where the underline is where the name of the node module goes, in this case it would be express. For express, in index.js, the first two lines of the file should be:
```js
const express = require("express");
const app = express();
```
The first line grabs the module, and the second line makes an app out of the module. At the end of the file should be this line:
```js
app.listen(4000);
```
This line makes the app listen to port 4000 requests. You are able to change the port used for the node application, although you will need to add more code to handle them. The following code handles an HTTP GET request at ip_address:portNumber/ 
```js
app.get("/", (request, response) => {
    response.send(`This is an Express Api!`);
});
```
This will send the message to the browser if anyone tries to reach it with a get request. Each app call has a request and a response. The response parameter is used to send data to the client, and the request parameter is used to get more information from the link.

The following code can be reached at ip\_address:portNumber/dragon with a POST request, not a GET request:
```js
app.post("/dragon", (req, res) => {
    res.send(`You have reached the dragon`);
});
```
The following code can be reached at ip\_address:portNumber/wolf with any type of HTTP request:
```js
app.use("/wolf", (req, res) => {
    res.send(`You have reached the wolf`);
});
```
The following code can be reached at ip\_address:portNumber/monkey with a GET request, but if you access ip\_address:portNumber/monkey?name=ANYTHING, it will say "This is an ANYTHING Api":
```js
app.get("/monkey", (req, res) => {
    res.send(`This is an ${req.query.name} Api!`);
});
```
The following code can be reached at ip\_address:portNumber/cat/ANYTHING with a GET request, and it will use the ANYTHING as the name parameter. If ANYTHING is not provided, the following code will not be get, and you will need an app.get("/cat/") function:
```js
app.get("/cat/:name", (req, res) => {
    res.send(`This is an ${req.params.name} Api!`);
});
```
The following code had a typo when wrote, but I believe is important to know. You can access the following at ip\_addres:4000/lemurANYTHING, and it will print out successfully. If ANYTHING is not provided, the GET request will be unsuccessful:
```js
app.get("/lemur:name", (req, res) => {
    res.send(`This is an ${req.params.name} Api!`);
});
```

:)

[Example Code](https://github.com/klforthwind/blog-examples/blob/master/node-express/index.js "Node Express")

#####Sources:
######None
