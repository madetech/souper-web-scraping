
const express = require('express')
var cors = require('cors')
const app = express()
const path = require('path');
const hostname = process.env.BACKEND_HOST;
const port = process.env.BACKEND_PORT;
const axios = require('axios')
var backend_url = process.env.REACT_APP_BACKEND_URL
var corsOptions = {
    origin: `${process.env.REACT_APP_BACKEND_URL}`
  }

app.use(cors(corsOptions))
app.use(express.static(path.join(process.cwd(), 'build')));

app.get('/', function (_, res, _) {
    res.sendFile('index.html');

  });

app.get('/reports', function(_, res) {
  axios.get(`${backend_url}/reports`)
  .then(backend_res => backend_res.status === 200 ? res.send(backend_res.data) : res.sendStatus(backend_res.status))
  .catch(next);
});



app.get(`/reports/:id/sections`, function(req,res) {
  var id = req.params['id']
  axios.get(`${backend_url}/reports/${id}/sections`)
  .then(backend_res => backend_res.status === 200 ? res.send(backend_res.data) : res.sendStatus(backend_res.status))
  .catch(next);
})

app.get(`/sections/:id/feedback`, function(req,res) {
  var id = req.params['id']
  axios.get(`${backend_url}/sections/${id}/feedback`)
  .then(backend_res => backend_res.status === 200 ? res.send(backend_res.data) : res.sendStatus(backend_res.status))
  .catch(next);
  
  })

app.post('/scrape', function(req, res) {
  axios.post(`${backend_url}/scrape`)
  .then(backend_res => res.status(backend_res.status))
  .catch(err => err);
  
});

app.get('/reports', function (_, res, next) {
  axios.get(`${backend_url}/reports`)
  .then(backend_res => backend_res.status === 200 ? res.send(backend_res.data) : res.sendStatus(backend_res.status))
  .catch(next);

})

app.get('/reports/:id/sections', function (req, res, next) {
  var id = req.params['id']
  axios.get(`${backend_url}/reports/${id}/sections`)
  .then(backend_res => backend_res.status === 200 ? res.send(backend_res.data) : res.sendStatus(backend_res.status))
  .catch(next);
})

app.get(`/sections/:id/feedback`, function (req, res, next) {
  var id  = req.params['id']
  axios.get(`${backend_url}/sections/${id}/feedback`)
  .then(backend_res => backend_res.status === 200 ? res.send(backend_res.data) : res.sendStatus(backend_res.status))
  .catch(next);
})

app.get('/scrape', function(req, res, next) {
  axios.get(`${backend_url}/scrape`)
  .then(backend_res => res.sendStatus(backend_res.status))
  .catch(next);
  })

app.use((err, req, res, next) => {
  console.log(err);
  res.sendStatus(500)
})

app.listen(3000);

