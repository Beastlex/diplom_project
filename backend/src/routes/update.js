const express = require('express');

const router = express.Router();

router.get('/api/update', (req, res) => {
  res.send("Update");
});

module.exports = router;