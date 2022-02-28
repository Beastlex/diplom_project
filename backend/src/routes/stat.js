const express = require('express');

const router = express.Router();

router.get('/api/get_countries', (req, res) => {
  res.send("Cointries");
});

module.exports = router;