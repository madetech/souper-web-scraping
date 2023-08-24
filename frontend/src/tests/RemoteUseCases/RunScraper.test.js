import axios from 'axios';
import nock from 'nock';
import runScrape from '../../RemoteUseCases/RunScraper';
axios.defaults.adapter = 'http'

it('renders successfully', async () => {
  const scope = nock('http://localhost:8000')
    .get(`/scrape`)
    .reply(201
      , {
        'Access-Control-Allow-Origin': '*',
        'Content-type': 'application/json'
      });

  await runScrape();

  expect(scope.isDone()).toBe(true)
  nock.cleanAll()
});
