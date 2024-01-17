
const express = require('express')
var cors = require('cors')
const app = express()
const path = require('path');
const hostname = process.env.BACKEND_HOST;
const port = process.env.BACKEND_PORT;
const axios = require('axios')
var backend_url = process.env.REACT_APP_BACKEND_URL
var corsOptions = {
  origin: `${process.env.REACT_APP_BACKEND_URL}`,
};

app.use(cors(corsOptions));
app.use(express.static(path.join(process.cwd(), 'build')));

app.get('/', function (_, res, _) {
  res.sendFile('index.html');
});

app.get('/reports', async function (_, res, next) {
  try {
    const result = await axios.get(`${backend_url}/reports`);
    if (result.status === 200) {
      res.send(result.data);
    } else {
      res.sendStatus(result.status);
    }
  } catch (error) {
    next(error);
  }
});

app.get('/reports/:id/sections', async function (req, res, next) {
  var id = req.params['id'];
  try {
    const backend_res = await axios.get(
      `${backend_url}/reports/${id}/sections`
    );
    if (backend_res.status === 200) {
      res.send(backend_res.data);
    } else {
      res.sendStatus(backend_res.status);
    }
  } catch (error) {
    console.error('Axios Error Sections:', error);
    next(error);
  }
});

app.get(`/sections/:id/feedback`, async function (req, res, next) {
  var id = req.params['id'];
  try {
    const backend_res = await axios.get(
      `${backend_url}/sections/${id}/feedback`
    );
    if (backend_res.status === 200) {
      res.send(backend_res.data);
    } else {
      res.sendStatus(backend_res.status);
    }
  } catch (error) {
    console.error('Axios Error Feedback:', error);
    next(error);
  }
});

app.get('/scrape', async function (req, res, next) {
  await axios
    .get(`${backend_url}/scrape`)
    .then((backend_res) => res.sendStatus(backend_res.status))
    .catch(next);
});

app.get('/counts', async function (_, res, next) {
  try{
  const result = await axios.get(
    `${backend_url}/datacounts`
  );
  if(result.status === 200) {
    res.send(result.data);
  } else {
    res.sendStatus(result.status);   
  }
} catch(error) {
  console.error('Axios Error Counts: ', error);
  next(error);
}
});

app.get('/resultcount', async function (_, res, next) {
  try {
    const result = await axios.get(`${backend_url}/resultcount`);
    if(result.status === 200) {
      res.send(result.data);
    } else {
      res.sendStatus(result.status);
    }
  } catch(error) {
    console.error('Axios Error Result Counts: ', error);
    next(error);
  }
  });

app.get('/average', async function (_,res, next) {
  try {
    const result = await axios.get(`${backend_url}/dataaverage`);
    if(result.status === 200) {
      res.send(result.data);
    } else {
      res.sendStatus(result.status);
    }
    } catch(error) {
      console.error('Axios Error Result Average: ', error);
      next(error);
  }});

app.use((err, req, res, next) => {
  console.log(err);
  res.sendStatus(500);
});

app.listen(3000);
