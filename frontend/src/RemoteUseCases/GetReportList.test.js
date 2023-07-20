
import getList from './GetReportList';
import axios from 'axios'
import nock from 'nock';
axios.defaults.adapter = 'http'

it('renders without crashing', async () => {

  const scope = nock('http://localhost:8008')
  .get('/report')
  .reply(200, [{ id: 1, name: 'nocked data' }]
  , {
    'Access-Control-Allow-Origin': '*',
    'Content-type': 'application/json'
  });

  await getList();

  expect(scope.isDone()).toBe(true)
  nock.cleanAll()
});