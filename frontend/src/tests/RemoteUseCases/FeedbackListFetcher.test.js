import axios from 'axios';
import nock from 'nock';
import getFeedbackList from '../../RemoteUseCases/FeedbackListFetcher';
axios.defaults.adapter = 'http'

it('renders successfully', async () => {
  const id = 12

  const scope = nock('http://localhost:8000')
    .get(`/sections/${id}/feedback`)
    .reply(200, [{"feedback":"This is a feedback","section_id":3,"id":34,"type":"constructive"}]
      , {
        'Access-Control-Allow-Origin': '*',
        'Content-type': 'application/json'
      });

  await getFeedbackList(id);

  expect(scope.isDone()).toBe(true)
  nock.cleanAll()
});
