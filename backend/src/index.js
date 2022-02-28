const express = require('express');
const bodyParser = require('body-parser');

const statRouter = require('./routes/stat');
const updateRouter = require('./routes/update');

const app = express();
app.use(bodyParser.json())

app.use(statRouter);


app.listen(5000, () => {
  console.log('Listening on port 5000');
})