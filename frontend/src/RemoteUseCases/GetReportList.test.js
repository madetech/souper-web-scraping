import axios from 'axios';
import nock from 'nock';
import getList from './GetReportList';
axios.defaults.adapter = 'http'

it('renders successfully', async () => {
  const scope = nock('http://localhost:8000')
  .get('/reports')
  .reply(200, [{ id: 1, name: 'nocked data' }]
  , {
    'Access-Control-Allow-Origin': '*',
    'Content-type': 'application/json'
  });

  await getList();

  expect(scope.isDone()).toBe(true)
  nock.cleanAll()
});
