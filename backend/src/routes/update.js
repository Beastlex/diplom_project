const express = require('express');

const updateController = require('../controllers/update');

const router = express.Router();

router.get('/update', updateController.getPerformUpdate);
router.get('/last_update', updateController.getLastUpdate);
router.get('/healthz', updateController.getHealth);

module.exports = router;