import express from 'express';
import { json } from 'body-parser';

import { statRouter } from './routes/stat';
import { updateRouter } from './routes/update';

const app = express();
app.use(json())

app.use(statRouter);


app.listen(5000, () => {
  console.log('Listening on port 5000');
})