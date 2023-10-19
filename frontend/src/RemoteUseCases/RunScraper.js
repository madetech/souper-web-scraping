import axios from "axios";

export default async function runScrape() {
    const result = await axios.get('/scrape')
        .then(res => res.status)
        .catch(err => err);
    return result;
}
