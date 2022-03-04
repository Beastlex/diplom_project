const request = require('supertest');
const app = require('../server');

describe('Check endpoints', () => {
  it('check unexisting path', async () => {
    const res = await request(app).get('/api/wrong');
    expect(res.statusCode).toEqual(404);
  });

  it('check country codes', async () => {
    const res = await request(app).get('/api/countries');
    expect(res.statusCode).toEqual(200);
  });
});
