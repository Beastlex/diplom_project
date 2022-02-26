import express from 'express';

const router = express.Router();

router.get('/api/get_countries', (req, res) => {
  res.send("Cointries");
});

export { router as statRouter };