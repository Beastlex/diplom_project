const express = require('express');
const bodyParser = require('body-parser');

const statRouter = require('./routes/stat');
const updateRouter = require('./routes/update');

const app = express();
app.use(bodyParser.json());

app.use('/api', statRouter);
app.use('/api', updateRouter);

app.use((req, res, next) => {
  console.log('No route to');
  res.status(404).json({ message: 'Not found!' });
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Server is live at localhost:${PORT}`);
});
