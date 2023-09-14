
const express = require('express')
const path = require('path');
const app = express()
const hostname = process.env.BACKEND_HOST;
const port = process.env.BACKEND_PORT;

app.use(express.static(path.join(process.cwd(), 'build')));

app.get('/', function (_, res) {
    const options = {
        root: path.join(process.cwd(), 'build'),
        headers: {
          'Access-Control-Allow-Origin': `http://${hostname}:${port}`,
          'Access-Control-Allow-Methods': 'GET,OPTIONS',
          'Access-Control-Allow-Headers': '*'
        }
      }
    res.sendFile('index.html', options);
  });

app.listen(3000);
