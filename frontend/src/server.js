
const express = require('express')
var cors = require('cors')
const app = express()
const path = require('path');
const hostname = process.env.BACKEND_HOST;
const port = process.env.BACKEND_PORT;

var corsOptions = {
    origin: 'http://localhost:8080'
}

app.use(cors(corsOptions))
app.use(express.static(path.join(process.cwd(), 'build')));



app.get('/', function (_, res, _) {
    res.sendFile('index.html');
  });

app.listen(3000);

