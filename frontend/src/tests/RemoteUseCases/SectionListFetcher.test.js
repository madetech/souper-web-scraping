import axios from 'axios';
import nock from 'nock';
import getSectionList from '../../RemoteUseCases/SectionListFetcher';
axios.defaults.adapter = 'http'

it('renders successfully', async () => {
  const id = 12

  const scope = nock('http://localhost:8000')
    .get(`/reports/${id}/sections`)
    .reply(200, [{ number: 1, decision: 'met' }]
      , {
        'Access-Control-Allow-Origin': '*',
        'Content-type': 'application/json'
      });

  await getSectionList(id);

  expect(scope.isDone()).toBe(true)
  nock.cleanAll()
});
