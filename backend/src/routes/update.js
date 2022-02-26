import express from 'express';

const router = express.Router();

router.get('/api/update', (req, res) => {
  res.send("Update");
});

export { router as updateRouter };