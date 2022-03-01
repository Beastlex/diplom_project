const express = require('express');

const statController = require('../controllers/stat');

const router = express.Router();

router.get('/countries', statController.getCountries);
router.post('/stats', statController.postStat);

module.exports = router;